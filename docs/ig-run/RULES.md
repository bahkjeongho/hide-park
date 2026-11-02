# 인스타그램 계정 → 위키 노트 작업 규칙

"RULES.md를 읽고 이어서 해줘"라고 하면 이 문서대로 진행한다. 사용자가 "계속"이라고 하면 다음 100개를 처리한다.

## 1. 경로
- 입력: `docs/instagram-following-remaining-names.csv` (열: no, username, url, display_name, name_status, archived, note), 총 2,210개
- 대기열: `docs/ig-run/queue.json` = 위 CSV에서 (a) 볼트에 이미 IG 값이 있는 계정, (b) 파일럿 30개(`docs/ig-pilot2/report.csv`)를 뺀 1,893개. CSV 순서 그대로
- 볼트: `/Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park` — 처리 중에는 **읽기 전용**. 쓰기는 사용자가 "적용"이라고 할 때만(아래 7번)
- 출력은 `docs/ig-run/` 안에서만: `notes/`(생성 노트), `progress.csv`, `manual-todo.csv`, `summary.md`, `topics.md`(볼트 topic 목록), `vault_names.json`(볼트 노트 이름, 충돌 확인용), `rec.py`(기록·노트 생성 도우미)
- 인스타그램 페이지에는 접속하지 않는다. 웹 검색과 공개 웹 페이지만 쓴다. 403/429/Cloudflare 차단은 우회하지 않고 no_evidence로 두고 사유를 적는다(정직한 User-Agent만 사용)

## 2. 검색 없이 처리하는 대상
- `__deleted__`로 시작하는 아이디 → private_or_unsure
- display_name이 한글만 2~5자 → private_or_unsure (개인 계정 추정)
- 특수문자·이모지뿐인 이름 등 식별이 불가능한 경우도 private_or_unsure(검색 생략 가능)
- 볼트에 같은 이름의 노트가 이미 있으면(`vault_names.json` 대조) 노트를 만들지 않고 conflict로 기록

## 3. 웹 접근 한도 (계정당 최대 2회)
- 검색 1회: 쿼리는 `"display_name 아이디"` (이름이 비어 있으면 아이디만). 변형·재검색·추가 검색 금지
- 열람 1회(필요할 때만): 검색 결과에서 식별된 대상의 공식 사이트 또는 위키 페이지 1개, 또는 Wikidata 조회 1회
- 근거가 안 보이면 즉시 no_evidence로 기록하고 다음 계정으로 넘어간다
- 검색은 한 번에 약 12개까지만 병렬로 실행한다(초과하면 too_many_requests)

## 4. 증거 규칙 (엄격)
인정하는 경우:
1. 열람한 공식 사이트 HTML이 `instagram.com/아이디`를 **정확히 같은 아이디로** 링크
2. 검색 결과나 페이지에 그 아이디가 그대로 적혀 있고 대상과 직접 연결됨(기사·소속 기관 페이지가 해당 계정을 링크)
3. 위키피디아 또는 Wikidata P2003(Instagram 사용자 이름) 또는 위키피디아 외부 링크가 CSV의 아이디와 **정확히 같음**

인정하지 않는 경우:
- 이름만 같거나 비슷함, 유명인과 같은 이름(예: 이름이 같은 방송인의 다른 아이디는 오탐)
- 공식 사이트가 링크하는 아이디가 다른 아이디(예: bbc ≠ bbcglobal)
- 출처 페이지를 확인할 수 없는 요약 문장
- 근거가 약하면 no_evidence

## 5. 분류
- **found**: 근거가 있고 topic을 볼트의 기존 topic(`topics.md`) 중에서 정할 수 있음 → 노트 생성. 새 topic은 만들지 않는다
- **needs_topic**: 식별됐지만 기존 topic에 맞는 것이 없음 → 노트 만들지 않음, 후보 topic을 기록
- **conflict**: 같은 이름의 노트가 볼트에 이미 있음 → 만들지 않음. IG만 채우는 후보로 기록
- **no_evidence**: 근거를 찾지 못함
- **private_or_unsure**: 개인 계정으로 보이거나 위키 대상(창작자·브랜드·기관·공인) 여부가 불확실함

## 6. 노트 형식 (found만)
- 파일명: 영어 기본, 한국 창작자·기관은 한글. 반대 표기는 aliases에 넣는다
- 속성 순서: aliases, topic, IG, Website, URL, Wikis, Cities, Countries, tags, Related. 스포츠팀은 기존 스포츠 팀 형식, **Music Artist는 기존 아티스트 형식**(Genre, Labels, Member of 추가; 본문은 Summary + People + Discography만, tl;dr·Info 없음)
- IG는 `https://www.instagram.com/아이디/` 형식. Website는 확인된 것만. tags·Related는 비운다. 확인되지 않은 속성은 비운다
- 본문: tl;dr(영어), Info(한국어 번역을 위에, 영어 원문을 아래; 원문을 읽지 못했으면 비움), Summary(위키 정보 상자가 있을 때만 표), `# Portfolio`, `# People`
- 고유명사 `[[ ]]` 허용. 값은 영어(도시·국가는 볼트 표기: USA, UK, South Korea 등)
- **노트 본문에 출처 줄과 "(확인필요)"를 넣지 않는다. 출처 URL은 CSV(`progress.csv`의 증거 URL 열)에만 적는다**
- 확인되지 않은 정보는 쓰지 않는다(추측 금지)

## 7. 기록과 이어하기
- `progress.csv`: 계정마다 1행 (username, 분류, topic, 증거 URL, 노트 경로, 웹 접근 횟수). 계정을 처리할 때마다 기록한다
- 시작할 때 `progress.csv`가 있으면 거기 있는 계정은 건너뛴다(`rec.py`의 `done()`). 다음 대상 = 대기열에서 아직 progress에 없는 계정을 순서대로 100개
- `manual-todo.csv`: found 외 모든 계정을 한 번에 모은다. 열: username, url, display_name, 분류, 사유, 후보 topic(needs_topic만), archived, note. 처리 중에도 계속 갱신
- 파일럿 30개는 다시 검색하지 않고 결과를 가져온 상태다(found 노트는 notes/에 복사됨, 나머지는 manual-todo)
- 사용자가 "적용"이라고 하면 `notes/`의 노트를 볼트 `2. Wiki/`에 복사한다. 같은 이름의 파일이 있으면 덮어쓰지 않고 건너뛴다

## 8. 100개 단위와 요약
- 한 회차에 100개를 처리하고 멈춘다. 사용자가 "계속"이라고 하면 이어서 다음 100개
- 100개마다 `summary.md`를 갱신한다: 처리 개수, 분류별 개수, 계정당 평균 웹 접근, 새 규칙으로 인정된 개수, 규칙 위반이 있었다면 그 내용
- 사용량 한도나 오류로 중단되면 `progress.csv`를 갱신한 뒤 멈춘다

## 9. 현재 상태 (2026-11-03 기준)
- 처리한 신규 계정: **237개** + 파일럿 30개 = progress.csv 267행
- 분류(신규 237개): no_evidence 169, found 35, private_or_unsure 23, conflict 9, needs_topic 1
- 생성 노트: `docs/ig-run/notes/` (파일럿 포함), 볼트 `2. Wiki/`에 적용 완료
- **다음 시작 위치: 대기열 228번째 (인덱스 227), 첫 계정 = `yinyang.fig` (원본 CSV no 289)**. 대기열 총 1893개 중 남은 것은 1666개
- 3회차는 웹 검색 한도 소진으로 중간에 멈춤. 한도 안내: 세션당 WebSearch 200회(약 시간당 100회 회복, `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`으로 조정). 한도에 걸리면 우회하지 말고 기록 후 멈춘다. 새 세션에서는 batch 처리 전에 `batch4.json`이 아닌 `queue.json`과 `progress.csv`로 다음 대상을 다시 계산한다
