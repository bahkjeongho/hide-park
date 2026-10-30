# Hide Park 디자인 명세 v1

시안(흰 배경, 모노톤)을 Quartz 사이트에 적용하기 위한 명세. 이 문서와 `docs/design/`의 시안 캡처가 다르면 **캡처가 우선**이다.

## 원칙
- 흰 배경, 검정 + 회색 위계, 얇은 구분선. 색 강조 없음.
- 애니메이션과 transition 없음. 호버는 색 변화만.
- 작은 글자, 큰 여백. 이미지가 없어도 성립하는 구조(글자와 구조 중심).
- 홈에는 소개 글, 링크 설명 없음. 워드마크 + 카테고리 메뉴 + 무작위 목록만.

## 토큰

| 이름 | 라이트 | 다크(제안, 시안 없음) |
|---|---|---|
| bg | `#ffffff` | `#111111` |
| text | `#111111` | `#f2f2f2` |
| muted | `#6b6b6b` | `#9a9a9a` |
| hairline | `#e6e6e6` | `#2a2a2a` |
| dim (호버 시 나머지 행, 큰 글자 전용) | `#8c8c8c` | `#6f6f6f` |

서체: 본문과 제목 **Geist**, 메타와 코드 **Geist Mono**. `quartz.config.yaml`의 `typography.body`를 Geist Mono → **Geist**로 변경(긴 글에 불리하고 한글은 대체 서체로 표시됨). 한글 대체 서체는 `'Apple SD Gothic Neo', system-ui`.

| 용도 | 서체 | 크기 / 행간 | 굵기 | 자간 |
|---|---|---|---|---|
| 워드마크 (홈, 카테고리 페이지) | Geist | 96px / 0.9 (모바일 44px) | 500 | -0.05em |
| 카테고리 메뉴 | Geist | 22px / 1.25 | 400 | -0.02em |
| 목록 제목 | Geist | 24px / 1.2 (모바일 19px) | 400 | -0.01em |
| 메타 라벨 | Geist Mono | 11px (모바일 10px), 대문자 | 400 | 0.06em |
| 노트 제목 | Geist | 72px / 1 | 300 | -0.04em |
| 소제목 (h2) | Geist | 22px | 500 | -0.02em |
| 본문 | Geist | 16px / 1.75 | 400 | 0 |
| 본문 영어 블록 | Geist | 15px / 1.75, muted | 400 | 0 |
| 사이드바 | Geist | 13px / 1.3 | 400 (현재 항목 500) | 0 |

간격: 페이지 패딩 `28px 32px` (모바일 20px), 열 간격 `32px 48px`, 목록 행 패딩 `15px 0` (모바일 11px), 구분선 1px.

## 레이아웃

**홈, Wiki, Thoughts, About (2분할)**
- 왼쪽 `flex: 1 1 340px` (대략 1/3): 워드마크 → 카테고리 메뉴(세로) → 맨 아래 `Search`, `Dark` 텍스트 링크(모노 11px).
- 오른쪽 `flex: 2 1 560px` (대략 2/3): 내용.
- 약 900px 이하에서 세로로 쌓임(`flex-wrap`).
- 카테고리 메뉴: `Wiki / Thoughts / About`. 현재 위치만 text, 나머지 muted, 호버 시 text. **홈에서는 아무것도 선택되지 않음.**

**노트 페이지 (3분할)**
- 왼쪽 240px: 작은 워드마크(22px), 카테고리 메뉴(가로, 14px), 검색, 탐색기.
- 가운데 최대 1080px(2026-10-31에 700px에서 변경, 노트 맨 위 웹사이트 임베드 때문), 가운데 정렬: 경로(모노 11px) → 제목 → 속성 표 → 본문.
- 오른쪽 220px: 목차(On this page), 백링크. 그래프는 시안에 없음(제거하거나 접어서 둠, 결정 필요).

## 컴포넌트

**목록 행 (홈, Wiki)**: `display: grid; grid-template-columns: 200px 1fr`, 왼쪽 메타 라벨(muted), 오른쪽 제목. 행 위에 1px hairline, 마지막 행 아래에도 1px. 링크 밑줄 없음. 목록에 마우스를 올리면 모든 제목이 dim, 올린 행만 text(라벨도 text). transition 없음.

**Thoughts 목록**: 열 `140px 1fr 120px` = Date(모노) / Title / Type(Essay, Critique). 호버 규칙은 위와 동일.

**Wiki 목록 페이지**: 맨 위에 버튼 3개(`Topic +`, `Region +`, `Sort: A–Z`, 모노 11px muted, 테두리 없음). 헤더 `Topic | Notes (N)` (N은 실제 Wiki 노트 수). 행은 위 목록 행과 같음, 기본 정렬 A–Z.

**속성 표 (노트 페이지)**: 속성을 모노 11px 대문자 행으로 표시. 열 `140px 1fr`, 키는 muted, 값은 text, 값이 링크면 밑줄(1px, offset 3px), 각 행 아래 hairline, 맨 위에도 hairline. 표시할 속성은 `note-properties`의 `includedProperties`를 따른다.

**Members 목록**: 열 `200px 1fr`, 왼쪽 직함(muted, 영어 원어), 오른쪽 이름 링크.

**본문 링크**: 밑줄 1px, offset 3px. 그 외 UI 링크는 밑줄 없음.

**제외**: 플로팅 하단 바, 모달 상세, 큰 이미지 그리드, 둥근 박스 카드, 애니메이션. 링크 호버 미리보기는 Quartz 기본 팝오버를 유지하되 같은 토큰으로 맞춤.

## 홈 무작위 목록: 비율과 계산

설정: `total 15`, `wikiRatio 0.6`, `thoughtsRatio 0.2`, 나머지는 Object, `musicShare 0.5` (Object 안에서 음악:건축 = 1:1).

계산식 (JS `Math.round`, 0.5는 올림):
- wikiN = round(total × 0.6)
- thoughtsN = round(total × 0.2)
- objectN = total − wikiN − thoughtsN
- musicN = round(objectN × musicShare)
- architectureN = objectN − musicN

| 총 개수 | Wiki | Thoughts | Object | 음악 | 건축 |
|---|---|---|---|---|---|
| 15 (데스크톱) | 9 | 3 | 3 | 2 | 1 |
| 10 (모바일 시안) | 6 | 2 | 2 | 1 | 1 |

분류 규칙(Quartz slug 기준, 소문자와 `-`):
- `1-thoughts/…` → thoughts
- `2-wiki/…` → wiki
- `3-object/31-music/…` → music
- `3-object/32-architecture/…` → architecture
- 그 외(예: `3-object/34-film/`), `index`, `*/index`, `tags/…`, `.md`가 아닌 파일은 제외.

부족분 처리: 한 분야의 노트가 모자라면 남은 노트(다른 분야)로 채워 총 개수를 유지한다(현재 코드 그대로). **Thoughts 폴더는 처음에 비어 있으므로 이 규칙이 실제로 작동한다.**

라벨: Wiki는 `random-labels.json`의 topic 값(없으면 `Wiki`), Thoughts는 `Thoughts`, 음악은 `Music`, 건축은 `Architecture`. 나중에 Thoughts는 `type` 속성(Essay, Critique)으로 바꿀 수 있음.

구현 위치: `~/Developer/random-notes` 플러그인
- `Category`에 `"thoughts"` 추가, `LABELS`에 `thoughts: "Thoughts"`.
- `RandomNotesOptions`에 `thoughtsRatio?: number` (기본 0.2), `wikiRatio` 기본을 0.6으로.
- `RandomNotes.tsx`의 `data-*`와 `random-notes.inline.ts`의 읽기 로직에 `thoughtsRatio` 추가.
- `pickNotes`의 계산을 위 식으로 변경, `test/pick.test.ts`에 thoughts 케이스(비율 9/3/2/1, Thoughts가 비었을 때 채움) 추가.
- 반영: build → push → 사이트에서 `quartz plugin remove quartz-random-notes` 후 `add github:bahkjeongho/quartz-random-notes`.

## 페이지와 주소

| 메뉴 | 주소 | 비고 |
|---|---|---|
| 홈 | `/` | 볼트 루트의 본문 없는 `index.md` (title: Hide Park) |
| Wiki | `/2-wiki/` | Quartz folder-page를 위 목록 스타일로 |
| Thoughts | `/1-thoughts/` | 볼트에 `1. Thoughts` 폴더가 생김 |
| About | `/about` | 볼트 루트에 `About.md`를 만들지, 사이트 전용 페이지로 할지 결정 필요 |

폴더 번호가 주소에 들어간다(`1-thoughts`). 볼트의 폴더 이름은 `1. Thoughts`처럼 온점을 유지하고, `update.sh`가 `rename-folders.mjs`로 content/ 복사본의 온점만 뺀다(`1 Thoughts` → `/1-thoughts`). 이름을 바꾸면 이미 공유한 주소가 깨진다. 아직 공유 전이라 2026-10-24에 온점 없는 주소로 확정함.

## 작업 순서 (각 단계마다 localhost:8080에서 확인한 뒤 다음으로)
1. 토큰, 서체, 타입 스케일을 `quartz/styles/custom.scss`와 `quartz.config.yaml`에 적용. 본문을 Geist로.
2. 노트 페이지: 3분할, 속성 표, 목차와 백링크.
3. 홈: 불필요한 요소 숨김, 워드마크 + 카테고리 메뉴 + 목록 (먼저 현재 `random-notes` 그대로).
4. `random-notes` 플러그인에 thoughts 분류와 새 비율 적용 (위 구현 위치).
5. Wiki와 Thoughts 폴더 페이지를 목록 스타일로.
6. About 페이지.
7. 모바일(390px) 확인, 다크 모드 값 확정.
8. `./update.sh`로 배포. 배포 전에 변경 내용을 사용자에게 보여 주고 승인을 받는다.

## 주의
- 볼트(iCloud)는 읽기만 한다. 수정이 필요하면 먼저 사용자에게 확인.
- 공개 레포다. 토큰, 비밀번호를 커밋하지 않는다.
- 레이아웃 수치는 시안 우선. 문자 간격과 크기를 임의로 바꾸지 않는다.
- 미결: 오른쪽의 그래프 처리, About의 구현 방식, 다크 모드 값.
