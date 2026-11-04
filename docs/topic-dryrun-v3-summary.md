# Topic dry-run v3 요약

- 전체 md 노트 2905개 / 건너뜀: frontmatter 없음 66, topic 비어 있음 101 / 분석 대상(topic 있음) 2738

## status별 노트 수
- complete: 1381
- resolved_a: 845
- resolved_b: 420
- domain_only: 65
- kind_only: 27

## 충돌 해결 방식별 노트 수 (충돌이 있었던 노트)
- (a) 더 구체적인 쪽: 850
- (b) 리스트 앞쪽 값: 434
- 한 노트에 두 축 모두 충돌하면 (b)가 하나라도 있으면 b로 센다.

## 충돌 값 조합 상위 20
|축|조합|노트 수|해결|
|---|---|---|---|
|kind|K-Pop Idol + Music Artist|456|a:456|
|dom|Fashion + Fashion Magazine + Magazine + Media|74|a:74|
|dom|Creative + Creative Direction + Creative Director|59|b:59|
|dom|Brand Design + Branding Agency|40|a:40|
|kind|Academic Program + Graphic Design Program + School|28|a:28|
|dom|Design + Design Magazine + Magazine + Media|27|b:27|
|dom|Creative + Creative Direction + Creative Studio|25|b:25|
|kind|Academic Program + Fine Art Program + School|24|a:24|
|dom|Entertainment Company + K-Pop|23|a:23|
|kind|Director + Photographer + Video Director|15|b:15|
|kind|Academic Program + Film Program + School|15|a:15|
|dom|Creative + Creative Studio|14|b:14|
|dom|Photographer + Photography + Video + Video Director|14|b:14|
|kind|School + University|14|b:14|
|kind|Academic Program + Photography Program + School|14|a:14|
|kind|Editor + Editor-in-Chief|14|b:14|
|kind|Academic Program + Design Program + School|13|a:13|
|kind|Academic Program + Fashion Design Program + School|12|a:12|
|dom|Culture + Culture Magazine + Magazine + Media|12|a:12|
|dom|Creative + Creative Agency|11|b:11|

## kind_only 노트가 가장 많은 원본 topic 값 상위 20 (도메인 판별 필요)
- School: 17
- University: 14
- Writer: 4
- Academic Program: 3
- Award: 3
- Comptetition: 1
- Human Network: 1
- Critic: 1

## composed=true & composed_match=false Topic (CSV에 없는 새 후보)
- 종류 82, 노트 375
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
- Multidisciplinary Award: 9
- Brand Design Consultancy: 8
- Animation School: 7
- Art Direction Award: 6
- Illustration School: 6
- Brand Design Designer: 5
- Textile Design School: 5
- Furniture Design School: 5
- Digital Design School: 5
- Styling Director: 3
- Engineering CEO: 3
- Creative Editor: 3
- Furniture Design Studio: 3
- Acting School: 2
- Production School: 2
- Web & UI/UX Award: 2
- Brand Design Company: 2
- Typography Magazine: 2
- Craft School: 2
- Editorial Design Award: 2
- Typography Studio: 2
- Blog Writer: 2
- Engineering Entrepreneur: 2
- Graphic Design Award: 2
- Typography School: 2
- Investment Entrepreneur: 2
- Typography Award: 2
- Publishing Studio: 1
- Publishing Journalist: 1
- Film Company: 1
- News Company: 1
- Acting Director: 1
- Motion Design Studio: 1
- Philosophy Critic: 1
- Popular Music Brand: 1
- Comics School: 1
- Architectural Design Studio: 1
- Popular Music Writer: 1
- Media Collective: 1
- Graphic Design Festival: 1
- Space Award: 1
- Fashion Journalism Critic: 1
- Space Design School: 1
- Playwriting School: 1
- Stage Management School: 1
- Costume Design School: 1
- Popular Music Editor: 1
- Design Collective: 1
- Graphic Design Collective: 1
- Music Radio: 1
- Curating Publisher: 1
- Production Design School: 1
- Motion Design Agency: 1
- Branding School: 1
- Art Direction Studio: 1
- Furniture Design Festival: 1
- Scenography School: 1
- Screenwriting School: 1
- Furniture Design Designer: 1
- Digital Design Studio: 1
- Moving Image Magazine: 1
- Styling Designer: 1
- Management Company: 1
- Programming Designer: 1
- Photography Magazine: 1
- Sociology Critic: 1
- Editorial Design Studio: 1
- Audio-Visual Collective: 1
- Graphic Design Promoter: 1

## J열 불일치 (단일 행 매칭 노트)
- 없음

## 매핑 누락 topic 값
- 없음

## existing_property 노트
- 없음

## 규칙 해석 메모
- 행 안의 빈 칸 사이 공백(gap)은 건너뛰고 비어 있지 않은 값만 경로로 사용. gap이 있는 행은 flags에 gap_in_row.
- 충돌이 한 축에만 있고 다른 축이 비면 status는 domain_only/kind_only, flags에 conflict_a/b.
- 일반 값 우선순위 낮음: 도메인 끝값 Visual Art, Culture / 종류 끝값 Artist, Creator.