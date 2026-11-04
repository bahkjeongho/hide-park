import csv,sys
from rec import *
rows={r[0]:r for r in list(csv.reader(open(D+"manual-check-Park.csv",encoding="utf-8-sig")))[1:]}
def norm(u): return u if u.endswith("/") else u+"/"
def wk(r):
    d=r[3].replace("en.wikipedia.com","en.wikipedia.org")
    return [d] if "wikipedia.org" in d or "namu.wiki" in d else []
def site(r):
    from urllib.parse import urlparse
    w=r[2]
    if not w: return ""
    p=urlparse(w); return f"{p.scheme}://{p.netloc}"
# user: (filename, aliases, cities, countries, korean tldr)  ; kind W=wiki A=artist
E_={
"hikingpatrol":("Hiking Patrol",["HIKING PATROL"],[],["Norway"],"Wai Tsui가 설립한 노르웨이 의류 브랜드"),
"ysl":("Saint Laurent",["SAINT LAURENT","Saint Laurent Paris","Yves Saint Laurent"],["Paris"],["France"],"1961년 설립된 프랑스 패션 하우스, Kering 소유"),
"10corsocomo":("10 Corso Como",[],["Milan"],["Italy"],"밀라노의 컨셉 스토어"),
"10corsocomoseoul":("10 Corso Como Seoul",[],["Seoul"],["South Korea"],"2008년 청담에 문을 연 10 Corso Como 서울 매장"),
"augustbarron":("August Barron",["ALL–IN magazine"],[],[],"ALL–IN 매거진과 연관된 크리에이터"),
"annieleibovitz":("Annie Leibovitz",[],[],["USA"],"미국 인물 사진가"),
"another_man":("AnOther Man",["AnOther Man Magazine"],["London"],["UK"],"2005년 창간한 Dazed Media의 남성 패션 매거진"),
"apartamentomagazine":("Apartamento",[],["Barcelona"],["Spain"],"2008년 바르셀로나에서 창간한 인테리어 매거진"),
"artpartner":("Art Partner",[],["New York"],["USA"],"1992년 Giovanni Testino가 설립한 뉴욕 에이전시"),
"artnet":("Artnet",[],[],[],"1989년 시작된 미술 시장 정보 사이트"),
"ashleywilliamslondon":("Ashley Williams",["ASHLEY WILLIAMS LONDON"],["London"],["UK"],"런던 기반 패션 디자이너"),
"bellahadid":("Bella Hadid",[],[],["USA"],"미국 모델"),
"bloombergbusiness":("Bloomberg Business",[],[],["USA"],"Bloomberg의 비즈니스 뉴스 브랜드"),
"bluenoterecords":("Blue Note Records",[],[],["USA"],"1939년 창립된 재즈 레이블"),
"bode":("Bode",["BODE"],["New York"],["USA"],"2016년 Emily Adams Bode가 설립한 뉴욕 브랜드"),
"casamagazinesnyc":("Casa Magazines",["CASA MAGAZINES NYC"],["New York"],["USA"],"웨스트빌리지의 매거진 전문 서점"),
"chiomannadi":("Chioma Nnadi",["chioma nnadi"],[],["UK"],"British Vogue의 편집 총괄"),
"kidsuper":("KidSuper",["Colm Dillane"],["New York"],["USA"],"Colm Dillane이 설립한 브루클린 브랜드"),
"corteiz":("Corteiz",["CORTEIZ"],["London"],["UK"],"런던 기반 스트리트웨어 브랜드"),
"craig__green":("Craig Green",["CRAIG GREEN"],["London"],["UK"],"2012년 설립된 영국 패션 디자이너 브랜드"),
"danielroseberry":("Daniel Roseberry",[],[],["USA"],"Schiaparelli의 아티스틱 디렉터"),
"davemeyers":("Dave Meyers",[],[],["USA"],"뮤직비디오 감독"),
"derekblasberg":("Derek Blasberg",["Derek C. Blasberg"],[],["USA"],"패션 작가이자 에디터"),
"dionlee":("Dion Lee",["DION LEE"],["Sydney"],["Australia"],"시드니 출신 디자이너와 그의 브랜드"),
"wordimagetext":("Emmanuel Olunkwa",[],[],[],"November의 Founder & Publisher"),
"evachen212":("Eva Chen",[],[],["USA"],"전 Lucky 편집장이자 Instagram 패션 파트너십 총괄"),
"gentlemonster":("Gentle Monster",["GENTLE MONSTER","젠틀몬스터"],["Seoul"],["South Korea"],"2011년 설립된 한국 아이웨어 브랜드"),
"walesbonner":("Wales Bonner",["Grace Wales Bonner"],["London"],["UK"],"2014년 Grace Wales Bonner가 설립한 런던 레이블"),
"gus_van_sant":("Gus Van Sant",[],[],["USA"],"미국 영화감독"),
"yanghaegue":("양혜규",["Haegue Yang"],[],["South Korea"],"한국 현대미술 작가"),
"henrikvibskov":("Henrik Vibskov",[],["Copenhagen"],["Denmark"],"덴마크 디자이너이자 아티스트"),
"heromag":("Hero Magazine",["HERO MAGAZINE"],["London"],["UK"],"런던 패션 매거진"),
"highsnobiety":("Highsnobiety",["HIGHSNOBIETY"],["Berlin"],["Germany"],"2005년 David Fischer가 설립한 베를린 기반 매체"),
"hypebeast":("Hypebeast",["HYPEBEAST"],["Hong Kong"],["Hong Kong"],"2005년 Kevin Ma가 설립한 홍콩 미디어"),
"hystericglamour_tokyo":("Hysteric Glamour",["HYSTERIC GLAMOUR","ヒステリックグラマー"],["Tokyo"],["Japan"],"1984년 설립된 도쿄 패션 브랜드"),
"idea.ltd":("IDEA",["IDEA Books"],["London"],["UK"],"런던 소호의 희귀서적 서점"),
"interviewmag":("Interview Magazine",["Interview"],["New York"],["USA"],"1969년 Andy Warhol이 창간한 매거진"),
"isywod":("Issy Wood",[],["London"],["UK"],"화가이자 음악가"),
"jadedldn":("Jaded London",["JADED LONDON"],["London"],["UK"],"영국 스트리트웨어 브랜드"),
"jamesturell":("James Turrell",[],[],["USA"],"미국 빛 예술가"),
"jamie.hawkesworth":("Jamie Hawkesworth",[],[],["UK"],"영국 패션·다큐멘터리 사진가"),
"jw_anderson":("JW Anderson",["JW ANDERSON"],["London"],["UK"],"2008년 Jonathan Anderson이 설립한 패션 브랜드"),
}
ARTISTS={
"bassvictim":("Bassvictim",["bassvictim"],["London"],["UK"]),
"betcover_official":("Betcover!!",["betcover!!","柳瀬二郎"],["Tokyo"],["Japan"]),
"dg_bladee":("Bladee",["ƎE","BladeeCity"],[],["Sweden"]),
"clipse":("Clipse",[],[],["USA"]),
"esdeekid":("EsDeeKid",[],["Liverpool"],["UK"]),
"fakemink":("Fakemink",[],[],[]),
"fourtetkieran":("Four Tet",["Kieran Hebden"],["London"],["UK"]),
"kuma_power":("Hikaru Utada",["宇多田ヒカル","우타다 히카루"],[],["Japan"]),
}
ALL=list(E_)+list(ARTISTS)
def make():
    n=0;skip=[]
    for u in E_:
        fn,al,ci,co,tl=E_[u]; r=rows[u]
        if exists(fn): skip.append(fn);continue
        mknote(fn,al,[],norm(r[1]),website=site(r),urls=[],wikis=wk(r),cities=ci,countries=co,tldr=tl);n+=1
    for u,(fn,al,ci,co) in ARTISTS.items():
        r=rows[u]
        if exists(fn): skip.append(fn);continue
        artist(fn,al,norm(r[1]),web=site(r),wikis=wk(r),cities=ci,countries=co);n+=1
    return n,skip
if __name__=="__main__":
    print(make())
    import csv as c
    w=c.writer(open(D+"park-done.csv","a",newline="",encoding="utf-8-sig"))
    for u in ALL:
        w.writerow([u,(E_.get(u) or ARTISTS[u])[0]+".md",2])
