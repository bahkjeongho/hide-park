# Wiki 속성 체계 (Category / Field / Type / Topic)

2026-11-05에 노트의 소문자 `topic`을 지우고 아래 7개 속성으로 바꿨다. 이 문서는 작업 이력과 규칙, 도구 사용법이다.

## 속성
| 속성 | 의미 |
|---|---|
| Category, Sub-Category | 도메인 축의 윗부분 (예: Design > Fashion) |
| Field, Sub-Field | 도메인 축의 구체 분야 (예: Popular Music > K-Pop) |
| Type, Sub-Type | 종류 축 (예: People > Idol, Organization > Agency) |
| Topic | 두 축을 합친 핵심 분류 (예: K-Pop Idol, Creative Agency). 사이트에 보이는 것은 이것뿐 |

- 값은 `"[[값]]"` 링크 리스트이고, 빈 값은 쓰지 않는다(시범으로 `London Design Biennale`만 빈 속성 줄 7개를 둠).
- 원래의 4단계 분류(최상위, 상위, 중간, 하위)는 볼트 `00. Template/Wiki System.md`에 있고, 이 체계의 전신이다.

## 입력 데이터
- `docs/topic-mapping.csv`: 원래 topic 값 269종 → Category … Topic 매핑. 열 `Topic(현재 값), 노트 수, Category, Sub-Category, Field, Sub-Field, Type, Sub-Type, Topic (최종 값), 최종 속성 종류`.
- `docs/topic-dryrun-v5.csv`: 노트별 계산 결과(적용에 쓴 것). 요약은 `topic-dryrun-v5-summary.md`, 확인용 샘플은 `topic-dryrun-v5-sample.md`.

## 노트별 계산 규칙 (v5)
1. 노트의 각 원래 topic 값을 매핑 행으로 찾아 두 축의 후보 경로를 모은다. 도메인 축 (Category, Sub-Category, Field, Sub-Field), 종류 축 (Type, Sub-Type).
2. 한 후보가 다른 후보의 앞부분이면 호환이다. 더 깊은 쪽을 택한다.
3. 호환되지 않으면 충돌이다. (a) 더 깊은 쪽이 이긴다. 같은 깊이면 J열이 Category인 행과 역할 전용 행(Magazine, School처럼 값 이름이 Type과 같은 행)이 최하위다. 일반 값(Visual Art, Culture, Artist, Creator)도 최하위. (b) 그래도 같으면 원래 리스트에서 앞에 있던 값이 이긴다. 진 값은 CSV의 `secondary`에 남긴다.
4. 도메인 후보에서 Field가 Multidisciplinary인 행은 제외한다.
5. 종류 축 예외: Editor-in-Chief가 Editor를, CEO가 Entrepreneur를 이긴다.
6. Topic은 두 축이 모두 있을 때만 만든다. 같은 행에서 나왔고 J열이 Topic이면 그 행의 최종 값, 아니면 "가장 깊은 도메인 값 + 종류 값"으로 합성한다. 합성한 값은 CSV의 최종 Topic에 있거나 5개 이상 노트에서 나올 때만 남긴다. 덮어쓰기: `Brand Design Designer`는 `Brand Designer`로, `Engineering CEO`는 비운다.

## 적용 이력 (2026-11-05)
- v5 결과를 `docs/apply_topic_props.py`로 노트 2,737개에 썼다(시범 5개 포함). 본문과 기존 줄은 바뀌지 않았음을 검증함.
- 이어서 `2. Wiki`의 소문자 `topic`을 2,834개 노트에서 삭제했다.
- 사이트: `make-labels.mjs`가 `Topic`을 읽고, `quartz.config.yaml` note-properties는 `includeAll: true`에 Category, Sub-Category, Field, Sub-Field, Type, Sub-Type을 제외했다. 배포 확인함.

## 도구
- `python3 docs/apply_topic_props.py --all --dry` (건수만), `--all` (적용), `--notes "파일.md" …` (일부). 같은 키가 있는 노트는 건너뛰고, 검증 실패 시 되돌린다. 실행 전 Obsidian을 종료할 것.

## 백업과 롤백
- `~/Developer/hide-park-backup-20261105/`: 새 속성을 쓰기 전의 볼트 .md 4,677개(원래 `topic` 값이 있음). 파일 수와 해시는 `BACKUP_INFO.txt`.
- `~/Developer/hide-park-backup-20261105c/2. Wiki/`: 소문자 `topic`을 지우기 직전의 `2. Wiki` 2,905개(새 속성이 있는 상태). `…105b`는 복사가 중단된 불완전한 폴더라 쓰지 않는다.
- 노트 하나 복원: 백업 폴더의 파일을 볼트의 같은 위치에 `cp`로 덮어쓴다. 전체 복원은 백업 이후의 편집이 사라지니 사용자에게 먼저 알린다.

## 미해결
- Topic이 비어 있는 노트 약 190개와 `London Design Biennale`(Multidisciplinary뿐)의 분류.
- 충돌 규칙 추가 다듬기, 합성 Topic 이름이 어색한 값(예: Photography Director) 검토.
- `Category`, `Type` 등 값에 해당하는 링크 대상 노트가 없다(값 310종 중 62종만 노트가 있음).
- 속성 탭에 `Title`, `Modified`가 새로 보임. 제외할지 결정 필요.
- 볼트에서 frontmatter가 없는 노트 66개(허브 노트)는 이 작업 대상이 아니다.

## 허브 노트 (2026-11-05)
- 속성 값(Category … Topic) 312종마다 허브 노트가 있다. 허브 311개 전부 `2. Wiki/21. Hub/`에 있고 `unlisted: true`다(새로 만든 249개 + 기존 62개를 옮겨 형식 통일: aliases, tags, Related, unlisted. 값이 있던 Parent Topic, Sub Topic은 유지).
- 같은 이름은 속성이 달라도 허브 하나에 모은다. 값 `Web & UI/UX`는 파일 이름에 `/`를 쓸 수 없어 `Web & UI-UX`로 바꿨다(Awwwards, FWA Awards).
- 본문의 `<!-- hub:start -->` ~ `<!-- hub:end -->` 사이는 `python3 docs/make_hubs.py --out <스테이징폴더> --apply`가 다시 만든다(노트가 150개를 넘는 상위 허브는 하위 분류와 Topic 목록만). 이 구간 밖의 내용은 건드리지 않는다. 실행 전 Obsidian 종료와 백업은 필수.
- 사이트: `unlisted`라 검색, 그래프, 탐색기, 폴더 목록에서 빠지고 링크로만 열린다. `make-labels.mjs`도 `21 Hub` 폴더를 목록, 라벨, 필터에서 뺀다.
- 백업: `~/Developer/hide-park-backup-20261105d/2. Wiki`(허브 생성 직전).
- 백업: `…105e/2. Wiki`는 기존 허브 62개를 옮기기 직전 상태.

## 프롬프트
- 볼트 `00. Template/'00. Prompt.md`의 Wiki, Artist, Art School 프롬프트는 이 체계를 따른다(맨 위 "분류 속성" 절). Music(3. Object)은 소문자 `topic`을 그대로 쓴다. `Wiki Template.md`, `Artist Template.md`의 `topic:` 줄은 아직 그대로다.

## 3. Object와 빈 속성 (2026-11-05)
- 31. Music, 32. Architecture, 33. Video도 7개 속성을 쓴다. `docs/apply_object_props.py`로 순서를 정리했다(Genre, Date, title, 옛 type 삭제). 백업 `…105f/3. Object`.
- `docs/fill_class_props.py`로 `2. Wiki`(21. Hub 제외) 전 노트에 7개 속성 줄을 빈 값이라도 채웠고, 31. Music 전 노트에 Category=The Arts, Sub-Category=Music, Field=Popular Music, Type=Record를 넣었다. 예전 topic의 EP, Studio Album, Single, Compilation은 Sub-Type으로 옮기고 Topic은 비웠다. 백업 `…105g`(2. Wiki, 3. Object).
- 새 값(Record, EP, Studio Album, Single, Compilation)의 허브는 아직 없다. make_hubs.py가 3. Object(31~34)도 읽도록 확장했고(허브 323개), 새 허브 11개(Record, EP, Studio Album, Single, Compilation 등)를 `21. Hub`에 만들었다. 백업 `…105h`.
