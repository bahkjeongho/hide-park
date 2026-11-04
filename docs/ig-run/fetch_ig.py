import os
import sys
import time
import json
import random
import urllib.request
import urllib.error
import urllib.parse
import ssl

# docs/ig-run/ 디렉토리 기준
D = os.path.dirname(os.path.abspath(__file__))
COOKIE_FILE = os.path.join(D, "ig_cookie.txt")

def get_session_id():
    """ig_cookie.txt 파일이 있으면 읽고, 없으면 환경변수나 콘솔 입력을 받음"""
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, "r", encoding="utf-8") as f:
            c = f.read().strip()
            if c:
                return c
    return os.environ.get("IG_SESSION_ID", "")

def fetch_profile(username, session_id):
    """
    인스타그램 웹 공식 내부 엔드포인트를 호출하여 프로필 정보를 가져옴
    """
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "X-IG-App-ID": "936619743392459",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "*/*",
        "Referer": f"https://www.instagram.com/{username}/",
        "Cookie": f"sessionid={session_id};"
    }

    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers=headers, method="GET")

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            user = data.get("data", {}).get("user", {})
            if not user:
                return None, "empty_user"

            # bio_links 추출
            bio_links = []
            for link in user.get("bio_links", []):
                u = link.get("url") or link.get("lynx_url")
                title = link.get("title", "")
                if u:
                    bio_links.append({"title": title, "url": u})

            # 외부 URL 단일 항목이 있는 경우 보합
            ext_url = user.get("external_url")
            if ext_url and not any(l["url"] == ext_url for l in bio_links):
                bio_links.insert(0, {"title": "Website", "url": ext_url})

            result = {
                "username": username,
                "full_name": user.get("full_name", ""),
                "biography": user.get("biography", ""),
                "category_name": user.get("category_name", ""),
                "is_private": user.get("is_private", False),
                "is_verified": user.get("is_verified", False),
                "bio_links": bio_links,
            }
            return result, "ok"

    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8")[:300]
        except Exception:
            pass
        if e.code == 404:
            return None, "not_found"
        elif e.code in (401, 403):
            return None, f"session_expired_or_blocked (code {e.code}, body: {body})"
        elif e.code == 429:
            return None, f"rate_limited (code {e.code}, body: {body})"
        else:
            return None, f"http_error_{e.code} (body: {body})"
    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    sid = get_session_id()
    if not sid:
        print("ERROR: ig_cookie.txt 파일에 sessionid를 넣거나 IG_SESSION_ID 환경변수를 지정하세요.")
        print(f"경로: {COOKIE_FILE}")
        sys.exit(1)

    # 샘플 테스트용 상위 3개 계정
    test_usernames = ["futurebless.studio", "designofficefun", "tangshuang"]
    print(f"--- 3개 계정 파일럿 테스트 시작 (sessionid 길이: {len(sid)}) ---")

    for u in test_usernames:
        print(f"\n조회 중: {u} ...")
        info, status = fetch_profile(u, sid)
        if status == "ok":
            print(f"  [성공]")
            print(f"  이름: {info['full_name']}")
            print(f"  카테고리: {info['category_name']}")
            print(f"  소개(Bio): {repr(info['biography'])}")
            print(f"  링크: {info['bio_links']}")
        else:
            print(f"  [실패] 사유: {status}")
        time.sleep(random.uniform(2.0, 3.5))
