# ig-run 1회차 요약 (신규 100개 + 파일럿 30개 가져옴)
- 처리: 신규 100개 (대기열 1893개 중, 볼트에 이미 IG가 있는 계정과 파일럿 30개는 제외)
- 분류(신규): no_evidence 77, found 17, private_or_unsure 4, conflict 1, needs_topic 1
- 노트 생성: 신규 17개 + 파일럿 found 7개 중 7개(docs/ig-run/notes/, 총 24개 파일)
- 계정당 평균 웹 접근: 1.41회 (검색 1회 + 페이지 열람). 규칙(최대 2회)을 어긴 경우: indexshop.kr(4회)
- 걸린 시간: 약 8분(대화 시간 포함, 정확한 측정은 아님). 토큰 사용량은 확인할 수 없음
- 병목: 검색 결과 요약에 아이디가 거의 나오지 않아 공식 사이트를 열어야 확인됨. 검색은 한 번에 약 12개까지만 병렬로 가능(초과 시 too_many_requests)
- 전체 1893개 추정: 100개당 약 8분이면 약 2시간(여러 회차). found 비율 약 17% → 예상 노트 약 321개
- 사람이 정리할 목록: manual-todo.csv (found 외 전부, 파일럿 포함)

## 위키데이터 재확인 (신규 규칙: Wikidata P2003/위키 외부 링크가 아이디와 정확히 일치)
- 대상: 지난 100개 중 no_evidence인 유명 대상 14개를 1회씩 재확인(applenews, sacaiofficial, showstudio, rhizomedotorg, newinc, bbc, wsj, npr, guggenheim, balmain, gus_van_sant, tinashenow, ludovicdesaintsernin, objekteunserertage)
- 새로 인정: 5개 (bbc, wsj, npr, guggenheim, balmain). 그중 4개는 노트 생성, npr는 볼트에 NPR 노트가 있어 conflict
- 불인정: showstudio(Wikidata 값이 nick_knight로 아이디 불일치), newinc(newmuseum 불일치), 나머지는 Wikidata에 값 없음 또는 문서 없음

## 2회차 (신규 100개)
- 분류: no_evidence 74, found 11, private_or_unsure 8, conflict 7
- 계정당 평균 웹 접근 1.06회. 한글만 2~5자·삭제 계정은 검색 없이 private_or_unsure
- 새 규칙(Wikidata/위키 아이디 일치) 적용으로 인정된 계정: MIT Press, Ars Electronica (Wikidata만으로), Metahaven·Noema·Joey Valence & Brae(사이트 링크와 Wikidata 모두 일치). 이름만 같은 Lulu Kennedy는 Wikidata가 다른 사람(가수)이라 불인정
- 규칙 위반: 이름 충돌 확인 없이 `Joey Valence & Brae` 노트를 만들었다가 볼트에 같은 이름이 있어 conflict로 되돌림

## 3회차 (진행 중단: 웹 검색 한도 소진, 신규 37개 처리)
- 분류: no_evidence 23, private_or_unsure 11, found 3
- 중단 사유: 세션의 WebSearch 한도(200회, 시간당 약 100회씩 회복)를 모두 써서 100개를 채우지 못함. 우회하지 않고 progress.csv를 갱신한 뒤 멈춤
- 새 노트: Louisiana Channel, Jurgen Maelfeyt, A. G. Cook(Wikidata P2003 일치)
- 누적 신규 237개 처리, found 35
