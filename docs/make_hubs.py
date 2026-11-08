#!/usr/bin/env python3
"""A_Wiki와 B_Object(B1~B4)의 속성 값(Category … Topic)마다 허브 노트를 만든다. 지금은 스테이징 폴더에만 쓴다(볼트는 읽기만).

  python3 docs/make_hubs.py --out <스테이징폴더>
허브 본문의 자동 생성 구간은 <!-- hub:start --> ~ <!-- hub:end --> 이고, 다시 돌리면 이 구간만 바뀐다.
"""
import collections, os, re, sys

V = "/Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park"
W = V + "/A_Wiki"
K = ['Category', 'Sub-Category', 'Field', 'Sub-Field', 'Type', 'Sub-Type', 'Topic']
DOM, KIND = K[:4], K[4:6]
BIG = 150


def read(p):
    t = open(p, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    if not m:
        return None
    props, cur = {}, None
    for l in m.group(1).split('\n'):
        mm = re.match(r'^([A-Za-z-]+):', l)
        if mm:
            cur = mm.group(1)
        elif cur in K:
            x = re.match(r'^  - "\[\[(.*)\]\]"$', l)
            if x:
                props.setdefault(cur, []).append(x.group(1))
    return props


APPLY = '--apply' in sys.argv
HUB = W + '/A1_Hub'
TPL = "---\naliases:\ntags:\nRelated:\n---\n>[!tldr] tl;dr\n>\n\n"
MARK = re.compile(r'<!-- hub:start -->.*?<!-- hub:end -->', re.S)


def apply_one(v, fn, kind, txt, body, names, stat):
    if kind == 'new':
        os.makedirs(HUB, exist_ok=True)
        p = f"{HUB}/{fn}.md"
        if os.path.exists(p):
            stat['skip_exists'] += 1
            return
        open(p, 'w', encoding='utf-8').write(txt)
        stat['written_new'] += 1
        return
    p = V + '/' + names[v.lower()]
    old = open(p, encoding='utf-8').read()
    if MARK.search(old):
        new = MARK.sub(lambda m: body, old)
    elif old.strip() == '':
        new = TPL + body + '\n'
    else:
        new = old.rstrip('\n') + '\n\n' + body + '\n'
    open(p, 'w', encoding='utf-8').write(new)
    stat['written_existing'] += 1


def main():
    out = sys.argv[sys.argv.index('--out') + 1]
    names = {}
    for d, ds, fs in os.walk(V):
        ds[:] = [x for x in ds if x not in ('.obsidian', '.trash')]
        for f in fs:
            if f.endswith('.md'):
                names.setdefault(f[:-3].lower(), os.path.relpath(os.path.join(d, f), V))
    notes, obj = {}, set()
    for root in [W] + [V + '/B_Object/' + x for x in ('B1_Music', 'B2_Architecture', 'B3_Video', 'B4_Film')]:
        for d, _, fs in os.walk(root):
            if 'A1_Hub' in d.split(os.sep):
                continue
            for f in fs:
                if f.endswith('.md'):
                    pr = read(os.path.join(d, f))
                    if pr:
                        notes.setdefault(f[:-3], pr)
                        if root != W:
                            obj.add(f[:-3])
    uses = collections.defaultdict(collections.Counter)    # 값 -> 속성별 노트 수
    members = collections.defaultdict(set)                 # 값 -> 노트들
    parents = collections.defaultdict(collections.Counter)
    children = collections.defaultdict(collections.Counter)
    topics_in = collections.defaultdict(collections.Counter)
    for n, pr in notes.items():
        for k, vs in pr.items():
            for v in vs:
                uses[v][k] += 1
                members[v].add(n)
        for chain in ([pr.get(k, [None])[0] for k in DOM], [pr.get(k, [None])[0] for k in KIND]):
            c = [x for x in chain if x]
            for a, b in zip(c, c[1:]):
                if a != b:
                    children[a][b] += 1
                    parents[b][a] += 1
        t = (pr.get('Topic') or [None])[0]
        if t:
            for k in K[:6]:
                for v in pr.get(k, []):
                    if v != t:
                        topics_in[v][t] += 1
    hubs = set(uses)
    os.makedirs(out + '/new', exist_ok=True)
    os.makedirs(out + '/existing', exist_ok=True)
    stat = collections.Counter()
    for v in sorted(hubs):
        mem = sorted((m for m in members[v] if m not in hubs), key=str.lower)
        L = ['<!-- hub:start -->']
        kinds = ', '.join(f"{k} {c}" for k, c in uses[v].most_common())
        L += ['', f'> 속성: {kinds}', '']
        if parents[v]:
            L += ['# Parents', ''] + [f'- [[{p}]]' for p, _ in parents[v].most_common()] + ['']
        if children[v]:
            L += ['# Children', ''] + [f'- [[{c}]] ({n})' for c, n in children[v].most_common()] + ['']
        tp = [(t, c) for t, c in topics_in[v].most_common() if t != v]
        is_end = uses[v]['Topic'] > 0 and uses[v]['Topic'] == max(uses[v].values())
        is_end = is_end or (mem and all(m in obj for m in mem))   # B_Object 작품만 모인 값은 전부 나열
        if len(mem) > BIG and not is_end:
            if tp:
                L += ['# Topics', ''] + [f'- [[{t}]] ({c})' for t, c in tp] + ['']
            L += [f'> 노트 {len(mem)}개는 많아서 목록을 하위 분류와 Topic으로 나눠 보여 준다.', '']
            stat['big'] += 1
        else:
            L += [f'# Notes ({len(mem)})', ''] + [f'- [[{m}]]' for m in mem] + ['']
        L += ['<!-- hub:end -->']
        body = '\n'.join(L)
        kind = 'existing' if v.lower() in names else 'new'
        stat[kind] += 1
        fn = v.replace('/', '-')
        if fn != v:
            stat['slash'] += 1
        if kind == 'new':
            txt = f"---\naliases:\ntags:\nRelated:\nunlisted: true\n---\n>[!tldr] tl;dr\n>\n\n{body}\n"
        else:
            txt = body + '\n'
        open(f"{out}/{kind}/{fn}.md", 'w', encoding='utf-8').write(txt)
        if APPLY:
            apply_one(v, fn, kind, txt, body, names, stat)
    print(dict(stat), 'hubs', len(hubs))


main()
