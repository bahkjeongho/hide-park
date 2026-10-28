# Journal 속성 시험 변환 결과 (2단계)

볼트 원본은 수정하지 않았습니다. 스크립트 `docs/work/journal-fix.mjs`, 변환 결과 복사본 `docs/work/journal-out/`, 원자료 `docs/work/journal-report.json`.

## 요약

- 대상 노트 60개, 복사본 생성 60개, frontmatter가 바뀐 노트 60개
- 본문 해시 전후 일치: **60 / 60**
- 멱등성: 변환 결과를 입력으로 같은 스크립트를 다시 실행하면 변경 0건이고 파일이 완전히 같음(`diff -r` 일치)
- 병합 충돌(목표 속성으로 합칠 때 값이 서로 다른 경우): 0건
- 적용한 규칙: `subject_area`→`Subject Area`, `research_orientation`→`Orientation`, `Country/Region`→`Countries`, 소문자 이름은 대소문자만 맞춤, `title`·`aliases`·`IG`·`Website`·`Wikis`·`Cities` 삭제, `tags`·`Related`는 빈 속성
- 국가 약어: `USA`→`[[USA]]`, `UK`→`[[UK]]`, `NL`→`[[Netherlands]]`, `PL`→`[[Poland]]`. 이 국가들은 볼트에 별도 노트 파일이 없고 다른 노트들이 쓰는 `[[UK]]` 같은 표기에 맞춘 것입니다.

## 변환 전후 비교 샘플 10개

### 2. Wiki/Cultural Studies (CS).md

**전**

```yaml
title: Cultural Studies (CS)
aliases: []
academy:
Country/Region: UK
language: EN
discipline: Cultural Studies
subdiscipline: Cultural Studies
publisher: Taylor & Francis
research_orientation: Cultural Studies
subject_area:
  - Digital Media
  - Media
  - Popular Culture
URL:
  - https://www.tandfonline.com/journals/rcus20
tags: []
Related: []
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Digital Media]]"
  - "[[Media]]"
  - "[[Popular Culture]]"
Discipline:
  - "[[Cultural Studies]]"
SubDiscipline:
  - "[[Cultural Studies]]"
Orientation: Cultural Studies
Academy:
Publisher:
  - "[[Taylor & Francis]]"
URL:
  - https://www.tandfonline.com/journals/rcus20
Countries:
  - "[[UK]]"
Language: EN
tags:
Related:
```

### 2. Wiki/OASE- Journal for Architecture (OASE).md

**전**

```yaml
title: "OASE: Journal for Architecture (OASE)"
aliases: []
academy:
Country/Region: NL
language: EN
discipline: Design Studies
subdiscipline: Architecture
publisher: nai010 publishers
research_orientation: Critical Theory
subject_area:
  - Design
  - Visual Art
URL:
  - https://oasejournal.nl/en/
tags: []
Related: []
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Design]]"
  - "[[Visual Art]]"
Discipline:
  - "[[Design Studies]]"
SubDiscipline:
  - "[[Architecture]]"
Orientation: Critical Theory
Academy:
Publisher:
  - "[[nai010 publishers]]"
URL:
  - https://oasejournal.nl/en/
Countries:
  - "[[Netherlands]]"
Language: EN
tags:
Related:
```

### 2. Wiki/Studia Logica (SL).md

**전**

```yaml
title: Studia Logica (SL)
aliases: []
academy:
Country/Region: PL
language: EN
discipline: Philosophy
subdiscipline: Philosophy
publisher: Springer
research_orientation: Analytic Philosophy
subject_area:
  - Philosophy
URL:
  - https://link.springer.com/journal/11225
tags: []
Related: []
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Philosophy]]"
Discipline:
  - "[[Philosophy]]"
SubDiscipline:
  - "[[Philosophy]]"
Orientation: Analytic Philosophy
Academy:
Publisher:
  - "[[Springer]]"
URL:
  - https://link.springer.com/journal/11225
Countries:
  - "[[Poland]]"
Language: EN
tags:
Related:
```

### 2. Wiki/Antikythera Journal (Antikythera).md

**전**

```yaml
title: Antikythera Journal (Antikythera)
aliases: []
academy:
Country/Region: INT
language: EN
discipline: Art History
subdiscipline: Contemporary Art
publisher: Antikythera
research_orientation: Critical Theory
subject_area:
  - Digital Media
  - Visual Art
URL:
  - https://journal.antikythera.org/
tags: []
Related: []
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Digital Media]]"
  - "[[Visual Art]]"
Discipline:
  - "[[Art History]]"
SubDiscipline:
  - "[[Contemporary Art]]"
Orientation: Critical Theory
Academy:
Publisher:
  - "[[Antikythera]]"
URL:
  - https://journal.antikythera.org/
Countries:
  - "[[INT]]"
Language: EN
tags:
Related:
```

### 2. Wiki/Antikythera.md

**전**

```yaml
aliases:
topic:
  - "[[Journal]]"
IG:
  - https://www.instagram.com/antikythera_xyz/
Website: https://journal.antikythera.org/
URL:
  - https://www.linkedin.com/company/antikythera-program/
Wikis:
Cities:
Countries:
tags:
Related:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
Discipline:
SubDiscipline:
Orientation:
Academy:
Publisher:
URL:
  - https://www.linkedin.com/company/antikythera-program/
Countries:
Language:
tags:
Related:
```

### 2. Wiki/AA Files (AAF).md

**전**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Design]]"
  - "[[Visual Art]]"
discipline: "[[Design Studies]]"
subdiscipline: "[[Architecture]]"
Orientation: Critical Theory
academy: Architectural Association School of Architecture
publisher: "[[Architectural Association]]"
URL:
  - https://www.aaschool.ac.uk
Countries:
  - "[[UK]]"
language: EN
tags: []
Related: []
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Design]]"
  - "[[Visual Art]]"
Discipline:
  - "[[Design Studies]]"
SubDiscipline:
  - "[[Architecture]]"
Orientation: Critical Theory
Academy: Architectural Association School of Architecture
Publisher:
  - "[[Architectural Association]]"
URL:
  - https://www.aaschool.ac.uk
Countries:
  - "[[UK]]"
Language: EN
tags:
Related:
```

### 2. Wiki/International Journal of Art & Design Education (IJADE).md

**전**

```yaml
title: International Journal of Art & Design Education (IJADE)
aliases: []
academy: National Society for Education in Art and Design
Country/Region: UK
language: EN
discipline: Design Studies
subdiscipline: Art & Design Education
publisher: Wiley
research_orientation: Interdisciplinary Research
subject_area:
  - Design
  - Education
  - Visual Art
URL:
  - https://onlinelibrary.wiley.com/journal/14768070
tags: []
Related:
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Design]]"
  - "[[Education]]"
  - "[[Visual Art]]"
Discipline:
  - "[[Design Studies]]"
SubDiscipline:
  - "[[Art & Design Education]]"
Orientation: Interdisciplinary Research
Academy: National Society for Education in Art and Design
Publisher:
  - "[[Wiley]]"
URL:
  - https://onlinelibrary.wiley.com/journal/14768070
Countries:
  - "[[UK]]"
Language: EN
tags:
Related:
```

### 2. Wiki/Daedalus.md

**전**

```yaml
title: Daedalus
aliases: []
academy: American Academy of Arts and Sciences
Country/Region: USA
language: EN
discipline: Philosophy
subdiscipline: Philosophy
publisher: MIT Press
research_orientation: Interdisciplinary Research
subject_area:
  - Literature
  - Philosophy
URL:
  - https://direct.mit.edu/daed
tags: []
Related: []
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Literature]]"
  - "[[Philosophy]]"
Discipline:
  - "[[Philosophy]]"
SubDiscipline:
  - "[[Philosophy]]"
Orientation: Interdisciplinary Research
Academy: American Academy of Arts and Sciences
Publisher:
  - "[[MIT Press]]"
URL:
  - https://direct.mit.edu/daed
Countries:
  - "[[USA]]"
Language: EN
tags:
Related:
```

### 2. Wiki/Afterall- A Journal of Art, Context and Enquiry (Afterall).md

**전**

```yaml
aliases: []
academy: Afterall Research Centre
Country/Region: "[[UK]]"
language: EN
discipline: "[[Art History]]"
subdiscipline: "[[Contemporary Art]]"
publisher: "[[University of Chicago Press]]"
research_orientation: Critical Theory
subject_area:
  - Visual Art
URL:
  - https://www.afterall.org/
tags: []
Related:
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Visual Art]]"
Discipline:
  - "[[Art History]]"
SubDiscipline:
  - "[[Contemporary Art]]"
Orientation: Critical Theory
Academy: Afterall Research Centre
Publisher:
  - "[[University of Chicago Press]]"
URL:
  - https://www.afterall.org/
Countries:
  - "[[UK]]"
Language: EN
tags:
Related:
```

### 2. Wiki/Communication and Critical-Cultural Studies (CCCS).md

**전**

```yaml
title: Communication and Critical/Cultural Studies (CCCS)
aliases: []
academy: National Communication Association
Country/Region: USA
language: EN
discipline: Communication Studies
subdiscipline: Cultural Studies
publisher: Taylor & Francis
research_orientation: Critical Theory
subject_area:
  - Communication
  - Media
  - Popular Culture
URL:
  - https://www.tandfonline.com/journals/rccc20
tags: []
Related: []
topic:
  - "[[Journal]]"
IG:
Website:
Wikis:
Cities:
Countries:
```

**후**

```yaml
topic:
  - "[[Journal]]"
Subject Area:
  - "[[Communication]]"
  - "[[Media]]"
  - "[[Popular Culture]]"
Discipline:
  - "[[Communication Studies]]"
SubDiscipline:
  - "[[Cultural Studies]]"
Orientation: Critical Theory
Academy: National Communication Association
Publisher:
  - "[[Taylor & Francis]]"
URL:
  - https://www.tandfonline.com/journals/rccc20
Countries:
  - "[[USA]]"
Language: EN
tags:
Related:
```

## 본문 해시 비교 (SHA-256 앞 12자리)

| 노트 | 전 | 후 | 일치 |
|---|---|---|---|
| AA Files (AAF).md | `ccc5ecfa5f02` | `ccc5ecfa5f02` | ✅ |
| ARTMargins (ARTMargins).md | `c1064d19784c` | `c1064d19784c` | ✅ |
| Afterall- A Journal of Art, Context and Enquiry (Afterall).md | `d3c909254f61` | `d3c909254f61` | ✅ |
| Afterimage- The Journal of Media Arts and Cultural Criticism.md | `02aefe6493e4` | `02aefe6493e4` | ✅ |
| Analysis.md | `d954a04152fe` | `d954a04152fe` | ✅ |
| Antikythera Journal (Antikythera).md | `c90197f74f0c` | `c90197f74f0c` | ✅ |
| Antikythera.md | `713c3ecbb937` | `713c3ecbb937` | ✅ |
| Communication and Critical-Cultural Studies (CCCS).md | `be4c3364026e` | `be4c3364026e` | ✅ |
| Computational Culture (CC).md | `c1064d19784c` | `c1064d19784c` | ✅ |
| Computer Music Journal (CMJ).md | `b8f31e2fa249` | `b8f31e2fa249` | ✅ |
| Critical Inquiry (CI).md | `444a7cb65cde` | `444a7cb65cde` | ✅ |
| Critical Quarterly (CQ).md | `51afb104aa33` | `51afb104aa33` | ✅ |
| Critical Studies in Television (CST).md | `4c76c1d18876` | `4c76c1d18876` | ✅ |
| Cultural Studies (CS).md | `0bc847ede978` | `0bc847ede978` | ✅ |
| Cultural Studies ↔ Critical Methodologies (CSCM).md | `dd049e0ef5c6` | `dd049e0ef5c6` | ✅ |
| Cultural Trends (CT).md | `fa897f1e9554` | `fa897f1e9554` | ✅ |
| Daedalus.md | `67b357062f9d` | `67b357062f9d` | ✅ |
| Design Issues (DI).md | `0e7f08ab417f` | `0e7f08ab417f` | ✅ |
| Design Management Journal (DMJ).md | `5ce79b17501a` | `5ce79b17501a` | ✅ |
| Design Studies (DS).md | `2cfce6802d9a` | `2cfce6802d9a` | ✅ |
| Design and Culture (D&C).md | `4ad4c8e89182` | `4ad4c8e89182` | ✅ |
| Digital Creativity (DC) (Taylor & Francis).md | `ed84dd944864` | `ed84dd944864` | ✅ |
| Games and Culture (G&C).md | `0f6aacbaf7ea` | `0f6aacbaf7ea` | ✅ |
| Grey Room (Grey Room).md | `4cb25e6ef53c` | `4cb25e6ef53c` | ✅ |
| International Journal of Art & Design Education (IJADE).md | `cb34d08c93f4` | `cb34d08c93f4` | ✅ |
| International Journal of Cultural Studies (IJCS).md | `f93650a1776d` | `f93650a1776d` | ✅ |
| Journal of Brand Management (JBM).md | `5f344bdc3459` | `5f344bdc3459` | ✅ |
| Journal of Communication (JoC).md | `1d1f110aa152` | `1d1f110aa152` | ✅ |
| Journal of Design History (JDH).md | `16c237464437` | `16c237464437` | ✅ |
| Journal of Popular Music Studies (JPMS).md | `a841f30723fa` | `a841f30723fa` | ✅ |
| Journal of Visual Culture (JVC).md | `3e67664f2ab0` | `3e67664f2ab0` | ✅ |
| Journal of the American Philosophical Association (J-APA).md | `740511157a4a` | `740511157a4a` | ✅ |
| Leonardo (Leonardo).md | `8f71ad923699` | `8f71ad923699` | ✅ |
| Leonardo Music Journal (LMJ).md | `2d705c2c7886` | `2d705c2c7886` | ✅ |
| New Media & Society (NMS).md | `f93aad8e2170` | `f93aad8e2170` | ✅ |
| Noûs (Noûs).md | `19047b90e5f0` | `19047b90e5f0` | ✅ |
| OASE- Journal for Architecture (OASE).md | `010388e262f5` | `010388e262f5` | ✅ |
| October (October).md | `4028a7a17748` | `4028a7a17748` | ✅ |
| Oxford Art Journal (OAJ).md | `15b77ff268f4` | `15b77ff268f4` | ✅ |
| PAJ- A Journal of Performance and Art (PAJ).md | `b19a23bfe84a` | `b19a23bfe84a` | ✅ |
| Performance Research (PR).md | `4dabccd4360a` | `4dabccd4360a` | ✅ |
| Philosophical Issues (PI).md | `7b70a89ee4aa` | `7b70a89ee4aa` | ✅ |
| Philosophical Studies (PS).md | `98c8a616222c` | `98c8a616222c` | ✅ |
| Philosophy Compass.md | `9e94b44d210d` | `9e94b44d210d` | ✅ |
| Popular Music and Society (PMS).md | `d02a22991f07` | `d02a22991f07` | ✅ |
| Res- Anthropology and Aesthetics (RES).md | `39845585510c` | `39845585510c` | ✅ |
| Rock Music Studies (RMS).md | `20c6dff92aa1` | `20c6dff92aa1` | ✅ |
| Social Media + Society (SM+S).md | `5fb78abc6441` | `5fb78abc6441` | ✅ |
| Studia Logica (SL).md | `42aa8cc22c23` | `42aa8cc22c23` | ✅ |
| Synthese (Synthese).md | `80b245ccacdf` | `80b245ccacdf` | ✅ |
| The British Journal of Aesthetics (BJA).md | `2c9d9ce5ba1f` | `2c9d9ce5ba1f` | ✅ |
| The Design Journal (TDJ).md | `0d305264a818` | `0d305264a818` | ✅ |
| The Journal of Aesthetics and Art Criticism (JAAC) (Wiley).md | `fdca66cc83fe` | `fdca66cc83fe` | ✅ |
| The Journal of Aesthetics and Art Criticism (JAAC).md | `52b60c2719e9` | `52b60c2719e9` | ✅ |
| The Philosophical Quarterly (PQ).md | `8b711cc4251a` | `8b711cc4251a` | ✅ |
| The Philosophical Review (PR).md | `8b0fe9bbea7a` | `8b0fe9bbea7a` | ✅ |
| Theory, Culture & Society (TCS).md | `d52f278deecc` | `d52f278deecc` | ✅ |
| Thresholds (Thresholds).md | `470349e6ddd3` | `470349e6ddd3` | ✅ |
| Visible Language (VL).md | `571827d1e260` | `571827d1e260` | ✅ |
| Visual Studies (VS).md | `73660a257330` | `73660a257330` | ✅ |

## 지워지는 값이 있는 노트

- `title`: 57개 노트 (값은 노트 이름과 같은 제목 텍스트, 아래 표 참고)
- `IG` — 2. Wiki/Antikythera.md: `['https://www.instagram.com/antikythera_xyz/']`
- `Website` — 2. Wiki/Antikythera.md: `['https://journal.antikythera.org/']`

<details><summary>title 값이 있던 노트 57개</summary>

- ARTMargins (ARTMargins).md → `ARTMargins (ARTMargins)`
- Afterimage- The Journal of Media Arts and Cultural Criticism.md → `"Afterimage: The Journal of Media Arts and Cultural Criticism"`
- Analysis.md → `Analysis`
- Antikythera Journal (Antikythera).md → `Antikythera Journal (Antikythera)`
- Communication and Critical-Cultural Studies (CCCS).md → `Communication and Critical/Cultural Studies (CCCS)`
- Computational Culture (CC).md → `Computational Culture (CC)`
- Computer Music Journal (CMJ).md → `Computer Music Journal (CMJ)`
- Critical Inquiry (CI).md → `Critical Inquiry (CI)`
- Critical Quarterly (CQ).md → `Critical Quarterly (CQ)`
- Critical Studies in Television (CST).md → `Critical Studies in Television (CST)`
- Cultural Studies (CS).md → `Cultural Studies (CS)`
- Cultural Studies ↔ Critical Methodologies (CSCM).md → `Cultural Studies ↔ Critical Methodologies (CSCM)`
- Cultural Trends (CT).md → `Cultural Trends (CT)`
- Daedalus.md → `Daedalus`
- Design Issues (DI).md → `Design Issues (DI)`
- Design Management Journal (DMJ).md → `Design Management Journal (DMJ)`
- Design Studies (DS).md → `Design Studies (DS)`
- Design and Culture (D&C).md → `Design and Culture (D&C)`
- Digital Creativity (DC) (Taylor & Francis).md → `Digital Creativity (DC)`
- Games and Culture (G&C).md → `Games and Culture (G&C)`
- Grey Room (Grey Room).md → `Grey Room (Grey Room)`
- International Journal of Art & Design Education (IJADE).md → `International Journal of Art & Design Education (IJADE)`
- International Journal of Cultural Studies (IJCS).md → `International Journal of Cultural Studies (IJCS)`
- Journal of Brand Management (JBM).md → `Journal of Brand Management (JBM)`
- Journal of Communication (JoC).md → `Journal of Communication (JoC)`
- Journal of Design History (JDH).md → `Journal of Design History (JDH)`
- Journal of Popular Music Studies (JPMS).md → `Journal of Popular Music Studies (JPMS)`
- Journal of Visual Culture (JVC).md → `Journal of Visual Culture (JVC)`
- Journal of the American Philosophical Association (J-APA).md → `Journal of the American Philosophical Association (J-APA)`
- Leonardo (Leonardo).md → `Leonardo (Leonardo)`
- Leonardo Music Journal (LMJ).md → `Leonardo Music Journal (LMJ)`
- New Media & Society (NMS).md → `New Media & Society (NMS)`
- Noûs (Noûs).md → `Noûs (Noûs)`
- OASE- Journal for Architecture (OASE).md → `"OASE: Journal for Architecture (OASE)"`
- October (October).md → `October (October)`
- Oxford Art Journal (OAJ).md → `Oxford Art Journal (OAJ)`
- PAJ- A Journal of Performance and Art (PAJ).md → `"PAJ: A Journal of Performance and Art (PAJ)"`
- Performance Research (PR).md → `Performance Research (PR)`
- Philosophical Issues (PI).md → `Philosophical Issues (PI)`
- Philosophical Studies (PS).md → `Philosophical Studies (PS)`
- Philosophy Compass.md → `Philosophy Compass`
- Popular Music and Society (PMS).md → `Popular Music and Society (PMS)`
- Res- Anthropology and Aesthetics (RES).md → `"Res: Anthropology and Aesthetics (RES)"`
- Rock Music Studies (RMS).md → `Rock Music Studies (RMS)`
- Social Media + Society (SM+S).md → `Social Media + Society (SM+S)`
- Studia Logica (SL).md → `Studia Logica (SL)`
- Synthese (Synthese).md → `Synthese (Synthese)`
- The British Journal of Aesthetics (BJA).md → `The British Journal of Aesthetics (BJA)`
- The Design Journal (TDJ).md → `The Design Journal (TDJ)`
- The Journal of Aesthetics and Art Criticism (JAAC) (Wiley).md → `The Journal of Aesthetics and Art Criticism (JAAC)`
- The Journal of Aesthetics and Art Criticism (JAAC).md → `The Journal of Aesthetics and Art Criticism (JAAC)`
- The Philosophical Quarterly (PQ).md → `The Philosophical Quarterly (PQ)`
- The Philosophical Review (PR).md → `The Philosophical Review (PR)`
- Theory, Culture & Society (TCS).md → `Theory, Culture & Society (TCS)`
- Thresholds (Thresholds).md → `Thresholds (Thresholds)`
- Visible Language (VL).md → `Visible Language (VL)`
- Visual Studies (VS).md → `Visual Studies (VS)`

</details>

`tags`, `Related`, `aliases`, `Wikis`, `Cities`는 모든 대상 노트에서 값이 비어 있어 사라지는 값이 없습니다.

## 애매한 값과 처리 방식

- `Countries` = `INT` — 2. Wiki/Antikythera Journal (Antikythera).md (국가 표기를 알 수 없어 값 그대로 링크함)
- `SubDiscipline` = `Art & Design Education` — 2. Wiki/International Journal of Art & Design Education (IJADE).md

처리 방식:
- `INT`(Antikythera Journal): 국가 약어인지 International인지 알 수 없어 `[[INT]]`로 값을 그대로 보존했습니다. 3단계 전에 `[[International]]`로 바꿀지, 비울지 정해 주세요.
- `Art & Design Education`: `&`가 값 자체에 포함된 것으로 보여 나누지 않고 `[[Art & Design Education]]` 하나로 변환했습니다.
- 이 밖에 `Taylor & Francis` 등 `Publisher`의 `&`, `Academy`의 `and`는 이름의 일부로 보고 나누지 않았습니다(`Academy`는 어차피 링크 변환 대상이 아님).
- 쉼표·세미콜론·슬래시로 여러 값이 한 문자열에 들어 있는 값은 없었습니다.

## 참고

- 볼트에서 `2. Wiki/AA Files (AAF).md`의 수정 시각이 최근 1시간 이내입니다. 제 스크립트는 볼트에 쓰지 않으므로 다른 곳(Obsidian/iCloud)의 수정입니다. 변환은 현재 내용 기준으로 했습니다.
- 복사본은 속성 순서를 목표 순서로 재배열합니다. `Orientation`, `Academy`, `Language`는 지시대로 값을 링크로 바꾸지 않았습니다.