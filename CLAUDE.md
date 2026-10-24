# Hide Park 사이트 (Quartz v5)

## 목적
옵시디언 위키(Hide Park)를 GitHub Pages로 공개하는 사이트. 친구에게 공유하고, 장기적으로 개인 미디어 채널로 키운다.
주소: https://bahkjeongho.github.io/hide-park/ (레포 이름은 소문자 hide-park, 경로는 대소문자 구분)

## 구조와 배포
- content/ 는 update.sh가 실행할 때마다 볼트에서 통째로 새로 복사한다. content/를 직접 수정하지 않는다. 노트 수정은 볼트에서 한다.
- 볼트 경로: /Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park (사이트 작업 중에는 읽기만 하고, 수정은 사용자에게 먼저 확인)
- update.sh: 볼트 복사 → 0. Clipping Origin, 00. Template 제외 → 콜아웃 [! → [! 교정 → rename-folders.mjs(폴더 이름의 번호 뒤 온점 제거) → clean-frontmatter.mjs(빈 속성 제거) → make-labels.mjs(random-labels.json, wiki-meta.json 생성) → commit → push (브랜치 v5). `git add -A`로 전부 올리므로 실행 전에 git status로 낯선 파일이 없는지 본다.
- push 하면 GitHub Actions가 빌드해 Pages에 배포한다 (1~3분). 실행 기록은 https://api.github.com/repos/bahkjeongho/hide-park/actions/runs?branch=v5 로 확인한다 (gh 미설치).
- 설정: quartz.config.yaml (폰트는 `quartz-fonts` 플러그인 옵션에서 Geist / Geist Mono 지정, note-properties, 플러그인 3개 등)

## 주소 규칙
- 볼트 폴더 이름은 `2. Wiki`처럼 온점을 유지하고, 사이트에서는 rename-folders.mjs가 복사본의 이름을 `2 Wiki`로 바꿔 주소가 `/2-wiki/`가 된다. (온점이 있으면 폴더 페이지가 404가 났다.)
- 주요 주소: `/2-wiki/`, `/1-thoughts/`, `/4-about/about`. 폴더 이름을 바꾸면 주소가 바뀌고 random-notes 분류 규칙(slug 기준)과 folder-index의 `FOLDER_PAGES`도 같이 고쳐야 한다.
- **GitHub Pages는 주소의 대소문자를 구분한다.** slug는 항상 소문자(`4-about/about`)다. 로컬 `npx quartz build --serve`는 구분하지 않으니 메뉴 링크와 설정의 경로는 소문자로 쓴다.

## 직접 만든 플러그인 (모두 공개 GitHub 레포, 로컬 폴더는 ~/Developer 아래: random-notes, quartz-site-menu, quartz-folder-index)
| 플러그인 | 레포 | 역할 |
|---|---|---|
| random-notes | bahkjeongho/quartz-random-notes | 홈에 노트 15개 무작위. Wiki 60% / Thoughts 20% / 나머지 Object(음악:건축 1:1). 분야가 모자라면 다른 분야로 채운다. |
| site-menu | bahkjeongho/quartz-site-menu | 카테고리 메뉴(Wiki / Thoughts / About). 링크는 현재 페이지 기준 상대 경로, 현재 구역만 진하게. 항목은 quartz.config.yaml의 options.items. |
| folder-index | bahkjeongho/quartz-folder-index | Wiki와 Thoughts 폴더 페이지를 색인표로. Wiki는 Topic / Region 필터와 A–Z 정렬, Thoughts는 Date / Title / Type. |
- 수정 후 반영: 플러그인 로컬 폴더에서 `npm test`, `npm run build`(dist도 커밋) → commit, push → 이 레포에서 `npx quartz plugin remove <이름>` 후 `npx quartz plugin add github:bahkjeongho/<레포>` (update 명령 없음). add가 설정에 기본 옵션 항목을 하나 더 넣으니 중복을 지우고 옵션을 확인한다.
- **로컬 경로 플러그인(`./plugins/...`)은 쓰지 않는다.** 로컬 미리보기는 되지만 설치가 이 컴퓨터의 절대 경로를 써서 GitHub Actions 빌드가 실패한다. 반드시 GitHub 레포로 올려 설치한다.
- 플러그인 빌드의 `DTS Build error`(`@quartz-community/types`를 못 찾음)는 기존 오류이고 JS 결과에는 영향이 없다.
- 설정을 바꾸거나 플러그인 파일을 갈아 끼운 뒤에는 개발 서버를 껐다 켠다. 증분 재빌드가 `postscript.js`와 설정을 다시 만들지 않을 때가 있다.
- Wiki 노트의 세부 라벨은 frontmatter topic의 첫 값. 없으면 "Wiki". 필터용 데이터(topic 전체, 지역=Countries+Cities, Thoughts의 Date와 Type)는 make-labels.mjs가 wiki-meta.json으로 만든다.

## 규칙
- 공개 레포다. 토큰, 비밀번호, 개인정보, 클립핑 원문을 커밋하지 않는다.
- 디자인 작업은 quartz/styles/custom.scss에 CSS를 넣고 `npx quartz build --serve`(localhost:8080)로 미리 본다.
- macOS: sed는 BSD(-i ''), 긴 한글 파일명에서 rsync 문제가 있어 cp -R 사용.
- **레포와 플러그인 폴더는 iCloud 동기화 밖(~/Developer)에 둔다.** 이 레포는 `~/Developer/Hide-Park`다. 예전에 ~/Documents(iCloud 동기화 대상) 안에 있을 때 이름 끝에 ` 2`, ` 3`이 붙은 충돌 복사본(content/, public/, 플러그인 dist/)이 반복해서 생겼다(원인은 iCloud 충돌로 추정, 확정은 아님). ~/Documents나 ~/Desktop 아래로 다시 옮기지 않는다.
- 그래도 ` 2`, ` 3` 파일이 보이면 push 전에 `git status`로 걸러 내고, 플러그인 레포는 파일을 하나씩 지정해 add 한다.
- 개발 서버 미리보기는 브라우저 캐시가 남을 수 있으니 `Cmd+Shift+R`. 화면 검증은 헤드리스 Chrome 캡처(390px 폭은 기기 에뮬레이션)로 한다.
- 볼트 루트의 `index.md`(title: Hide Park)가 홈이다. 폴더 이름과 별개로 소문자 `index`여야 한다.

## 작업 방식
- 한국어, 차분하고 간결하게. 가장 작은 단위부터 한 단계씩, 구체적인 다음 행동 중심.
- 사용자는 터미널과 Git에 익숙하지 않다. 명령은 무엇을 하는지와 기대 결과를 함께 설명한다.

## 남은 과제
- 디자인 디테일 한 번에 다듬기 (모바일 Thoughts와 About 확인, 호버 효과 확인, 다크 모드 값 확정)
- 경로(breadcrumb)의 폴더 자리: `2. Wiki/index.md`가 없어져 `2 Wiki`로 나올 수 있음. `Wiki`로 하려면 폴더마다 index.md(title: Wiki 등)를 만든다 (배포 사이트에서 확인 전).
- 볼트 데이터: Thoughts의 Date와 Type 비어 있음, Region(Countries+Cities) 있는 노트 28개뿐, 값에 `colleague` 같은 것 섞임, 루트의 Pasted image가 공개 레포에 올라가 있음
- 히스토리 사이드바, 태그 시스템(보류), Pretendard(보류)
- 볼트 오타 [!summray] 1건

## 디자인
- 디자인 명세는 DESIGN.md, 시안 캡처는 docs/design/ 에 있다. 디자인 작업 전에 읽는다.
