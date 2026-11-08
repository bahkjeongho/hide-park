#!/usr/bin/env python3
"""모든 A_Wiki 노트와 B1_Music 노트에 Category … Topic 7개 속성 줄을 순서대로 채운다.
사용: python3 docs/fill_class_props.py --dry | --apply
- A_Wiki(A1_Hub 제외): 값 있는 기존 속성은 그대로, 없는 속성은 빈 줄로 추가, 7개를 한 덩어리로 정렬.
- B1_Music: Category=The Arts, Sub-Category=Music, Field=Popular Music, Type=Record,
  Topic에 EP/Studio Album/Single/Compilation 등이 있으면 그 값을 Sub-Type으로 옮기고 Topic은 비움.
검증: 본문 해시, 다른 속성 YAML 값, 7개 속성 값(기대값) 일치. 실패한 노트는 쓰지 않는다.
"""
import os, re, sys, json, hashlib, subprocess, collections
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "/Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park"
K7 = ["Category", "Sub-Category", "Field", "Sub-Field", "Type", "Sub-Type", "Topic"]
FORMATS = {"EP", "Studio Album", "Single", "Compilation", "Live Album", "Mini Album", "Remix Album", "Soundtrack"}
MUSIC_FIX = {"Category": "The Arts", "Sub-Category": "Music", "Field": "Popular Music", "Type": "Record"}

def split(t):
    m = re.match(r'---\n(.*?)\n---\n?', t, re.S)
    return (m.group(1), t[m.end():], m.end()) if m else (None, t, 0)

def blocks(fm):
    out = []
    for l in fm.split("\n"):
        m = re.match(r'^([^\s#\-][^:]*):', l)
        if m: out.append([m.group(1).strip(), [l]])
        elif out: out[-1][1].append(l)
        else: out.append(["", [l]])
    return out

def vals(ls):
    s = [ls[0].split(":", 1)[1].strip()] if ":" in ls[0] else []
    v = s + [x for x in ls[1:]]
    return re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', "\n".join(v)), "\n".join(v).strip(" -\n\t") == ""

def build(fm, music):
    bl = blocks(fm)
    keep = []; old = {}; pos = None
    for b in bl:
        if b[0] in K7:
            if pos is None: pos = len(keep)
            old[b[0]] = b[1]
        else: keep.append(b)
    if pos is None:
        pos = next((i + 1 for i, b in enumerate(keep) if b[0] == "aliases"), 0)
    want = {}
    if music:
        topic = vals(old["Topic"])[0] if "Topic" in old else []
        fmts = [x for x in topic if x in FORMATS]
        for k, v in MUSIC_FIX.items(): want[k] = [v]
        want["Sub-Type"] = fmts
        want["Topic"] = [x for x in topic if x not in FORMATS]
    new7 = []
    for k in K7:
        if music:
            v = want.get(k)
            if v is None: v = vals(old[k])[0] if k in old else []
            new7.append([k, [k + ":"] + [f'  - "[[{x}]]"' for x in v]])
        else:
            new7.append([k, old.get(k, [k + ":"])])
    allb = keep[:pos] + new7 + keep[pos:]
    return "\n".join(l for b in allb for l in b[1]), want

def parse_many(fms):
    js = "const y=require('yaml');const a=JSON.parse(require('fs').readFileSync(0,'utf8'));console.log(JSON.stringify(a.map(s=>{try{return y.parse(s)}catch(e){return '__ERR__'}})))"
    out = []
    for i in range(0, len(fms), 300):
        r = subprocess.run(["node", "-e", js], input=json.dumps(fms[i:i+300]), capture_output=True, text=True, cwd=REPO)
        out += json.loads(r.stdout)
    return out

def norm(v):
    if v is None: return []
    if not isinstance(v, list): v = [v]
    return [str(x).strip() for x in v if x is not None and str(x).strip()]

def main():
    apply = "--apply" in sys.argv
    jobs = []
    for sub, music in (("A_Wiki", False), ("B_Object/B1_Music", True)):
        for r, _, fs in os.walk(os.path.join(V, sub)):
            if "A1_Hub" in r.split(os.sep): continue
            for f in fs:
                if not f.endswith(".md"): continue
                p = os.path.join(r, f); t = open(p, encoding="utf-8").read()
                fm, body, end = split(t)
                if fm is None: jobs.append((p, None, None, None, music, None)); continue
                nfm, want = build(fm, music)
                nt = "---\n" + nfm + "\n---" + t[end - (1 if t[end-1:end] == "\n" else 0):] if False else t[:t.index(fm)] + nfm + t[t.index(fm) + len(fm):]
                jobs.append((p, t, fm, nfm, music, nt))
    todo = [j for j in jobs if j[1] is not None]
    parsed = parse_many([x for j in todo for x in (j[2], j[3])])
    st = collections.Counter(); fails = []; nofm = 0; writes = []
    for i, j in enumerate(todo):
        p, t, fm, nfm, music, nt = j
        o, n = parsed[2*i], parsed[2*i+1]; err = None
        if not isinstance(o, dict) or not isinstance(n, dict): err = "yaml"
        else:
            if hashlib.sha256(split(t)[1].encode()).digest() != hashlib.sha256(split(nt)[1].encode()).digest(): err = "body"
            for k, v in o.items():
                if k in K7: continue
                if norm(v) != norm(n.get(k)): err = err or "other:" + k
            if not music:
                for k in K7:
                    if norm(o.get(k)) != norm(n.get(k)): err = err or "k7:" + k
            else:
                nm = lambda v: [re.sub(r"^\[\[|\]\]$", "", x) for x in norm(v)]
                ot = nm(o.get("Topic")); exp_st = [x for x in ot if x in FORMATS]; exp_t = [x for x in ot if x not in FORMATS]
                if nm(n.get("Sub-Type")) != exp_st or nm(n.get("Topic")) != exp_t or norm(n.get("Category")) != ["[[The Arts]]"]: err = err or "music"
                if "Sub-Type" in o and norm(o["Sub-Type"]): err = err or "had_subtype"
        if err: fails.append((p, err)); continue
        st["music" if music else "wiki"] += 1
        if nt != t: writes.append((p, nt)); st["changed"] += 1
    if apply:
        for p, nt in writes: open(p, "w", encoding="utf-8").write(nt)
    print("대상", dict(st), "실패", len(fails), "frontmatter 없음", len(jobs) - len(todo))
    for x in fails[:15]: print("  FAIL", x)
main()
