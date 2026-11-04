# Topic dry-run v4 요약

- 전체 md 2905 / 건너뜀: frontmatter 없음 66, topic 비어 있음 101 / 분석 대상 2738

## status별 노트 수 (v3 대비)
|status|v4|v3|변화|
|---|---|---|---|
|complete|1516|1381|+135|
|resolved_a|910|845|+65|
|resolved_b|211|420|-209|
|domain_only|64|65|-1|
|kind_only|36|27|+9|
|none|1|0|+1|

## resolved_b 조합 상위 20 (축, 이김, 진)
|노트 수|축|이김|진|
|---|---|---|---|
|27|도메인|Media|Design, Design Magazine|
|25|종류|Director|Photographer|
|11|종류|Director|Graphic Designer|
|9|종류|Brand|Fashion Designer|
|9|도메인|Photography|Video, Video Director|
|9|종류|Director|Fashion Designer|
|8|도메인|Creative|Brand Design|
|8|종류|Book|Book Store|
|8|도메인|Creative|Fashion, Fashion Designer|
|6|종류|Director|Stylist|
|6|도메인|Media|Tech, Tech Magazine|
|5|도메인|Video|Photographer, Photography|
|3|종류|Studio|Agency, Branding Agency|
|3|종류|Studio|Graphic Designer|
|2|도메인|Creative|Brand Design, Branding Agency|
|2|종류|Agency|Design Group|
|2|도메인|Photography|Film, Film Director|
|2|도메인|Creative|Fashion, Styling, Stylist|
|2|종류|Programmer|Entrepreneur|
|2|종류|Rapper|Music Artist, Producer|

## new_topic이 빈 노트
- 합계 186
- 한 축만 있음(domain_only/kind_only/none): 101
- topic_dropped_lt5: 85
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
- Engineering CEO: 7
- Art Direction Award: 6
- Illustration School: 6
- Brand Design Designer: 5
- Textile Design School: 5
- Furniture Design School: 5
- Digital Design School: 5

- 5 미만으로 버려진 종류 63, 노트 85

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