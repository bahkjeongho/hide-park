# Topic 점검 보고서 (읽기 전용, 2026-11-04)

볼트 `2. Wiki`와 `docs/topic-mapping.csv`(269행)를 대조했다. 아무것도 수정하지 않았다.

## 1. 매핑 표에 없는 topic 값
- **0건.** 노트에 쓰인 값은 모두 표에 있다.
- 표의 열은 `Topic(현재 값), 노트 수, Category, Sub-Category, Field, Sub-Field, Type, Sub-Type, Topic (최종 값), 확인 필요 메모, 처리 방식`이다.

## 2. topic 현황 (md 2,905개)
| 구분 | 노트 수 |
|---|---|
| topic 있음 | 2,739 |
| 값 1개 | 402 |
| 값 여러 개(리스트) | 2,337 |
| topic 없음(빈 값, 속성은 있음) | 100 |
| frontmatter 자체가 없음 | 66 (Writer, Filmmaker, Youtuber 등 topic 이름과 같은 허브 노트로 보임) |

- topic 비어 있는 노트와 frontmatter 없는 노트 166개의 경로는 필요하면 따로 뽑는다(예: Hide Park, Giorgia Lupi, Graham Harvey, Shelby Hawker, Allen Gove, Leonardo Landoni, Abbott Miller).
- 값이 `[[ ]]` 링크가 아닌 평문인 노트 2개: `Natalie Patane.md`(URL `https://nataliepatane.com/`), `London Design Biennale.md`(`"Multidisciplinary"`).

## 3. 표기 방식
- topic은 소문자 `topic`, 값은 **`[[ ]]` 링크의 YAML 리스트**(2,737개). 평문은 위 2개뿐이다.
- 다른 속성은 대문자 시작(`IG`, `URL`, `Website`, `Countries`, `Cities`, `Wikis`, `Related`, `Genre`, `Labels`, `Member of`), `aliases`, `tags`는 소문자. 공백 있는 이름(`Member of`)과 붙여 쓴 이름(`SubDiscipline`)이 섞여 있다. 하이픈 속성은 없다.
- 새 속성도 같은 규칙(첫 글자 대문자, 값은 `[[ ]]` 링크 리스트)을 따르면 일관적이다.

## 4. 새 속성 이름이 이미 쓰이는 노트
- `Category`: `빠른손.md` 1개
- `Type`: `Thom Bettridge (Interview).md` 1개
- `Field`, `Sub-Category`, `Sub-Field`, `Sub-Type`: 없음
- 이 두 노트는 적용 때 덮어쓰지 말고 값을 확인한 뒤 처리해야 한다.
- 참고: Subject Area, Discipline, SubDiscipline, Orientation 등이 학교 노트 60개에 쓰이지만 새 속성과 이름은 겹치지 않는다.

## 5. topic을 참조하는 곳
- `make-labels.mjs` 44행: topic 첫 값을 홈 목록 라벨로 사용. 56행: topic 전체를 `wiki-meta.json`의 `topics`로 만듦.
- `quartz.config.yaml` 289행: `note-properties` 플러그인의 표시 속성 목록에 `topic`이 있다. 같은 목록에 `type`이 이미 있고, 새 속성(Category, Field 등)을 화면에 보이려면 여기에 추가해야 한다.
- `quartz-folder-index` 플러그인(`.quartz/plugins`): `wiki-meta.json`의 topic으로 Topic 필터를 만든다. 테스트는 `tools/example-wiki-filter-test.js`.
- `custom.scss`와 `quartz/components`: topic 직접 참조 **없음**.
- 영향: topic 값 순서나 내용이 바뀌면 사이트 라벨과 필터가 바뀐다(첫 값이 라벨).

## 6. 처리 방식별 집계
행(topic 값 종류)과 노트 수(값 기준, 한 노트에 여러 값이 있어 합이 노트 수보다 크다):

| 처리 방식 | 값 종류 | 값 기준 노트 수 | 이 값을 가진 노트 수(중복 제거) | 적용 |
|---|---|---|---|---|
| 확정 | 119 | 2,504 | 1,903 | 적용 |
| 추정 확인 | 49 | 464 | 448 | 적용 |
| Field 추가 | 50 | 1,732 | 1,274 | 빈칸 |
| Type 추가 | 43 | 1,727 | 1,341 | 빈칸 |
| 상위 허브 | 4 | 766 | 708 | 빈칸 |
| Sub-Type 확인 | 4 | 11 | 11 | 빈칸 |
| 노트 수정 | 1 | 1 | 1 | 빈칸 (URL 입력 노트) |

- 적용 대상(확정 + 추정 확인): 값 168종, **값 기준 2,968건**. 노트 단위로는 중복을 빼고 아래 dry-run 계산을 따른다.
- "Field 추가", "Type 추가"는 표에 Field 또는 Type이 비어 있어 해당 칸만 빈칸으로 남고, 채워진 칸은 적용 가능한지 사용자 결정이 필요하다. 이 보고서는 지시대로 적용 대상에서 뺐다.

## 7. 적용 계획 요약 (dry-run, 변경 예정)
- 노트가 가진 값 중 처리 방식이 확정 또는 추정 확인인 값이 하나라도 있는 노트가 변경 후보다. 정확한 노트 수는 dry-run 스크립트를 짜서 계산해야 한다(이번 점검에서는 값 단위 집계까지만 했다).
- 건너뛸 노트: topic 없음 100개, frontmatter 없음 66개, 값이 모두 빈칸 처리 방식인 노트.
- 먼저 풀어야 할 충돌/주의:
  1. `빠른손.md`의 Category, `Thom Bettridge (Interview).md`의 Type 기존 값과 충돌 처리
  2. 평문 topic 2개와 URL topic 1개 수동 수정
  3. `note-properties` 목록에 새 속성 추가 여부 결정
  4. `make-labels.mjs`가 topic 첫 값을 라벨로 쓰므로 Topic (최종 값)과 순서를 어떻게 둘지 결정
  5. 속성이 6개(Category … Sub-Type)로 늘면 노트 frontmatter 길이가 커진다. 값이 있을 때만 쓰고 빈 속성은 만들지 않는 편이 `clean-frontmatter.mjs`와 맞다.
- 이후 단계: 적용 전에 백업, 한 번에 100개가 아닌 전체 dry-run → 건수 확인 → 적용 순으로 진행한다.
