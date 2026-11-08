#!/usr/bin/env python3
"""B_Object (B1_Music, B2_Architecture, B3_Video) 속성을 새 순서로 정리한다.
사용: python3 docs/apply_object_props.py --dry | --apply
규칙: 순서 고정, 키 첫 글자 대문자, topic 값은 Topic으로 그대로 이동, 빈 속성도 줄로 만듦,
      Genre/Date/title/type/Type은 삭제(Architecture는 해당 없음), 정해지지 않은 다른 키는 Related 뒤에 보존.
검증: 본문 해시 동일, 옮긴 값 YAML 파싱 동일. 실패 시 되돌림.
"""
import os, re, sys, json, hashlib, subprocess, collections
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBJ = "/Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park/B_Object"
CLS = ["Category", "Sub-Category", "Field", "Sub-Field", "Type", "Sub-Type", "Topic"]
ORDER = {
 "B1_Music": ["aliases"] + CLS + ["Artist", "Creative", "Client", "Year", "URL", "tags", "Related"],
 "B2_Architecture": ["aliases"] + CLS + ["Architect", "Program", "Cities", "Countries", "Year", "URL", "tags", "Related"],
 "B3_Video": ["aliases"] + CLS + ["Creative", "URL", "tags", "Related"],
}
RENAME = {"aliases": "aliases", "topic": "Topic", "artist": "Artist", "creatives": "Creative", "year": "Year", "architect": "Architect"}
DROP = {"title", "genre", "date", "type"}  # 소문자 비교; 새 Type은 CLS에서 빈 줄로 만든다

def split(t):
    m = re.match(r'---\n(.*?)\n---\n?', t, re.S)
    return (m.group(1), t[m.end():], m.end()) if m else (None, t, 0)

def blocks(fm):
    out = []  # (key, [lines])
    for l in fm.split("\n"):
        m = re.match(r'^([^\s#\-][^:]*):(.*)$', l)
        if m: out.append([m.group(1).strip(), [l]])
        elif out: out[-1][1].append(l)
    return out

def nonempty(lines):
    first = lines[0].split(":", 1)[1].strip()
    if first: return True
    return any(re.sub(r'^\s*-?\s*', '', x).strip() for x in lines[1:])

def items(lines):
    """블록의 값 줄(키 줄 뒤)과 한 줄 값"""
    first = lines[0].split(":", 1)[1].strip()
    return first, [x for x in lines[1:] if re.sub(r'^\s*-?\s*', '', x).strip()]

def build(folder, fm):
    want = ORDER[folder]
    got = collections.OrderedDict(); extra = []; dropped = []
    for k, ls in blocks(fm):
        lk = k.lower()
        nk = RENAME.get(lk, k[0].upper() + k[1:] if lk not in DROP else k)
        if lk == "type" or lk in DROP:
            if nonempty(ls): dropped.append(k)
            continue
        if nk in want or nk == "aliases":
            nk = nk if nk in want else nk
        if nk in want:
            if nk in got and nonempty(got[nk]) and nonempty(ls):
                # 둘 다 값이 있으면 이어 붙임(한 줄 값은 목록 항목으로)
                a1, ai = items(got[nk]); b1, bi = items(ls)
                lines = [nk + ":"]
                for v in (a1, b1):
                    if v: lines.append("  - " + v)
                got[nk] = lines + ai + bi; continue
            if nk in got and nonempty(got[nk]): continue
            ls = [nk + ls[0][len(k):]] + ls[1:]
            got[nk] = ls
        else:
            extra.append((nk, [nk + ls[0][len(k):]] + ls[1:]) if nk != k else (k, ls))
    new = []
    for k in want:
        if k in got: new += got[k]
        else: new.append(k + ":")
    for k, ls in extra:
        if nonempty(ls): new += ls  # 값 없는 알 수 없는 키는 정리
    return "\n".join(new), dropped, [k for k, ls in extra if nonempty(ls)]

def parse_many(fms):
    js = "const y=require('yaml');const a=JSON.parse(require('fs').readFileSync(0,'utf8'));console.log(JSON.stringify(a.map(s=>{try{return y.parse(s)}catch(e){return '__ERR__'+e.message}})))"
    r = subprocess.run(["node", "-e", js], input=json.dumps(fms), capture_output=True, text=True, cwd=REPO)
    return json.loads(r.stdout)

def norm(v):
    if v is None: return []
    if not isinstance(v, list): v = [v]
    return [str(x).strip() for x in v if x is not None and str(x).strip()]

def check(old_fm, new_fm, folder):
    o, n = parse_many([old_fm, new_fm])
    if isinstance(o, str) or isinstance(n, str) or o is None or n is None: return "yaml_error"
    ol = {}
    for k, v in o.items():
        ol.setdefault(k.lower(), [])
        ol[k.lower()] = ol[k.lower()] + norm(v)
    for k in ORDER[folder]:
        src = [x for x in (k.lower(),) if x in ol]
        if k == "Creative": src = ["creatives"] if "creatives" in ol else []
        want = []
        for s in ([k.lower()] + (["creatives"] if k == "Creative" else [])):
            if s in ol and not (s == "type"): want += norm(ol[s])
        if k in CLS and k != "Topic": want = []
        if k == "Topic": want = norm(ol.get("topic"))
        if k == "Year": want = norm(ol.get("year")) if "year" in ol else []
        if sorted(want) != sorted(norm(n.get(k))): return "value_mismatch:" + k
    return None

def main():
    apply = "--apply" in sys.argv
    stats = collections.Counter(); fails = []; dropped = collections.Counter(); extras = collections.Counter(); nofm = []
    for folder in ORDER:
        for r, _, fs in os.walk(os.path.join(OBJ, folder)):
            for f in sorted(fs):
                if not f.endswith(".md"): continue
                p = os.path.join(r, f)
                t = open(p, encoding="utf-8").read()
                fm, body, end = split(t)
                if fm is None: nofm.append(p); continue
                nfm, dr, ex = build(folder, fm)
                for d in dr: dropped[d] += 1
                for e in ex: extras[e] += 1
                nt = "---\n" + nfm + "\n---\n" + body if t[end-1:end] == "\n" else "---\n" + nfm + "\n---" + body
                err = check(fm, nfm, folder)
                if hashlib.sha256(split(nt)[1].encode()).digest() != hashlib.sha256(body.encode()).digest(): err = err or "body_changed"
                if err: fails.append((p, err)); continue
                stats[folder] += 1
                if apply and nt != t:
                    open(p, "w", encoding="utf-8").write(nt)
    print("대상", dict(stats), "실패", len(fails), "frontmatter 없음", len(nofm))
    print("삭제되는 값(키: 값 있는 노트 수)", dict(dropped))
    print("보존되는 추가 키", dict(extras))
    for x in fails[:20]: print("  FAIL", x)
    for x in nofm: print("  NOFM", os.path.basename(x))
main()
