import json,re
from mk_park import *
import park01
col={x["user"]:x for x in json.load(open("../work/collected.json"))}
KO={
"emuartspace":"서울 종로구의 독립영화 전용관이자 아트 스페이스",
"gareth_wrighton":"런던 기반 아트 디렉터",
"berlinphotobookdistribution":"베를린과 서울을 기반으로 한 사진집 출판·유통 브랜드",
"workbyworks":"Works의 공동 창업자이자 그래픽 디자이너",
"actualsource.work":"출판과 브랜드를 겸하는 Actual Source",
"grafik.media":"디자인 매거진 Grafik을 복간하는 프로젝트",
"antwerpfashionmasters":"안트베르펜 왕립예술학교 패션과 졸업 쇼",
"antwerpart":"2014년 시작된 안트베르펜 현대미술 비영리 단체",
"artinculture":"1999년 창간한 미술 월간지",
"okulo_magazine":"2016년 창간한 계간 영상비평지",
"fluks__":"브랜드와 음악 작업을 해온 크리에이티브 스튜디오",
"here.creative":"Dante Yun이 설립한 글로벌 크리에이티브 에이전시",
"artpapereditions":"겐트 기반 아트 출판사",
"ljbtnstudio":"2018년 설립된 파리 기반 크리에이티브 스튜디오",
"artreview_magazine":"런던 기반 현대미술 매거진",
"ob.scenefestival":"서울에서 매년 가을 열리는 현대미술 축제",
"awakenewyorkclothing":"Angelo Baque가 2012년 설립한 뉴욕 브랜드",
"sandoll.otf":"1984년 설립된 한국 폰트 파운드리",
"iannbooks":"2007년 문을 연 종로구 서점이자 출판사",
"bof":"Imran Amed가 2007년 설립한 패션 비즈니스 미디어",
"oio.studio":"Matteo Loglio와 Simone Rebaudengo가 2020년 설립한 런던 크리에이티브 스튜디오",
"aino.agency":"고텐부르크와 오슬로 기반 디지털 디자인 에이전시",
"lottavolkova":"러시아 출신 패션 스타일리스트",
"montana_colors":"1994년 바르셀로나에서 시작한 스프레이 페인트 브랜드",
"nensidojaka":"티라나 출생, 영국 기반 패션 디자이너이자 2021 LVMH Prize 수상자",
"ceciliebahnsen":"2015년 시작한 덴마크 디자이너 브랜드",
"cfda":"1962년 설립된 미국 디자이너 협회",
"stylenotcom":"Beka Gvishiani가 운영하는 패션 인스타그램 계정이자 브랜드",
"official_studiounravel":"서울 기반 인테리어 디자인 스튜디오",
"holographik.co":"자그레브 기반 브랜드·모션·디지털 스튜디오",
"linear_non":"유타 파크시티 기반 디자인·개발 스튜디오",
"caption.seoul":"서울의 아트 플랫폼",
"cphfw":"2006년 시작된 코펜하겐 패션위크",
"coperni":"Sébastien Meyer와 Arnaud Vaillant가 2013년 설립한 파리 레이블",
"campbellhaybranding":"2004년 설립된 런던 기반 브랜딩 에이전시",
"plusx_creative":"2010년 설립된 서울 기반 BX·UX 디자인 에이전시",
"paju.typography.institute":"안상수가 설립한 파주 기반 디자인 학교",
"dampmagazines":"Substack 기반 매거진 아카이브",
"michelgaubert":"프랑스 사운드 디렉터이자 리믹서",
"yoshiyukiokuyama":"1991년 도쿄 출생 사진가이자 영화감독",
"comet_magazine":"도쿄 YAMEPI가 이끄는 컬처 매거진",
"denimtears":"Tremaine Emory가 설립한 패션 브랜드",
"sangnok.kr":"북디자이너 함지은의 디자인 스튜디오",
"lgartscenter":"LG연암문화재단이 운영하는 서울 마곡의 공연장",
"unlimited_edition_seoul":"2009년 시작된 서울 아트북 페어",
"kuo__duo":"2021년 설립된 서울 기반 3D 디자인 스튜디오",
"designfestival.kr":"월간 디자인이 주관하는 서울 디자인 페스티벌",
"typography_seoul":"윤디자인그룹 계열의 타입·타이포그래피 매체",
"marcatlandesign":"로스앤젤레스 기반 크리에이티브 디렉터",
"districtvision":"Tom Daly와 Max Vallot이 2016년 설립한 아이웨어 브랜드",
}
SKIP=("cargoworld","/p/","jbtalbourdet","wepro","croissant","peach_prodigy","ddungsang","patislow","shop.","hl=en")
def links(u):
    c=col[u]; out=[]
    for s in c["soc"]:
        if "instagram" in s: continue
        s=s.split("?")[0].rstrip("/") if "linkedin" in s else s
        if any(k in s for k in SKIP) or s in out: continue
        out.append(s)
    # one linkedin only
    li=[s for s in out if "linkedin" in s][:1]
    return [s for s in out if "linkedin" not in s]+li
made=0
for u,(fn,al,tp,ci,co,tl) in park01.E_.items():
    r=rows[u]; ig=r[1] if r[1].endswith("/") else r[1]+"/"
    t=open("notes/"+fn+".md",encoding="utf-8").read()
    web=(re.search(r"Website:\n  - (\S+)",t) or [None,""])[1]
    if u=="antwerpfashionmasters": pass
    mknote(fn,al,tp,ig,website=web,urls=links(u),cities=ci,countries=co,tldr=KO[u])
    made+=1
print(made)
