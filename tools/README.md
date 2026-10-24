# tools — 화면 검증 스크립트

개발 서버(`npx quartz build --serve`, localhost:8080)나 배포 사이트를 **헤드리스 Chrome**으로 열어 실제로 어떻게 그려지는지 확인한다. 브라우저를 직접 열 수 없는 환경(Claude Code 등)에서 화면을 검증하려고 만들었다.

필요한 것: macOS의 Google Chrome(`/Applications/Google Chrome.app`), Node 22 이상(전역 `WebSocket`을 쓴다). 설치할 패키지는 없다.

| 스크립트 | 용도 | 예 |
|---|---|---|
| `shot.mjs` | 스크린샷. 기기 에뮬레이션이라 390 폭이 진짜 모바일 폭이다. `dark`를 주면 다크 모드, `full`을 주면 전체 높이. | `node tools/shot.mjs http://localhost:8080/ /tmp/home.png 390 844` |
| `fontprobe.mjs` | 요소별로 실제로 쓰인 글꼴 조회(웹폰트인지 시스템 폰트인지). | `node tools/fontprobe.mjs http://localhost:8080/ ".page-title a" ".random-notes__label"` |
| `evalprobe.mjs` | 페이지에서 JS 식을 실행해 결과를 출력(목록 개수, 링크, 필터 동작 등). Promise 가능. | `node tools/evalprobe.mjs http://localhost:8080/ 'document.querySelectorAll(".random-notes__item").length'` |
| `example-wiki-filter-test.js` | Wiki 필터를 버튼으로 눌러 보는 `evalprobe` 용 예제 식. | `node tools/evalprobe.mjs http://localhost:8080/2-wiki/ "$(cat tools/example-wiki-filter-test.js)"` |

## 알아 둘 것

- 페이지 로드 후 약 9초 기다렸다가 측정한다. 느린 페이지는 기다림이 모자랄 수 있다.
- 일반 헤드리스 창(`--window-size=390`)은 최소 폭이 더 넓어서 모바일 화면이 잘려 보인다. 모바일은 반드시 `shot.mjs`(기기 에뮬레이션)로 본다.
- 로컬 개발 서버는 주소의 대소문자를 구분하지 않지만 GitHub Pages는 구분한다. 배포 사이트 검증은 `https://bahkjeongho.github.io/hide-park/...`를 소문자 주소로 넣는다.
- `shot.mjs`에 `LS_SEED='{"키":"값"}'`을 앞에 붙이면 localStorage를 미리 채우고 찍는다(예: Recent 목록 확인용 방문 기록).
- 임시 프로필 폴더는 자동으로 만들고 끝나면 지운다. 직접 지정하려면 `PROF=/폴더` 를 앞에 붙인다.
