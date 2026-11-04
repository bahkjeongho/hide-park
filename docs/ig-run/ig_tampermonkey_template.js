// ==UserScript==
// @name         Instagram Bio & Website Collector for Obsidian
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  892개 인스타그램 프로필에서 Bio와 실제 웹사이트 링크를 자동 수집하여 CSV로 다운로드
// @match        https://www.instagram.com/*
// @grant        none
// ==/UserScript==

(async function () {
    'use strict';

    // 중복 실행 방지
    if (window.hasRunCollector) return;
    window.hasRunCollector = true;

    // 대기 헬퍼
    const sleep = (ms) => new Promise(r => setTimeout(r, ms));

    // URL 정제 (추적 태그 제거)
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

    // 1. 상태 불러오기 (localStorage)
    const STATE_KEY = "IG_COLLECTOR_STATE_V1";
    let state = JSON.parse(localStorage.getItem(STATE_KEY) || "null");

    // 초기 상태 세팅
    if (!state) {
        // 계정 목록이 없으면 생성
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
        const headers = ["username", "url", "display_name", "Website", "Bio", "All_Links", "분류", "사유", "수집상태"];
        const lines = [headers.join(",")];

        for (const r of state.results) {
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

    // 2. 화면 우측 상단 플로팅 UI 생성
    const ui = document.createElement("div");
    ui.id = "ig-collector-panel";
    ui.style.cssText = "position:fixed; top:20px; right:20px; z-index:9999999; background:rgba(20,20,20,0.95); color:#fff; padding:16px 20px; border-radius:12px; box-shadow:0 8px 32px rgba(0,0,0,0.6); font-family:system-ui, -apple-system, sans-serif; font-size:13px; width:340px; border:1px solid #555;";
    
    const percent = ((state.currentIndex / state.accounts.length) * 100).toFixed(1);
    const foundWebsites = state.results.filter(r => r.website).length;

    ui.innerHTML = `
      <div style="font-weight:bold; font-size:15px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
        <span>📸 IG 위키 수집기</span>
        <span id="ig-prog" style="color:#c084fc; font-size:13px;">${state.currentIndex} / ${state.accounts.length} (${percent}%)</span>
      </div>
      <div id="ig-curr" style="color:#aaa; font-size:12px; margin-bottom:10px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
        ${state.isRunning ? `@${state.accounts[state.currentIndex]?.username || ""} 처리 중...` : "일시정지 상태"}
      </div>
      <div style="background:#333; height:7px; border-radius:4px; margin-bottom:14px; overflow:hidden;">
        <div id="ig-bar" style="background:#a855f7; height:100%; width:${percent}%;"></div>
      </div>
      <div style="display:flex; justify-content:space-between; margin-bottom:12px; font-size:12px; color:#bbb;">
        <span>발견된 웹사이트: <b id="ig-count" style="color:#34d399;">${foundWebsites}</b>개</span>
      </div>
      <div style="display:flex; gap:8px;">
        <button id="ig-toggle-btn" style="flex:1; background:${state.isRunning ? '#dc2626' : '#10b981'}; color:#fff; border:none; padding:8px 10px; border-radius:6px; cursor:pointer; font-weight:bold; font-size:12px;">
          ${state.isRunning ? '⏸ 일시정지' : '▶ 수집 시작'}
        </button>
        <button id="ig-dl-btn" style="flex:1.2; background:#374151; color:#fff; border:none; padding:8px 10px; border-radius:6px; cursor:pointer; font-weight:bold; font-size:12px;">
          CSV 다운로드
        </button>
        <button id="ig-reset-btn" style="background:#4b5563; color:#fff; border:none; padding:8px; border-radius:6px; cursor:pointer; font-size:11px;" title="처음부터 다시">
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
            // 현재 타겟 계정 페이지로 이동
            const curr = state.accounts[state.currentIndex];
            if (curr && window.location.pathname !== `/${curr.username}/`) {
                window.location.href = `https://www.instagram.com/${curr.username}/`;
            } else {
                processCurrentPage();
            }
        } else {
            toggleBtn.innerText = "▶ 수집 재개";
            toggleBtn.style.background = "#10b981";
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

    // 3. 현재 페이지 처리 함수
    async function processCurrentPage() {
        if (!state.isRunning) return;
        if (state.currentIndex >= state.accounts.length) {
            alert("🎉 모든 계정의 수집이 완료되었습니다! CSV를 다운로드합니다.");
            downloadCSV();
            state.isRunning = false;
            saveState();
            return;
        }

        const currAcc = state.accounts[state.currentIndex];
        const targetPath = `/${currAcc.username}/`;

        // 아직 해당 계정 페이지가 아니면 이동
        if (window.location.pathname.toLowerCase() !== targetPath.toLowerCase()) {
            window.location.href = `https://www.instagram.com/${currAcc.username}/`;
            return;
        }

        // 페이지 렌더링 대기 (1.5초)
        await sleep(1500);

        const res = {
            username: currAcc.username,
            url: currAcc.url,
            display_name: currAcc.display_name,
            website: "",
            bio: "",
            all_links: "",
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

            let extractedLinks = [];

            // 링크 모달 버튼 클릭 확인
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

            // 헤더의 일반 외부 링크도 수집
            const directLinks = Array.from(header.querySelectorAll("a"))
                .map(a => cleanUrl(a.href))
                .filter(u => u && !u.includes("instagram.com/") && u.startsWith("http"));
            extractedLinks.push(...directLinks);

            extractedLinks = [...new Set(extractedLinks)];

            if (extractedLinks.length > 0) {
                res.website = extractedLinks[0];
                res.all_links = extractedLinks.join(" | ");
            }

            const bioLines = lines.filter(l => !l.startsWith("게시물 ") && !l.startsWith("팔로워 ") && !l.startsWith("팔로우 ") && l !== "팔로우" && l !== "메시지 보내기" && l !== "더 보기" && !l.includes("님이 팔로우합니다"));
            res.bio = bioLines.join(" / ");
        }

        // 결과 저장 및 다음 계정 준비
        state.results.push(res);
        state.currentIndex++;
        saveState();

        // 1.0초 대기 후 다음 계정으로 이동
        await sleep(1000);
        if (state.currentIndex < state.accounts.length && state.isRunning) {
            const nextAcc = state.accounts[state.currentIndex];
            window.location.href = `https://www.instagram.com/${nextAcc.username}/`;
        } else if (state.currentIndex >= state.accounts.length) {
            alert("🎉 모든 계정의 수집이 완료되었습니다! CSV를 다운로드합니다.");
            downloadCSV();
            state.isRunning = false;
            saveState();
        }
    }

    // 만약 실행 중인 상태로 페이지가 로드되었다면 자동 진행
    if (state.isRunning) {
        processCurrentPage();
    }
})();
