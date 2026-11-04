import csv
import re
import urllib.request
import ssl
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
        
        u_base = username.replace("_", "").replace(".", "")
        for c in candidates:
            if u_base in c.replace("-", "").replace(".", "").lower():
                return c
        return candidates[0]
    except Exception:
        return url

KNOWN_CATEGORIES = [
    "시각 예술", "그래픽 디자이너", "작가", "사진작가", "사진가", "예술가", "음악가/밴드", 
    "디지털 크리에이터", "에디터", "건축가", "디자이너", "패션 디자이너", "제품/서비스",
    "예술 및 엔터테인먼트", "커뮤니티", "출판사", "의류(브랜드)", "미술관", "공예",
    "시각 연출자/미술 감독", "미술 및 공예 용품 상점", "비영리 단체", "교육"
]

JOB_KEYWORDS = [
    "디자이너", "디렉터", "아티스트", "작가", "포토그래퍼", "사진가", "건축", "일러스트", 
    "큐레이터", "에디터", "기획", "공예", "도예", "회화", "조각", "뮤지션", "음악", "프로듀서",
    "연구원", "교수", "대표", "founder", "co-founder",
    "designer", "director", "artist", "photographer", "architect", "illustrator", 
    "curator", "editor", "writer", "producer", "filmmaker", "stylist", 
    "ceramic", "studio", "craft", "researcher", "graphic", "visual"
]

def refine_job_and_category(bio, display_name, username):
    parts = [p.strip() for p in bio.split(" / ") if p.strip()]
    category = ""
    job_roles = []
    
    # 1. 알려진 카테고리 태그 탐색
    for p in parts:
        for cat in KNOWN_CATEGORIES:
            if p == cat or (cat in p and len(p) <= 20):
                category = p
                break
        if category: break

    # 2. 직업 키워드 또는 소속(@) 탐색
    for p in parts:
        if p == username or p == display_name or p == category:
            continue
        if p.startswith("bahkjeongho") or "팔로우합니다" in p:
            continue
        if p.isupper() and len(p) <= 10: # PLAYLIST, INSIGHT 등 하이라이트 이름 제외
            continue
            
        lower = p.lower()
        if any(kw in lower for kw in JOB_KEYWORDS) or ("@" in p and ("founder" in lower or "at" in lower or "with" in lower or len(p) <= 30)):
            job_roles.append(p)

    final_job = " | ".join(job_roles[:2])
    return category, final_job

in_path = "/Users/parkjeongho/Developer/Hide-Park/docs/ig-run/private-accounts-with-jobs-2026-11-03.csv"
out_path = "/Users/parkjeongho/Developer/Hide-Park/docs/ig-run/private-accounts-final.csv"

rows = []
with open(in_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append(r)

print(f"총 {len(rows)}개 행 처리 시작...")
lt_resolved = 0

for i, r in enumerate(rows):
    bio = r.get("Bio", "")
    disp = r.get("display_name", "")
    u = r.get("username", "")
    
    cat, job = refine_job_and_category(bio, disp, u)
    r["Category"] = cat
    r["Job_Role"] = job
    
    # Linktree 리졸브
    web = (r.get("Website") or "").strip()
    if any(domain in web for domain in ["linktr.ee", "lit.link", "carrd.co"]):
        resolved = resolve_linktree(web, u)
        if resolved != web:
            r["Website"] = resolved
            lt_resolved += 1
            print(f"[{i+1}/{len(rows)}] Linktree 해결: @{u} -> {resolved}")
        time.sleep(0.2)

fieldnames = ["username", "url", "display_name", "Category", "Job_Role", "Website", "Bio", "All_Links", "Is_Private", "분류", "사유", "수집상태"]
with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\n🎉 완료! Linktree 해결 {lt_resolved}개, 최종 파일 저장: {out_path}")
