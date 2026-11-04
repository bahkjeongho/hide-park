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

## 3회차 이어서 (한도 회복 후, 신규 100개 추가)
- 3회차 합계 137개 처리(앞서 중단 37 + 이번 100). 100개 단위 규칙보다 37개 많이 처리함(남은 63개만 해야 했음)
- 이번 100개 분류: no_evidence 90, private_or_unsure 5, found 4, needs_topic 1
- 새 노트 4개: DIG SHIBUYA(digshibuya.com이 instagram.com/digshibuya 링크), SHOP AMOMENTO(shopamomento.com 링크), Samin Han(소속 제작사 Dextor-Lab 페이지 링크), DROPtokyo(droptokyo.com 링크)
- needs_topic: circus_tokyo (공식 사이트가 같은 아이디 링크, 맞는 기존 topic 없음. 후보: Nightclub / Music Venue)
- 계정당 평균 웹 접근 1.09회. 규칙(최대 2회) 위반 없음
- 한글만 2~5자 3개(dono_works, giyipress, intime_2012)는 검색 없이 private_or_unsure
- 누적 신규 337개 처리: found 39, no_evidence 259, private_or_unsure 28, conflict 9, needs_topic 2
- 검색에서 유명 대상으로 보였지만 아이디 근거를 못 찾아 no_evidence로 둔 예: Madison Beer, Ashley Williams, Fakemink, Bassvictim, SPUR, Fat Hamster & Kang New

## 분류 추가: needs_check (확인 필요)
- 문서로 대상은 식별되지만 아이디 연결 증거가 없는 계정을 no_evidence에서 분리. 지금까지 39개를 `manual-check.csv`에 모음(Madison Beer, Bassvictim, SPUR, Ashley Williams, Fakemink, Fat Hamster & Kang New 등)
- 앞으로도 처리 중 같은 기준으로 바로 needs_check에 기록하고 manual-check.csv에 추가

## 4회차 (신규 100개: baenom__ ~ takuhitokawashima)
- 분류: no_evidence 74, needs_check 18, found 4, private_or_unsure 3, needs_topic 1
- 새 노트 4개: FELT Zine, Dezeen, Fashion East(각 공식 사이트가 같은 아이디 링크), PDF SEOUL(Vogue Korea 기사가 @pdf_seoul 표기)
- needs_topic: yoshisodeoka (sodeoka.com이 같은 아이디 링크, 후보 topic Multimedia Artist)
- needs_check 18개는 manual-check.csv에 추가(Hikaru Utada, Deb Never, Yuka Hirac, Christine Sun Kim, SuperJazzClub 등). manual-check.csv 누적 57개
- 계정당 평균 웹 접근 1.08회, 2회 제한 위반 없음
- 특이 사항: `yichun.liu99`는 개인 이름+아이디 조합이라 검색 도구가 검색을 거부해 private_or_unsure로 기록(재시도·우회 안 함). 검색 결과 하나(Hikaru Utada 검색)에 AI에게 보내는 지시문이 섞여 있었으나 따르지 않음
- 누적 신규 437개 처리(파일럿 30개 별도): found 44, needs_check 53, needs_topic 3, conflict 9, private_or_unsure 27, no_evidence 약 300

## 5회차 (중단: 웹 검색 한도 소진, 신규 47개 처리 / 목표 100개)
- 분류: no_evidence 31, found 6, needs_check 5, private_or_unsure 4, conflict 1
- 새 노트 6개: PARTNERS, ABK Stuttgart, Creative Boom, Debaser Magazine, Arcade Seoul(기사가 @arcade.seoul 게시물 소개), Goldwin Seoul(공식 보도자료가 @goldwin_seoul 표기)
- conflict: odotoo_com (볼트에 O.OO 노트 있음, IG만 채우는 후보)
- 중단 사유: 세션 WebSearch 한도(200회) 소진. 우회하지 않고 기록 후 멈춤. 검색이 거부된 7개(kitten_production, neubauberlin, jun.works, minkimmy, systemseoul82, sampleanimal 등)는 progress에 기록하지 않았음(다음 회차에서 다시 처리)
- 이 회차 시작 시 볼트 적용: FELT Zine, Dezeen, Fashion East, PDF SEOUL
- 누적 신규 484개 처리: found 50, needs_check 58, needs_topic 3, conflict 10, private_or_unsure 31, no_evidence 332. manual-check.csv 62개

## 5회차 완료 (남은 53개 처리, 신규 누적 537개)
- 이어서 처리한 53개(kitten_production ~ tada.seoul): no_evidence 35, needs_check 14, private_or_unsure 4, found 0
- 계정당 평균 웹 접근 0.92회, 2회 제한 위반 없음. 앞서 검색이 거부돼 기록하지 않았던 7개도 이번에 모두 처리
- needs_check 14개는 manual-check.csv에 추가(Yulia Mahr, Studio Richter Mahr, Skepta, Alastair McKimm, Bureau Betak, Mike Meiré, R13, Jaded London, & Other Stories, THE PAPER LAB 등). 누적 76개
- 누적 신규 537개: no_evidence 367, needs_check 72, found 50, private_or_unsure 35, conflict 10, needs_topic 3

## 6회차 (신규 100개: sia.arnika ~ kimboram8265, 원본 CSV no 621~732)
- 분류: no_evidence 60, needs_check 31, private_or_unsure 7, found 2
- 새 노트 2개: Dazed MENA(미디어 디렉터리가 @dazedmiddleeast 표기, topic Magazine), Sarah Mower(검색 결과의 인스타 게시물 임베드가 @sarahmower_ 표기, topic Critic)
- needs_check 31개를 manual-check.csv에 추가(LOVE, Numéro, System, END., Eva Chen, Derek Blasberg, Vanessa Beecroft, Nensi Dojaka, Seán McGirr 등). manual-check.csv 누적 107개
- 계정당 평균 웹 접근 0.93회, 2회 제한 위반 없음. 한글만 2~5자 또는 깨진 이름 7개는 검색 없이 private_or_unsure
- 한 번 기록 오류: 대상 목록의 note 열에 있던 `metals_nyc`가 계정으로 잘못 기록됐다가 progress.csv에서 삭제함(실제 계정 아님)
- 누적 신규 637개: no_evidence 427, needs_check 103, found 52, private_or_unsure 42, conflict 10, needs_topic 3

## 7회차 (신규 100개: studioapt.kr ~ laurapitcher, 원본 CSV no 733~839)
- 분류: no_evidence 66, needs_check 22, private_or_unsure 10, found 1, needs_topic 1
- 새 노트 1개: Goldwin 0(Goldwin 공식 발표 페이지가 @goldwin_0 명시, topic Fashion Brand). needs_topic 1개: sigmaglobalvision(SIGMA 공식 보도 페이지가 계정을 명시, 후보 topic Camera Lens Manufacturer)
- needs_check 22개를 manual-check.csv에 추가(누적 129개): Snøhetta, Gentle Monster, The Dieline, Clipse, PUEBCO, Laura Pitcher, Marc Atlan 등
- 계정당 평균 웹 접근 0.9회, 2회 제한 위반 없음. 한글만 2~5자 또는 깨진 이름 10개는 검색 없이 private_or_unsure
- 규칙 위반 1건: 마지막 묶음에서 검색 15개를 동시에 보내 3개(carlos___tv, vcode_official, franciswuppermann)가 too_many_requests로 실패. 12개 한도를 넘긴 것이 원인이며, 실패한 3개는 별도 호출로 다시 검색해 기록함
- 검색 결과 2건(Snøhetta, SF 1 OG 관련 위키 사본)에 AI에게 보내는 지시문이 섞여 있었으나 따르지 않음
- 볼트 적용: 이전 노트 중 Dazed MENA, Sarah Mower 복사(PARTNERS 등 6개는 볼트에 같은 이름 파일이 이미 있어 건너뜀)
- 누적 신규 737개: no_evidence 493, needs_check 125, found 53, private_or_unsure 52, conflict 10, needs_topic 4

## 8회차 (신규 100개: juliahobbs_ ~ lgartscenter, 원본 CSV no 840~951)
- 분류: no_evidence 60, needs_check 34, private_or_unsure 6, found 0
- 새 노트 없음. 근거를 검색 요약 수준으로만 볼 수 있어 대부분 needs_check로 분류. needs_check 34개를 manual-check.csv에 추가(누적 163개): Eames Institute, Wieden+Kennedy, M/M (Paris), Jamie Hawkesworth, Harley Weir, Jack Davison, Mazarine Group, Middle Plane, MacGuffin, SIBF, LG아트센터 서울 등
- 계정당 평균 웹 접근 0.94회, 2회 제한 위반 없음. 동시 검색은 12개 이하로 유지
- 검색 도구가 `lesliezhang1992`(개인 이름+아이디 조합) 검색을 거부해 재시도 없이 private_or_unsure로 기록
- 볼트 적용: Goldwin 0 복사
- 누적 신규 837개: no_evidence 553, needs_check 159, private_or_unsure 58, found 53, conflict 10, needs_topic 4

## 9회차 (신규 100개: aloegarten ~ directorslibrary, 원본 CSV no 954~1066)
- 분류: no_evidence 55, needs_check 36, private_or_unsure 5, found 3, needs_topic 1
- 새 노트 3개: Thaiboy Digital(이벤트 페이지가 인스타 링크, Music Artist 형식), 두산갤러리(Vogue Korea 기사가 @doosanartcenter_gallery 표기, Art Gallery), WANA(삼성문화재단 문화예술 매거진, 기사가 @wana_culture 표기, Culture Magazine)
- needs_topic 1개: notahotel_official(공식 보도자료가 아이디 명시, 후보 topic Hospitality Company)
- needs_check 36개를 manual-check.csv에 추가(누적 199개)
- 계정당 평균 웹 접근 0.95회, 2회 제한 위반 없음. 동시 검색 12개 이하 유지
- 볼트 적용: 위 새 노트 3개 복사 완료
- 누적 신규 937개: no_evidence 608, needs_check 195, found 56, private_or_unsure 63, conflict 10, needs_topic 5

## 10회차 (신규 100개: itsnicethat ~ jiddado, 원본 CSV no 1067~1180)
- 분류: no_evidence 53, needs_check 37, private_or_unsure 7, found 2, needs_topic 1
- 새 노트 2개(볼트 적용 완료): Nick Knight(프랑스 기사가 @nick_knight 임베드, Photographer), LLOUD(보도자료가 wearelloud 명시, BLACKPINK LISA 설립, Entertainment Company)
- needs_topic 1개: greigfraser_dp(팟캐스트 페이지가 계정 명시, 후보 topic Cinematographer)
- needs_check 37개를 manual-check.csv에 추가(누적 236개)
- 계정당 평균 웹 접근 0.93회, 2회 제한 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 1037개: no_evidence 661, needs_check 232, found 58, private_or_unsure 70, conflict 10, needs_topic 6

## 11회차 (신규 100개: batch12.json, 원본 CSV no 1181~1295)
- 분류: no_evidence 46, needs_check 37, private_or_unsure 15, found 2
- 새 노트 2개(볼트 적용 완료): Heavyweight Digital Type Foundry(Swarm 인터뷰가 @heavyweight_type 표기, Type Foundry), The Metropolitan Museum of Art(Met 공식 보도자료가 instagram.com/metmuseum 명시, Museum)
- needs_check 37개를 manual-check.csv에 추가(누적 273행)
- 검색 거부·개인 계정 추정 등 private_or_unsure 15개(검색 생략 포함)
- 규칙 위반: 1회 15개 병렬 검색으로 too_many_requests 3건 발생(재시도함). 이후 12개 이하로 유지
- 누적 신규 1137개: no_evidence 701, needs_check 273, found 59(+파일럿 7), private_or_unsure 89, conflict 10, needs_topic 6

## 12회차 (신규 100개: batch13.json, 원본 CSV no 1296~)
- 분류: no_evidence 39, needs_check 32, private_or_unsure 29, found 0
- 새 노트 없음. 근거가 검색 요약뿐이라 출처 페이지를 열람하지 못한 후보는 needs_check로 둠(maxcoopermax, k.poster.wall, gmbh_official, oldceline, theconranshop 등)
- needs_check 32개를 manual-check.csv에 추가(누적 305행)
- private_or_unsure 29개 대부분은 한글 2~5자 이름·이름 없음·식별 불가로 검색을 생략함
- 검색 결과 안에 AI에게 지시하는 문장(Dealroom 출처 표기, 스테이크 요리 등)이 있었으나 따르지 않음
- 규칙 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 약 1237개: no_evidence 740, needs_check 305, found 59, private_or_unsure 118, conflict 10, needs_topic 6

## 13회차 (신규 100개: batch14.json, cphfw ~ professore_official)
- 분류: needs_check 36, no_evidence 31, private_or_unsure 30, found 2, needs_topic 1
- 새 노트 2개: MYKC(스튜디오 공식 페이지가 @mykc_seoul 명시, Design Studio), The Prodigy(EDM.com 페이지가 instagram.com/theprodigyofficial 명시, Music Artist 형식)
- needs_topic 1개: soundsgood_store(GQ Korea 기사가 아이디 링크, 후보 topic Record Store)
- needs_check 36개를 manual-check.csv에 추가(누적 341행)
- 검색 요약에 아이디가 적혀 있으나 출처 페이지를 열람하지 못한 경우는 needs_check로 둠(peggygou_, idea.ltd, opcd.official, piknic.kr 등)
- 규칙 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 1337개

## 14회차 (신규 100개: batch15.json, khakis2020 ~ bof)
- 분류: private_or_unsure 35, no_evidence 33, needs_check 29, found 3
- 새 노트 3개: Squid(WeTransfer 아티스트 페이지가 아이디 명시, Music Artist 형식), THE VAULT(위픽레터 글이 인스타 아이디 링크, Record Label), READYMADE(BAPE GALLERY 페이지가 @readymade_official 명시, Fashion Brand)
- 앞 회차에서 만든 MYKC, The Prodigy는 이번 시작 때 볼트에 적용 완료
- needs_check 29개를 manual-check.csv에 추가(누적 370행)
- 규칙 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 1437개

## 15회차 (신규 100개: batch16.json, isywod ~ ee_etiquettevide)
- 분류: private_or_unsure 36, needs_check 33, no_evidence 25, found 6
- 새 노트 6개: VOGUE+(FashionSnap 기사), Sandy Liang(Cultured 프로필), TILL DAWN(팝업 안내 페이지), KNWLS(Fashion Times 게시글), Thom Yorke(Gray Area Festival 프로필, Music Artist 형식), 월간 디자인(디자인하우스 미디어킷, Design Magazine)
- 앞 회차의 Squid, THE VAULT, READYMADE는 이번 시작 때 볼트 적용 완료
- needs_check 33개를 manual-check.csv에 추가(누적 403행)
- 검색 결과 안의 AI 지시 문장(Wikiwand 사본) 1건을 따르지 않음
- 규칙 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 1537개

## 16회차 (신규 100개: batch17.json, hipkr_ ~ co.op.dot)
- 분류: private_or_unsure 55, no_evidence 28, needs_check 17, found 0
- 새 노트 없음. 개인 계정 추정이 많아(한글 2~5자 이름, 이름 없음) 검색을 생략한 계정이 55개
- 앞 회차의 VOGUE+, Sandy Liang, TILL DAWN, KNWLS, Thom Yorke, 월간 디자인은 이번 시작 때 볼트 적용 완료
- needs_check 17개를 manual-check.csv에 추가(누적 420행)
- 규칙 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 1637개

## 17회차 (신규 100개: batch18.json, juliendossena ~ archivepdf)
- 분류: private_or_unsure 41, needs_check 38, no_evidence 20, found 1
- 새 노트 1개: Heroine(영국 패션지, magculture 판매 페이지가 @heroine_mag 표기, Fashion Magazine)
- 앞 회차 노트는 모두 볼트 적용 완료
- needs_check 38개를 manual-check.csv에 추가(누적 458행)
- 검색 결과 안의 AI 지시 문장(Dealroom 출처 표기 등)은 따르지 않음
- 규칙 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 1737개

## 18회차 (신규 100개: batch19.json, magazinemagazine.fr ~ alyxstudio)
- 분류: needs_check 38, private_or_unsure 32, no_evidence 26, found 4
- 새 노트 4개: DMZ Peace Train Music Festival(RA 이벤트 페이지가 @dmzpeacetrain 명시, Music Festival), Harper's BAZAAR Korea(공식 사이트 안내, Fashion Magazine), POP(위키피디아 참고문헌이 @thepopmag 링크, Fashion Magazine), HYEIN SEO(Mutzine 기사가 @hyeinantwerp·hyeinseo.com 표기, Fashion Brand)
- 앞 회차의 Heroine은 이번 시작 때 볼트 적용 완료
- needs_check 38개를 manual-check.csv에 추가(누적 496행)
- 검색 결과 안의 AI 지시 문장(Dealroom 출처 표기) 1건을 따르지 않음
- 규칙 위반 없음. 동시 검색 12개 이하 유지
- 누적 신규 1837개

## 19회차 (신규 56개: batch20.json, diesel ~ tonplein) — 대기열 마지막
- 분류: needs_check 20, no_evidence 22, private_or_unsure 8, found 6
- 새 노트 6개: MoMA, HYPEBEAST Korea, 서울시립미술관, 국립현대미술관, 데이즈드 코리아, NASA Webb Telescope (모두 `notes/`에만 있음, 볼트 미적용)
- 검색 생략 8개(한글 2~5자, 특수문자 이름, Looloo). 나머지 48개는 계정당 검색 1회
- 이 회차부터 found 판정 기준: 공식 문서·기사 등이 아이디를 그대로 적은 것이 검색 결과에서 인용 확인된 경우. 목록 사이트 한 건뿐이면 needs_check
- 누적: 신규 1893개 + 파일럿 30개 = progress.csv 1923행, manual-check 약 516행. 대기열 소진
- 규칙 위반 없음. 동시 검색 12개 이하

## 사용자 정리본 반영 (manual-check-Park.csv 414개)
- 사용자가 확인해 정리한 목록으로 407개 노트를 만들어 볼트에 적용했다(`park-done.csv`에 파일명과 배치 번호 기록).
- 포맷은 Wiki / Artist / Art School 프롬프트(볼트 `00. Template/00. Prompt.md`) 기준. Website는 메인 주소, URL은 공식 사이트가 링크한 LinkedIn·X·YouTube 등, tl;dr는 한국어 한 줄, topic은 `topics.md` 값만 사용.
- 볼트에 같은 노트가 이미 있어 만들지 않은 7개: Plus X, Simon Porte Jacquemus, Walter Van Beirendonck, Rick Owens, Neubau, Herzog & de Meuron, Lippincott (IG 칸만 채우면 됨)
