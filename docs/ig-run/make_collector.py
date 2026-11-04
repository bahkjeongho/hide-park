import csv
import json
import os

D = "/Users/parkjeongho/Developer/Hide-Park/docs/ig-run"
csv_path = os.path.join(D, "no-evidence-accounts-park.csv")

accounts = []
with open(csv_path, "r", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        accounts.append({
            "username": r["username"].strip(),
            "url": r["url"].strip(),
            "display_name": r.get("display_name", "").strip(),
            "분류": r.get("분류", "").strip(),
            "사유": r.get("사유", "").strip()
        })

accounts_json = json.dumps(accounts, ensure_ascii=False)

js_code = """// 인스타그램 Bio & Website 자동 수집기
// 브라우저 개발자 도구 콘솔에 붙여넣고 실행하세요.
(() => {
  const ACCOUNTS = """ + accounts_json + """;
  let isPaused = false;
  let currentIndex = 0;
  const results = [];

  // 1. 화면 우측 상단 플로팅 UI 생성
  const oldUI = document.getElementById("ig-collector-ui");
  if (oldUI) oldUI.remove();

  const ui = document.createElement("div");
  ui.id = "ig-collector-ui";
  ui.style.cssText = "position:fixed; top:20px; right:20px; z-index:999999; background:rgba(20,20,20,0.95); color:#fff; padding:16px 20px; border-radius:12px; box-shadow:0 8px 32px rgba(0,0,0,0.5); font-family:system-ui, -apple-system, sans-serif; font-size:13px; width:340px; border:1px solid #555;";
  ui.innerHTML = `
    <div style="font-weight:bold; font-size:15px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
      <span>📸 IG Bio & Website 수집기</span>
      <span id="ig-col-prog" style="color:#c084fc; font-size:13px;">0 / ` + str(len(accounts)) + `</span>
    </div>
    <div id="ig-col-curr" style="color:#aaa; font-size:12px; margin-bottom:10px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">준비 중...</div>
    <div style="background:#333; height:7px; border-radius:4px; margin-bottom:14px; overflow:hidden;">
      <div id="ig-col-bar" style="background:#a855f7; height:100%; width:0%; transition:width 0.3s;"></div>
    </div>
    <div style="display:flex; justify-content:space-between; margin-bottom:12px; font-size:12px; color:#bbb;">
      <span>발견된 웹사이트: <b id="ig-col-count" style="color:#34d399;">0</b>개</span>
    </div>
    <div style="display:flex; gap:8px;">
      <button id="ig-col-pause-btn" style="flex:1; background:#374151; color:#fff; border:none; padding:8px 10px; border-radius:6px; cursor:pointer; font-weight:bold; font-size:12px;">일시정지</button>
      <button id="ig-col-save-btn" style="flex:1.2; background:#059669; color:#fff; border:none; padding:8px 10px; border-radius:6px; cursor:pointer; font-weight:bold; font-size:12px;">현재 결과 CSV 저장</button>
    </div>
  `;
  document.body.appendChild(ui);

  const progEl = document.getElementById("ig-col-prog");
  const currEl = document.getElementById("ig-col-curr");
  const barEl = document.getElementById("ig-col-bar");
  const countEl = document.getElementById("ig-col-count");
  const pauseBtn = document.getElementById("ig-col-pause-btn");
  const saveBtn = document.getElementById("ig-col-save-btn");

  pauseBtn.onclick = () => {
    isPaused = !isPaused;
    pauseBtn.innerText = isPaused ? "▶ 계속하기" : "⏸ 일시정지";
    pauseBtn.style.background = isPaused ? "#d97706" : "#374151";
    if (!isPaused) runLoop();
  };

  saveBtn.onclick = () => downloadCSV();

  function cleanUrl(raw) {
    if (!raw) return "";
    let u = raw;
    if (u.includes("l.instagram.com/?u=")) {
      const m = u.match(/[?&]u=([^&]+)/);
      if (m) u = decodeURIComponent(m[1]);
    }
    try {
      const parsed = new URL(u);
      parsed.searchParams.delete("utm_source");
      parsed.searchParams.delete("utm_medium");
      parsed.searchParams.delete("utm_campaign");
      parsed.searchParams.delete("utm_content");
      parsed.searchParams.delete("fbclid");
      return parsed.toString();
    } catch(e) {
      return u;
    }
  }

  function downloadCSV() {
    if (results.length === 0) return alert("수집된 데이터가 아직 없습니다.");
    const headers = ["username", "url", "display_name", "Website", "Bio", "All_Links", "분류", "사유", "수집상태"];
    const lines = [headers.join(",")];

    for (const r of results) {
      const row = [
        `"${(r.username||"").replace(/"/g, '""')}"`,
        `"${(r.url||"").replace(/"/g, '""')}"`,
        `"${(r.display_name||"").replace(/"/g, '""')}"`,
        `"${(r.website||"").replace(/"/g, '""')}"`,
        `"${(r.bio||"").replace(/"/g, '""')}"`,
        `"${(r.all_links||"").replace(/"/g, '""')}"`,
        `"${(r.분류||"").replace(/"/g, '""')}"`,
        `"${(r.사유||"").replace(/"/g, '""')}"`,
        `"${(r.status||"").replace(/"/g, '""')}"`
      ];
      lines.push(row.join(","));
    }

    const blob = new Blob(["\\ufeff" + lines.join("\\n")], { type: "text/csv;charset=utf-8;" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `no-evidence-with-website-${new Date().toISOString().slice(0,10)}.csv`;
    a.click();
  }

  async function sleep(ms) {
    return new Promise(r => setTimeout(r, ms));
  }

  async function runLoop() {
    while (currentIndex < ACCOUNTS.length && !isPaused) {
      const acc = ACCOUNTS[currentIndex];
      const percent = ((currentIndex / ACCOUNTS.length) * 100).toFixed(1);
      progEl.innerText = `${currentIndex + 1} / ${ACCOUNTS.length} (${percent}%)`;
      currEl.innerText = `@${acc.username} 이동 중...`;
      barEl.style.width = `${percent}%`;

      // 1. 화면 이동
      const navA = document.createElement("a");
      navA.href = `/${acc.username}/`;
      document.body.appendChild(navA);
      navA.click();
      navA.remove();

      // 페이지 로드 대기 (2.0 ~ 2.6초)
      await sleep(2000 + Math.random() * 600);

      // 2. 데이터 추출
      const res = {
        username: acc.username,
        url: acc.url,
        display_name: acc.display_name,
        website: "",
        bio: "",
        all_links: "",
        분류: acc.분류,
        사유: acc.사유,
        status: "ok"
      };

      const header = document.querySelector("header");
      if (!header) {
        if (document.body.innerText.includes("페이지를 사용할 수 없습니다") || document.body.innerText.includes("Page Not Found")) {
          res.status = "not_found";
        } else {
          res.status = "no_header";
        }
      } else {
        const headerText = header.innerText || "";
        const lines = headerText.split("\\n").map(l => l.trim()).filter(Boolean);

        // 표시 이름 갱신
        const nameEl = header.querySelector("h1, h2");
        if (nameEl && !res.display_name) res.display_name = nameEl.innerText.trim();

        let extractedLinks = [];

        // 링크 모달 버튼 확인
        const linkBtn = Array.from(header.querySelectorAll("button, div[role='button']"))
          .find(el => el.innerText.includes("외 ") || el.innerText.includes("linktr") || el.innerText.includes(".com") || el.innerText.includes(".kr") || el.innerText.includes(".net") || el.innerText.includes(".org") || el.innerText.includes(".io"));

        if (linkBtn) {
          try {
            linkBtn.click();
            await sleep(500);
            const modal = document.querySelector("div[role='dialog']");
            if (modal) {
              const modalLinks = Array.from(modal.querySelectorAll("a"))
                .map(a => cleanUrl(a.href))
                .filter(u => u && !u.includes("instagram.com/"));
              extractedLinks.push(...modalLinks);

              const closeBtn = modal.querySelector("button");
              if (closeBtn) closeBtn.click();
              await sleep(300);
            }
          } catch(e) {
            console.error("모달 클릭 에러:", e);
          }
        }

        // 헤더 안의 일반 링크 확인
        const directLinks = Array.from(header.querySelectorAll("a"))
          .map(a => cleanUrl(a.href))
          .filter(u => u && !u.includes("instagram.com/") && u.startsWith("http"));
        extractedLinks.push(...directLinks);

        // 중복 제거
        extractedLinks = [...new Set(extractedLinks)];

        if (extractedLinks.length > 0) {
          res.website = extractedLinks[0];
          res.all_links = extractedLinks.join(" | ");
          countEl.innerText = results.filter(r => r.website).length + 1;
        }

        // Bio 텍스트
        const bioLines = lines.filter(l => !l.startsWith("게시물 ") && !l.startsWith("팔로워 ") && !l.startsWith("팔로우 ") && l !== "팔로우" && l !== "메시지 보내기" && l !== "더 보기" && !l.includes("님이 팔로우합니다"));
        res.bio = bioLines.join(" / ");
      }

      results.push(res);
      currentIndex++;

      if (currentIndex % 30 === 0) {
        console.log(`[중간 저장 가능] ${currentIndex}개 진행됨 (웹사이트 ${results.filter(r => r.website).length}개 발견)`);
      }

      // 계정 간 딜레이 (0.8초 ~ 1.4초)
      await sleep(800 + Math.random() * 600);
    }

    if (currentIndex >= ACCOUNTS.length) {
      progEl.innerText = "수집 완료!";
      currEl.innerText = `총 ${results.length}개 수집 완료! CSV 다운로드 중...`;
      barEl.style.width = "100%";
      barEl.style.background = "#10b981";
      downloadCSV();
    }
  }

  // 실행 시작
  runLoop();
})();
"""

out_file = os.path.join(D, "auto_collector.js")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(js_code)

print("SUCCESS: auto_collector.js created! Size:", len(js_code))
