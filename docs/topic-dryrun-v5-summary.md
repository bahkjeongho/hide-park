# Topic dry-run v5 요약

- 전체 md 2905 / 건너뜀: frontmatter 없음 66, topic 비어 있음 101 / 분석 대상 2738

## status별 노트 수 (v4 대비)
|status|v5|v4|변화|
|---|---|---|---|
|complete|1516|1516|+0|
|resolved_a|945|910|+35|
|resolved_b|176|211|-35|
|domain_only|64|64|+0|
|kind_only|36|36|+0|
|none|1|1|+0|

## resolved_b 조합 상위 20 (축, 이김, 진)
|노트 수|축|이김|진|
|---|---|---|---|
|25|종류|Director|Photographer|
|11|종류|Director|Graphic Designer|
|9|종류|Brand|Fashion Designer|
|9|도메인|Photography|Video, Video Director|
|9|종류|Director|Fashion Designer|
|8|도메인|Creative|Brand Design|
|8|종류|Book|Book Store|
|8|도메인|Creative|Fashion, Fashion Designer|
|6|종류|Director|Stylist|
|5|도메인|Video|Photographer, Photography|
|3|종류|Studio|Agency, Branding Agency|
|3|종류|Studio|Graphic Designer|
|2|도메인|Creative|Brand Design, Branding Agency|
|2|종류|Agency|Design Group|
|2|도메인|Photography|Film, Film Director|
|2|도메인|Creative|Fashion, Styling, Stylist|
|2|종류|Programmer|Entrepreneur|
|2|종류|Rapper|Music Artist, Producer|
|2|도메인|Art Direction|Fashion, Styling, Stylist|
|2|종류|Entrepreneur|Investor|

## new_topic이 빈 노트
- 합계 195
- 한 축만 있음(domain_only/kind_only/none): 101
- topic_dropped_lt5: 87
- topic_dropped_override(Engineering CEO): 7
- 기타(같은 행인데 J가 Topic이 아님 등): 0

## 새 composed Topic 중 노트 수 5 이상
- Brand Design Agency: 43
- Graphic Design School: 28
- Fine Art School: 24
- K-Pop Company: 23
- Graphic Design Studio: 19
- Film School: 15
- Brand Design Studio: 15
- Photography School: 14
- Design School: 13
- Fashion Design School: 12
- Photography Director: 11
- Industrial Design School: 11
- Fashion Design Brand: 9
- Brand Design Consultancy: 8
- Animation School: 7
- Art Direction Award: 6
- Illustration School: 6
- Brand Designer: 5
- Textile Design School: 5
- Furniture Design School: 5
- Digital Design School: 5

- 5 미만으로 버려진 종류 65, 노트 87

## J열 불일치
- 없음

## 매핑 누락
- 없음

## existing_property
- 없음

## 규칙 메모
- J=Category 행은 같은 깊이 충돌에서 최하위로 (a)로 센다.
- Multidisciplinary 도메인 행 제외(flags: multidisciplinary_excluded).
- Editor-in-Chief>Editor, CEO>Entrepreneur는 (a).
- 나머지는 v3와 같다.

## status none 노트
- London Design Biennale.md : Multidisciplinary
- 규칙 추가(v5): 행 J=Category이거나 역할 전용 행(Magazine, School처럼 topic 이름이 Type/Sub-Type과 같은 행)에서 온 도메인 후보는 최하위로 본다.
- 합성 Topic 덮어쓰기: Brand Design Designer→Brand Designer, Engineering CEO→비움.
- composed_match는 이제 CSV I열(Topic 최종 값)과 비교한다(v4는 A열과 비교했다).