#!/usr/bin/env python3
"""topic-dryrun-v5.csv 결과를 볼트 노트 frontmatter에 쓴다.

사용법 (레포 루트에서):
  python3 docs/apply_topic_props.py --notes "&Walsh.md" "&TEAM.md"   # 지정한 노트만
  python3 docs/apply_topic_props.py --all                            # CSV 전체
  --dry 를 붙이면 쓰지 않고 변경 예정만 센다.

규칙: 기존 줄은 그대로 두고 topic 블록 바로 뒤에 새 속성 줄만 삽입한다.
검증 실패 시 백업본(BACKUP)으로 되돌린다.
"""
import csv, hashlib, json, os, re, shutil, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT = "/Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park"
WIKI = VAULT + "/A_Wiki"
BACKUP = os.path.expanduser("~/Developer/hide-park-backup-20261105")
CSV = REPO + "/docs/topic-dryrun-v5.csv"
KEYS = [("Category", "category"), ("Sub-Category", "sub_category"), ("Field", "field"),
        ("Sub-Field", "sub_field"), ("Type", "type"), ("Sub-Type", "sub_type"),
        ("Topic", "new_topic")]


def q(v):
    if re.search(r'^[\s\-?:,\[\]{}#&*!|>\'"%@`]|: | #|\s$', v) or v.lower() in ("true", "false", "null", "yes", "no", "~"):
        return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return v


def split(t):
    m = re.match(r'---\n(.*?)\n---\n?', t, re.S)
    return (m.group(1), t[m.end():]) if m else (None, t)


def parse_many(fms):
    js = "const y=require('yaml');const a=JSON.parse(require('fs').readFileSync(0,'utf8'));" \
         "console.log(JSON.stringify(a.map(s=>{try{return y.parse(s)}catch(e){return '__ERR__'+e.message}})))"
    r = subprocess.run(["node", "-e", js], input=json.dumps(fms), capture_output=True, text=True, cwd=REPO)
    return json.loads(r.stdout)


def plan(row):
    """returns (new_text, inserted_lines) or (None, reason)"""
    p = os.path.join(WIKI, row["path"])
    t = open(p, encoding="utf-8").read()
    fm, body = split(t)
    if fm is None:
        return None, "no_frontmatter"
    lines = fm.split("\n")
    raw = {re.match(r'^([^:\s][^:]*):', l).group(1).strip() for l in lines if re.match(r'^[^\s#-][^:]*:', l)}
    low = {x.lower() for x in raw}
    # 소문자 topic은 기존 속성이므로 Topic(대문자)은 정확히 같은 철자일 때만 중복으로 본다
    if any((k in raw) if k == "Topic" else (k.lower() in low) for k, _ in KEYS):
        return None, "existing_property"
    ti = next((i for i, l in enumerate(lines) if re.match(r'^topic\s*:', l)), None)
    if ti is None:
        return None, "no_topic_key"
    end = ti + 1
    while end < len(lines) and (lines[end].startswith((" ", "\t", "- ")) or lines[end] == ""):
        end += 1
    new = []
    for k, c in KEYS:
        if row[c]:
            new += [f"{k}:", f'  - "[[{row[c]}]]"']
    if not new:
        return None, "no_values"
    lines[end:end] = new
    head = t[:t.index(fm)]
    return head + "\n".join(lines) + t[t.index(fm) + len(fm):], new


def verify(p, old, newt):
    ofm, ob = split(old)
    nfm, nb = split(newt)
    if hashlib.sha256(ob.encode()).digest() != hashlib.sha256(nb.encode()).digest():
        return "body_changed"
    ol, nl = ofm.split("\n"), nfm.split("\n")
    it = iter(nl)
    if not all(any(x == y for y in it) for x in ol):
        return "old_lines_changed"
    po, pn = parse_many([ofm, nfm])
    if isinstance(po, str) or isinstance(pn, str):
        return "yaml_error"
    added = {k for k, _ in KEYS}
    if {k: v for k, v in pn.items() if k not in added} != po:
        return "old_values_changed"
    return None


def main():
    a = sys.argv[1:]
    dry = "--dry" in a
    rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
    if "--all" in a:
        sel = rows
    else:
        names = a[a.index("--notes") + 1:] if "--notes" in a else []
        names = [n for n in names if not n.startswith("--")]
        sel = [r for r in rows if r["path"] in names]
    res = {"written": [], "skipped": [], "failed": []}
    for r in sel:
        newt, info = plan(r)
        if newt is None:
            res["skipped"].append((r["path"], info))
            continue
        p = os.path.join(WIKI, r["path"])
        old = open(p, encoding="utf-8").read()
        if dry:
            res["written"].append((r["path"], info))
            continue
        open(p, "w", encoding="utf-8").write(newt)
        err = verify(p, old, open(p, encoding="utf-8").read())
        if err:
            open(p, "w", encoding="utf-8").write(old)
            res["failed"].append((r["path"], err))
        else:
            res["written"].append((r["path"], info))
    import collections
    print("속성 줄 수(키 줄 기준):", sum(len([l for l in info if not l.startswith("  ")]) for _, info in res["written"]))
    print("건너뜀 사유:", dict(collections.Counter(i for _, i in res["skipped"])))
    print("CSV 행 수:", len(sel))
    for k, v in res.items():
        print(k, len(v))
        for x in v[:50]:
            print("  ", x)


main()
