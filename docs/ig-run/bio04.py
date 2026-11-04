import csv,json,os,urllib.parse as up
from rec import mknote,D
S="/private/tmp/claude-503/-Users-parkjeongho-Developer-Hide-Park/873d87db-505a-43d5-8e4c-ad9523e833cb/scratchpad/"
R={o['u']:o for o in json.load(open(S+"f_300.json"))}
BATCH=4
def site(u):
    p=up.urlparse(R[u]['url']); return f"{p.scheme}://{p.netloc}/"
# u: (파일명, aliases, topics, cities, countries, tldr, website(None=사이트 루트, ''=없음))
N={
"p_____andrade":("P. Andrade",["P. ANDRADE"],["Fashion Brand"],[],["Brazil"],"Pedro Andrade와 Paula Kim의 브라질 남성복 브랜드",None),
"fontsfromfolch":("Fonts From Folch",["FFF"],["Type Foundry"],[],[],"리테일과 커스텀 서체를 제공하는 디지털 타입 파운드리",None),
"daisy_chain_studio":("Daisy Chain Studio",["Daisy Chain"],["Design Studio"],[],[],"Harry Butt와 Connor Campbell이 공동 디렉팅하는 모션 스튜디오",None),
"directorslibrary":("DIRECTORS' LIBRARY",["Directors Library"],["Media Platform"],[],[],"영화·영상·크리에이티브 산업을 위한 독립 플랫폼이자 자료실",None),
"a_new_plane":("A New Plane",[],["Creative Studio"],[],[],"Nick Knight와 Tom Wandrag가 설립한 크리에이티브 테크놀로지 스튜디오",None),
"calumkingsleyknight":("Calum Knight",[],["Creative Director"],[],[],"브랜드 아이덴티티를 위한 비주얼 월드와 장기 크리에이티브 전략을 만드는 크리에이티브 디렉터",None),
"ourspecialsupport":("OSS",["Our Special Support"],["Creative Production"],["Seoul"],["South Korea"],"서울 기반 크리에이티브 프로덕션 및 아티스트 대리 에이전시",None),
"alvarogarciaruano":("Álvaro García Ruano",["Alvaro Garcia Ruano"],["Graphic Designer"],[],["Spain"],"로고, 아이덴티티, 브랜딩, 애니메이션, 패키징을 다루는 그래픽 디자이너",None),
"d_v_t_k":("DVTK",["D V T K"],["Creative Studio"],[],[],"Kim Boutin과 D. Broner가 2015년에 설립한 독립 크리에이티브 디렉션 스튜디오",None),
"ob.studio_":("OB Studio",["OB Studio®"],["Design Studio"],[],[],"브랜드를 위한 경험을 만드는 디자인·테크놀로지 스튜디오",None),
"servicecenter.kr":("Service Center",["서비스센터"],["Brand Consultancy"],[],["South Korea"],"이름, 언어, 그래픽, 공간까지 브랜드 오너 곁에서 전략을 세우는 브랜딩 스튜디오",None),
"segajivideo":("SEGAJI",["새가지","Segaji Video"],["Video Director"],[],["South Korea"],"뮤직비디오와 커머셜을 연출하는 영상 감독 그룹",None),
"n.a.y.e.o.n.k":("Nayeon Kim",[],["3D Artist"],[],[],"3D 그래픽과 애니메이션을 다루는 작업자",None),
"same_dust":("Same Dust",["쎄임더스트"],["Book Store"],[],["South Korea"],"희귀서와 사인본 등을 다루는 서점",None),
"stillnice_official":("STILL NICE",["스틸나이스"],["Fashion Retail"],[],["South Korea"],"위탁 판매, 중고 판매, 플리마켓, 팝업을 운영하는 굿트레이딩 레이블",None),
"collectiveb_official":("Collective B",[],["Brand Consultancy"],[],["South Korea"],"브랜드·커머셜 디자인 컨설팅",None),
"ragged_edge":("Ragged Edge",[],["Branding Agency"],[],[],"야심 찬 브랜드를 위한 글로벌 브랜딩 에이전시",None),
"anton_rahlwes":("Anton Rahlwes",[],["Writer"],["Berlin"],["Germany"],"디자인, 미학, 문화 담론을 다루는 베를린 기반 큐레이터이자 작가",None),
"rough_side":("rough side",["러프사이드"],["Fashion Brand"],[],["South Korea"],"러프사이드와 러프사이드 화이트라벨을 선보이는 일상복 브랜드",None),
"lcbx_tailormade_garments":("Lcbx",[],["Fashion Brand"],[],["South Korea"],"테일러 메이드 가먼츠 브랜드",None),
"shop__epp":("SHOP EPP",["샵이피피"],["Fashion Retail"],[],["South Korea"],"국내외 패션 라이프스타일 셀렉트숍",None),
"wnk__official":("W(N)K",["WNK","wink"],["Design Studio"],["Seoul"],["South Korea"],"아트와 기술을 결합하는 서울 기반 그래픽 디자인 스튜디오",None),
"charlie__chops":("Charlotte Rutherford",[],["Photographer","Video Director"],["Los Angeles"],["USA"],"LA 기반 사진가, 감독, 아티스트",None),
"studio.earthround":("EARTH ROUND",["EARTHROUND"],["Creative Production"],[],[],"크리에이티브 비주얼 프로덕션",None),
"_bouk_ra_":("Bouk Ra",[],["Graphic Designer"],["Paris"],["France"],"파리에서 활동하는 한국 출신 그래픽·타입 디자이너",None),
"dmymag":("DMY",[],["Record Label"],[],[],"아티스트가 음악으로 지속 가능한 수입을 얻도록 돕는 새로운 형태의 음악 회사",None),
"namacheko":("NAMACHEKO",[],["Fashion Brand"],[],[],"남성복을 선보이는 패션 브랜드",None),
"odlyworkshop":("ODLYWORKSHOP",["odlyworkshop"],["Fashion Brand"],[],[],"시즌 컬렉션을 선보이는 패션 브랜드",None),
"works.works":("WORKS",["워크스","WORKS 워크스"],["Design Studio"],["Seoul"],["South Korea"],"2012년부터 서울에서 그래픽 디자인, 시각 예술, 오브제 디자인을 다루는 스튜디오",None),
}
CHK={
"flower.in.the.ashes_official":"향수·오브제 브랜드, 맞는 topic 없음",
"undermoodfilm":"본문 정보 없음",
"papermanapp":"책 제작용 종이 사용량 계산기 앱, 맞는 topic 없음",
"jiddado":"공부와 활동 모임, 맞는 topic 없음",
"wardrobe.41":"쇼핑몰 이름만 있고 분야 설명 없음",
"goodmothersyndrome":"공식 온라인스토어, 분야 설명 없음",
"robert.mccombe":"바이오 링크가 Liinks 링크 모음, 대상 성격 불명",
"brands.in.motion":"사이트 글 페이지(Thoughts)뿐, 성격 불명",
"movieland.archive":"쇼핑몰형 사이트(NOW SHOWING 등), 성격 불명",
"oldprada":"바이오 링크가 PAPER 기사(패션 아카이브 인스타그램), 맞는 topic 불명",
"charlieconstantinou":"SHOP·STOCKISTS만 있고 분야 설명 없음",
"pick.service":"stibee 뉴스레터 페이지, 성격 불명",
}
def w(path,row,head):
    new=not os.path.exists(D+path)
    with open(D+path,"a",encoding="utf-8-sig",newline="") as f:
        c=csv.writer(f)
        if new: c.writerow(head)
        c.writerow(row)
for u,v in N.items():
    fn,al,tp,ci,co,tl,web=v
    web=site(u) if web is None else web
    mknote(fn,al,tp,f"https://www.instagram.com/{u}/",website=web,cities=ci,countries=co,tldr=tl)
    w("bio-done.csv",[u,fn+".md",BATCH],["username","노트 파일","배치"])
for u,why in CHK.items():
    o=R[u]; w("manual-check-3.csv",[u,f"https://www.instagram.com/{u}/",o['n'],"사이트가 아이디를 링크함. "+why,o['url']],["username","인스타 주소","display_name","확인할 내용","바이오 링크"])
# 사이트가 아이디를 링크하지 않음 -> no-evidence-3, 열리지 않음 -> unverifiable-links
for u,o in R.items():
    if u in N or u in CHK: continue
    if 'err' in o: w("unverifiable-links.csv",[u,f"https://www.instagram.com/{u}/",o['n'],o['url'],o['err']],["username","인스타 주소","display_name","확인 못 한 링크","사유"])
    else: w("no-evidence-3.csv",[u,f"https://www.instagram.com/{u}/",o['n'],o['url'],o['title'][:60],"사이트가 이 인스타 아이디를 링크하지 않음"],["username","인스타 주소","display_name","바이오 링크","사이트 제목","사유"])
print(len(N),len(CHK))
