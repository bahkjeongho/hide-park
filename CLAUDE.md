# Hide Park 사이트 (Quartz v5)

## 목적
옵시디언 위키(Hide Park)를 GitHub Pages로 공개하는 사이트. 친구에게 공유하고, 장기적으로 개인 미디어 채널로 키운다.
주소: https://bahkjeongho.github.io/hide-park/ (레포 이름은 소문자 hide-park, 경로는 대소문자 구분)

## 구조와 배포
- content/ 는 update.sh가 실행할 때마다 볼트에서 통째로 새로 복사한다. content/를 직접 수정하지 않는다. 노트 수정은 볼트에서 한다.
- 볼트 경로: /Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park (사이트 작업 중에는 읽기만 하고, 수정은 사용자에게 먼저 확인)
- update.sh: 볼트 복사 → 0. Clipping, 00. Template 제외 → 콜아웃 [! → [! 교정 → clean-frontmatter.mjs(빈 속성 제거) → make-labels.mjs(random-labels.json 생성) → commit → push (브랜치 v5)
- push 하면 GitHub Actions가 빌드해 Pages에 배포한다 (1~3분)
- 설정: quartz.config.yaml (폰트 Geist / Geist Mono, note-properties, random-notes 플러그인 등)

## 직접 만든 플러그인
- random-notes: ~/Documents/random-notes (GitHub bahkjeongho/quartz-random-notes). 홈에 노트 15개 무작위(Wiki 70%, Music·Architecture 30%) 표시.
- 수정 후 반영: 플러그인 레포 build + push → 이 레포에서 `npx quartz plugin remove quartz-random-notes` 후 `npx quartz plugin add github:bahkjeongho/quartz-random-notes` (update 명령 없음)
- Wiki 노트의 세부 라벨은 frontmatter topic의 첫 값. 없으면 "Wiki".

## 규칙
- 공개 레포다. 토큰, 비밀번호, 개인정보, 클립핑 원문을 커밋하지 않는다.
- 디자인 작업은 quartz/styles/custom.scss에 CSS를 넣고 `npx quartz build --serve`(localhost:8080)로 미리 본다.
- macOS: sed는 BSD(-i ''), 긴 한글 파일명에서 rsync 문제가 있어 cp -R 사용.

## 작업 방식
- 한국어, 차분하고 간결하게. 가장 작은 단위부터 한 단계씩, 구체적인 다음 행동 중심.
- 사용자는 터미널과 Git에 익숙하지 않다. 명령은 무엇을 하는지와 기대 결과를 함께 설명한다.

## 남은 과제
- 홈 디자인 다듬기 (색인표형 목록, 홈에서 오른쪽 사이드바 숨김)
- 히스토리 사이드바, 태그 시스템(보류), Pretendard(보류)
- 볼트 오타 [!summray] 1건

## 디자인
- 디자인 명세는 DESIGN.md, 시안 캡처는 docs/design/ 에 있다. 디자인 작업 전에 읽는다.
