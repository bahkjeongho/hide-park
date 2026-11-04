import csv
import re
import urllib.request
import ssl
import json
import time

ctx = ssl.create_default_context()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

def resolve_linktree(url, username):
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, context=ctx, timeout=8).read().decode("utf-8")
        
        # Linktree 내부 데이터 탐색
        # 1. ba-reps.com 같은 username 기반 도메인 우선 탐색
        raw_urls = re.findall(r'https?://[^\s"\'<>]+', html)
        candidates = []
        for u in raw_urls:
            u_clean = u.replace("\\u0026", "&").replace("\\/", "/")
            if any(x in u_clean.lower() for x in [
                "linktr.ee", "cloudfront", "google", "facebook", "instagram", "tiktok",
                "youtube", "youtu.be", "twitter", "x.com", "threads.net", "spotify",
                "apple.com", "w3.org", "schema.org", "datagrail", "pxf.io", "linksynergy",
                "sjv.io", "wk5q.net"
            ]):
                continue
            candidates.append(u_clean)
        
        candidates = list(dict.fromkeys(candidates))
        if not candidates:
            return url
        
        # username이나 계정 관련 단어가 포함된 도메인 우선 선정
        u_base = username.replace("_", "").replace(".", "")
        for c in candidates:
            if u_base in c.replace("-", "").replace(".", "").lower():
                return c
        
        return candidates[0]
    except Exception as e:
        return url

in_path = "/Users/parkjeongho/Developer/Hide-Park/docs/ig-run/no-evidence-collected-fixed.csv"
out_path = "/Users/parkjeongho/Developer/Hide-Park/docs/ig-run/no-evidence-accounts-final.csv"

rows = []
with open(in_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append(r)

print(f"총 {len(rows)}개 행 로드됨. Linktree 및 모음 링크 2차 정제 시작...")
resolved_count = 0

for i, r in enumerate(rows):
    web = (r.get("Website") or "").strip()
    u = r.get("username", "").strip()
    if any(domain in web for domain in ["linktr.ee", "lit.link", "carrd.co"]):
        resolved = resolve_linktree(web, u)
        if resolved != web:
            r["Website"] = resolved
            resolved_count += 1
            print(f"[{i+1}/{len(rows)}] @{u}: {web} -> {resolved}")
        time.sleep(0.3)

# 최종 저장
fieldnames = ["username", "url", "display_name", "Website", "Bio", "All_Links", "분류", "사유", "수집상태"]
with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\n🎉 완료! Linktree 해결: {resolved_count}개")
print(f"최종 파일 생성됨: {out_path}")
