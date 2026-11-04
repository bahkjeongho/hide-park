import json
import os
import csv

D = "/Users/parkjeongho/Developer/Hide-Park/docs/ig-run"
accounts = []
with open(os.path.join(D, "private-accounts-park.csv"), "r", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        accounts.append({
            "username": r["username"].strip(),
            "url": r["url"].strip(),
            "display_name": r.get("display_name", "").strip(),
            "분류": r.get("분류", "").strip(),
            "사유": r.get("사유", "").strip()
        })

accounts_json = json.dumps(accounts, ensure_ascii=False)

js_code = """// ==UserScript==
// @name         Instagram Private Accounts - Bio & Job Collector
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  private-accounts-park.csv 대상: Bio, 직업/카테고리, 웹사이트 링크 자동 수집
// @match        *://*.instagram.com/*
// @match        *://instagram.com/*
// @run-at       document-idle
// @grant        none
// ==/UserScript==

(async function () {
    'use strict';

    if (window.hasRunPrivateCollector) return;
    window.hasRunPrivateCollector = true;

    const sleep = (ms) => new Promise(r => setTimeout(r, ms));

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

    // 직업/역할 관련 주요 키워드 탐색 헬퍼
    const JOB_KEYWORDS = [
        "디자이너", "디렉터", "아티스트", "작가", "포토그래퍼", "사진가", "건축", "일러스트", 
        "큐레이터", "에디터", "기획", "공예", "도예", "회화", "조각", "뮤지션", "음악", "프로듀서",
        "designer", "director", "artist", "photographer", "architect", "illustrator", 
        "curator", "editor", "founder", "writer", "producer", "filmmaker", "stylist", 
        "ceramic", "studio", "craft", "researcher", "graphic", "visual"
    ];

    function extractJobFromBio(bioLines, category) {
        if (category && category !== "없음") return category;
        for (const line of bioLines) {
            const lower = line.toLowerCase();
            for (const kw of JOB_KEYWORDS) {
                if (lower.includes(kw)) {
                    return line; // 해당 직업 언급 줄 반환
                }
            }
        }
        return "";
    }

    // 상태 저장 키 분리 (이전 수집기와 충돌 방지)
    const STATE_KEY = "IG_PRIVATE_COLLECTOR_STATE_V1";
    let state = JSON.parse(localStorage.getItem(STATE_KEY) || "null");

    if (!state) {
        const ACCOUNTS = """ + accounts_json + """;
        state = {
            isRunning: false,
            currentIndex: 0,
            accounts: ACCOUNTS,
            results: []
        };
        localStorage.setItem(STATE_KEY, JSON.stringify(state));
    }

    function saveState() {
        localStorage.setItem(STATE_KEY, JSON.stringify(state));
    }

    function downloadCSV() {
        if (!state.results || state.results.length === 0) return alert("수집된 데이터가 없습니다.");
        const headers = ["username", "url", "display_name", "Category", "Job_Role", "Website", "Bio", "All_Links", "Is_Private", "분류", "사유", "수집상태"];
        const lines = [headers.join(",")];

        for (const r of state.results) {
            const row = [
                `"${(r.username||"").replace(/"/g, '""')}"`,
                `"${(r.url||"").replace(/"/g, '""')}"`,
                `"${(r.display_name||"").replace(/"/g, '""')}"`,
                `"${(r.category||"").replace(/"/g, '""')}"`,
                `"${(r.job_role||"").replace(/"/g, '""')}"`,
                `"${(r.website||"").replace(/"/g, '""')}"`,
                `"${(r.bio||"").replace(/"/g, '""')}"`,
                `"${(r.all_links||"").replace(/"/g, '""')}"`,
                `"${(r.is_private ? "Y" : "N")}"`,
                `"${(r.분류||"").replace(/"/g, '""')}"`,
                `"${(r.사유||"").replace(/"/g, '""')}"`,
                `"${(r.status||"").replace(/"/g, '""')}"`
            ];
            lines.push(row.join(","));
        }

        const blob = new Blob(["\\ufeff" + lines.join("\\n")], { type: "text/csv;charset=utf-8;" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = `private-accounts-with-jobs-${new Date().toISOString().slice(0,10)}.csv`;
        a.click();
    }

    // UI 생성
    const oldUI = document.getElementById("ig-collector-panel");
    if (oldUI) oldUI.remove();

    const ui = document.createElement("div");
    ui.id = "ig-collector-panel";
    ui.style.cssText = "position:fixed; top:20px; right:20px; z-index:9999999; background:rgba(18,24,38,0.96); color:#fff; padding:16px 20px; border-radius:12px; box-shadow:0 8px 32px rgba(0,0,0,0.6); font-family:system-ui, -apple-system, sans-serif; font-size:13px; width:340px; border:1px solid #3b82f6;";
    
    const percent = ((state.currentIndex / state.accounts.length) * 100).toFixed(1);
    const foundJobs = state.results.filter(r => r.category || r.job_role).length;
    const foundWebsites = state.results.filter(r => r.website).length;

    ui.innerHTML = `
      <div style="font-weight:bold; font-size:15px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
        <span style="color:#60a5fa;">👤 개인계정 직업/Bio 수집기</span>
        <span id="ig-prog" style="color:#93c5fd; font-size:13px;">${state.currentIndex} / ${state.accounts.length} (${percent}%)</span>
      </div>
      <div id="ig-curr" style="color:#cbd5e1; font-size:12px; margin-bottom:10px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
        ${state.isRunning ? `@${state.accounts[state.currentIndex]?.username || ""} 처리 중...` : "일시정지 상태"}
      </div>
      <div style="background:#1e293b; height:7px; border-radius:4px; margin-bottom:14px; overflow:hidden;">
        <div id="ig-bar" style="background:#3b82f6; height:100%; width:${percent}%;"></div>
      </div>
      <div style="display:flex; justify-content:space-between; margin-bottom:12px; font-size:12px; color:#94a3b8;">
        <span>직업 발견: <b id="ig-job-count" style="color:#38bdf8;">${foundJobs}</b>개</span>
        <span>웹사이트: <b id="ig-web-count" style="color:#34d399;">${foundWebsites}</b>개</span>
      </div>
      <div style="display:flex; gap:8px;">
        <button id="ig-toggle-btn" style="flex:1; background:${state.isRunning ? '#ef4444' : '#2563eb'}; color:#fff; border:none; padding:8px 10px; border-radius:6px; cursor:pointer; font-weight:bold; font-size:12px;">
          ${state.isRunning ? '⏸ 일시정지' : '▶ 수집 시작'}
        </button>
        <button id="ig-dl-btn" style="flex:1.2; background:#334155; color:#fff; border:none; padding:8px 10px; border-radius:6px; cursor:pointer; font-weight:bold; font-size:12px;">
          CSV 다운로드
        </button>
        <button id="ig-reset-btn" style="background:#475569; color:#fff; border:none; padding:8px; border-radius:6px; cursor:pointer; font-size:11px;" title="처음부터 다시">
          초기화
        </button>
      </div>
    `;
    document.body.appendChild(ui);

    const toggleBtn = document.getElementById("ig-toggle-btn");
    const dlBtn = document.getElementById("ig-dl-btn");
    const resetBtn = document.getElementById("ig-reset-btn");

    toggleBtn.onclick = () => {
        state.isRunning = !state.isRunning;
        saveState();
        if (state.isRunning) {
            const curr = state.accounts[state.currentIndex];
            if (curr && window.location.pathname !== `/${curr.username}/`) {
                window.location.href = `https://www.instagram.com/${curr.username}/`;
            } else {
                processCurrentPage();
            }
        } else {
            toggleBtn.innerText = "▶ 수집 재개";
            toggleBtn.style.background = "#2563eb";
            document.getElementById("ig-curr").innerText = "일시정지됨";
        }
    };

    dlBtn.onclick = () => downloadCSV();

    resetBtn.onclick = () => {
        if (confirm("정말 처음부터 다시 시작하시겠습니까?")) {
            localStorage.removeItem(STATE_KEY);
            window.location.reload();
        }
    };

    async function processCurrentPage() {
        if (!state.isRunning) return;
        if (state.currentIndex >= state.accounts.length) {
            alert("🎉 295개 계정의 직업 & Bio 수집이 완료되었습니다! CSV를 다운로드합니다.");
            downloadCSV();
            state.isRunning = false;
            saveState();
            return;
        }

        const currAcc = state.accounts[state.currentIndex];
        const targetPath = `/${currAcc.username}/`;

        if (window.location.pathname.toLowerCase() !== targetPath.toLowerCase()) {
            window.location.href = `https://www.instagram.com/${currAcc.username}/`;
            return;
        }

        await sleep(1500);

        const isPrivate = document.body.innerText.includes("비공개 계정입니다") || document.body.innerText.includes("This account is private");

        const res = {
            username: currAcc.username,
            url: currAcc.url,
            display_name: currAcc.display_name,
            category: "",
            job_role: "",
            website: "",
            bio: "",
            all_links: "",
            is_private: isPrivate,
            분류: currAcc.분류,
            사유: currAcc.사유,
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

            const nameEl = header.querySelector("h1, h2");
            if (nameEl && !res.display_name) res.display_name = nameEl.innerText.trim();

            // 1. 카테고리 태그 탐색 (팔로우 수치 다음 줄 등에 위치하는 공식 프로페셔널 카테고리)
            for (let i = 0; i < lines.length; i++) {
                if (lines[i].startsWith("팔로우 ") || lines[i].startsWith("팔로워 ")) {
                    // 팔로우 관련 줄 이후 바로 나오는 짧은 텍스트 확인
                    if (i + 1 < lines.length) {
                        const candidate = lines[i + 1];
                        if (candidate !== "팔로우" && candidate !== "메시지 보내기" && candidate !== "더 보기" && !candidate.includes("님이 팔로우합니다") && candidate.length <= 25) {
                            res.category = candidate;
                            break;
                        }
                    }
                }
            }

            // 2. 외부 링크 수집
            let extractedLinks = [];
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
                } catch(e) {}
            }

            const directLinks = Array.from(header.querySelectorAll("a"))
                .map(a => cleanUrl(a.href))
                .filter(u => u && !u.includes("instagram.com/") && u.startsWith("http"));
            extractedLinks.push(...directLinks);

            extractedLinks = [...new Set(extractedLinks)];
            if (extractedLinks.length > 0) {
                res.website = extractedLinks[0];
                res.all_links = extractedLinks.join(" | ");
            }

            // 3. Bio 텍스트 정제
            const bioLines = lines.filter(l => !l.startsWith("게시물 ") && !l.startsWith("팔로워 ") && !l.startsWith("팔로우 ") && l !== "팔로우" && l !== "메시지 보내기" && l !== "더 보기" && !l.includes("님이 팔로우합니다") && l !== res.category);
            res.bio = bioLines.join(" / ");

            // 4. 직업/역할 정제 추출 (카테고리가 없더라도 Bio 문맥에서 직업 줄을 캐치)
            res.job_role = extractJobFromBio(bioLines, res.category);
        }

        state.results.push(res);
        state.currentIndex++;
        saveState();

        await sleep(1000);
        if (state.currentIndex < state.accounts.length && state.isRunning) {
            const nextAcc = state.accounts[state.currentIndex];
            window.location.href = `https://www.instagram.com/${nextAcc.username}/`;
        } else if (state.currentIndex >= state.accounts.length) {
            alert("🎉 모든 계정의 직업 & Bio 수집이 완료되었습니다! CSV를 다운로드합니다.");
            downloadCSV();
            state.isRunning = false;
            saveState();
        }
    }

    if (state.isRunning) {
        processCurrentPage();
    }
})();
"""

out_path = os.path.join(D, "ig_tampermonkey_private.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print("SUCCESS: ig_tampermonkey_private.js created! Size:", len(js_code))
