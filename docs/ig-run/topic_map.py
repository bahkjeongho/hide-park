import os,re,collections,csv
V='/Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park/2. Wiki/'
c=collections.Counter()
for f in os.listdir(V):
    if not f.endswith('.md'): continue
    t=open(V+f,encoding='utf-8').read()
    m=re.search(r'^topic:[ \t]*\n((?:[ \t]+-.*\n)+)',t,re.M)
    if not m or m.start()>t.find('\n---',4): continue
    c.update({re.sub(r'^\[\[(.*?)(\|.*)?\]\]$',r'\1',re.sub(r'^[ \t]+-[ \t]*','',l).strip().strip('"\'')) for l in m.group(1).splitlines()})
CAT={}
def add(cat,*fields):
    for x in fields: CAT[x]=cat
add('Design','Design','Graphic Design','Brand Design','Branding','Typography','Furniture','Furniture Design','Industrial Design','Product Design','Digital Design','Motion Design','Editorial Design','Book & Editorial Design','Type Design','Interior & Furniture Design','Space Design','Web & UI/UX','Creative','Creative Direction','Art Direction','Visual Direction','Architectural Design','Game Design','Lighting Design','Costume Design','Production Design','Industrial','Brand','3D Design','Animation Design')
add('Fashion','Fashion','Styling','Fashion Design','Textile Design','Hair','Luxury Goods')
add('Art','Art','Fine Art','Sculpture','Illustration','Media Art','Craft','Photography','Curating','Scenography','Comics')
add('Music','Music','Hip-Hop','K-Pop','Rock','Music Production','Audio Production','A&R','Singing')
add('Film','Film','Video','Animation','Production','Audio-visual Production','Video Production','Film Production','Cinematography','Acting','Screenwriting','Playwriting','Stage Management','Moving Image')
add('Architecture','Architecture','Interior Architecture')
add('Sports','Sports')
add('Media','Publishing','Editing','Journalism','Criticism','Writing','Fashion Journalism','Music Journalism','Podcast','Radio','Newspaper','Journal','Magazine')
add('Business','Marketing','Advertising','Consulting','PR','Brand Strategy','Investment','Management','Communication','Growth')
add('Tech','Tech','AI','Software','Programming','Engineering','Computer Science','Space','Spacecraft','Automobile','Instruments')
add('Culture','Culture','Philosophy','Sociology','Political Theory','Cultural Theory')
add('Entertainment','Entertainment')
TYPES=['Magazine','Studio','Agency','Brand','Company','Consultancy','Collective','Association','School','Award','Festival','Event','Critic','Editor','Director','Program','University','Museum','Gallery','Platform','Foundry','Label','Team','League','Firm','Office','Group','Store','Retail','Publisher','Producer','Designer','Photographer','Stylist','Architect','Writer','Curator','Artist','Idol','Band','DJ','Rapper','Prize','Week','Fair','Channel','Network','Marketplace','House','Journal','Newspaper','Radio','Podcast','Blogger','Youtuber','Engineer','Programmer','Entrepreneur','CEO','Investor','Philosopher','Sociologist','Journalist','Theorist','Scientist','Animator','Sculptor','Actor','Filmmaker','Tattooist','Strategist','Researcher','Maker','Operator','Venue','Team','Competition','Comptetition']
GROUP={'조직':{'Studio','Agency','Brand','Company','Consultancy','Collective','Association','Firm','Office','Group','Team','League','House','Label','Foundry','Store','Retail','Network','Venue'},
'직무':{'Director','Editor','Designer','Photographer','Stylist','Architect','Writer','Curator','Producer','Critic','Artist','Idol','Band','DJ','Rapper','Blogger','Youtuber','Engineer','Programmer','Entrepreneur','CEO','Investor','Philosopher','Sociologist','Journalist','Theorist','Scientist','Animator','Sculptor','Actor','Filmmaker','Tattooist','Strategist','Researcher','Maker','Operator'},
'매체':{'Magazine','Journal','Newspaper','Radio','Podcast','Channel','Publisher','Platform','Marketplace'},
'행사·상':{'Award','Festival','Event','Prize','Week','Fair','Competition','Comptetition'},
'교육·기관':{'School','University','Program','Museum','Gallery'}}
def grp(t):
    for g,s in GROUP.items():
        if t in s: return g
    return ''
OV={ # 직접 지정: 값:(Category,Field,Type,메모)
'Music Artist':('Music','','Artist',''),'K-Pop Idol':('Music','K-Pop','Idol',''),'K-Pop':('Music','K-Pop','','분야만 있음'),
'Design':('Design','Design','','분야만 있음'),'Fashion':('Fashion','Fashion','','분야만 있음'),'Media':('Media','','','Category 자체'),
'Sports':('Sports','Sports','','분야만 있음'),'Academic Program':('Education','','Program','분야 없음'),
'Creative Direction':('Design','Creative Direction','','분야만 있음'),'Photography':('Art','Photography','','Category가 Art인지 Photography인지 확인'),
'Video':('Film','Video','','분야만 있음'),'Music':('Music','Music','','분야만 있음'),'Film':('Film','Film','','분야만 있음'),
'Multidisciplinary':('','','','분류 불명'),'Entrepreneur':('Business','','Entrepreneur','직무·분야 없음'),'CEO':('Business','','CEO','직무·분야 없음'),
'Engineer':('Tech','Engineering','Engineer',''),'Producer':('','','Producer','분야 불명(음악/영상?)'),'Rapper':('Music','Hip-Hop','Rapper',''),
'DJ':('Music','','DJ',''),'Band':('Music','','Band',''),'Rock Band':('Music','Rock','Band',''),'Promoter':('Music','','Promoter','Type 목록에 없는 직무'),
'Record Label':('Music','','Label',''),'Type Foundry':('Design','Typography','Foundry',''),'Museum':('Art','','Museum',''),
'Art Platform':('Art','Art','Platform',''),'Art Gallery':('Art','Art','Gallery',''),'Art Collective':('Art','Art','Collective',''),
'Art Festival':('Art','Art','Festival',''),'Art Fair':('Art','Art','Fair',''),'Art Week':('Art','Art','Week',''),
'Book Store':('Media','Book','Store','Category 확인(Media/Retail)'),'Book':('Media','Book','',''),'Fashion Retail':('Fashion','Fashion','Retail',''),
'Fashion Platform':('Fashion','Fashion','Platform',''),'Media Platform':('Media','','Platform',''),'Music Platform':('Music','','Platform',''),
'Journal':('Media','','Journal',''),'Newspaper':('Media','','Newspaper',''),'Radio':('Media','','Radio',''),'Podcast':('Media','','Podcast',''),
'Video Channel':('Media','Video','Channel',''),'Media Company':('Media','','Company',''),'Media Design Program':('Education','Media Design','Program',''),
'Entertainment Company':('Entertainment','','Company',''),'Management Agency':('Entertainment','Management','Agency','Category 확인(Business?)'),
'Marketing':('Business','Marketing','',''),'Advertising':('Business','Advertising','',''),'Consulting':('Business','Consulting','',''),'Consulting Agency':('Business','Consulting','Agency',''),
'Marketing Agency':('Business','Marketing','Agency',''),'Marketing Company':('Business','Marketing','Company',''),'PR Agency':('Business','PR','Agency',''),
'Brand Consultancy':('Design','Brand Design','Consultancy','Category 확인(Business?)'),'Branding Agency':('Design','Brand Design','Agency','Category 확인(Business?)'),
'Brand Strategist':('Business','Brand Strategy','Strategist',''),'Creative Agency':('Design','Creative','Agency','Category 확인(Business?)'),
'Creative Production':('Film','Creative','Production','Production은 분야/유형 겹침'),'Creative Company':('Design','Creative','Company',''),
'Creative Group':('Design','Creative','Group',''),'Creative Team':('Design','Creative','Team',''),'Creative Office':('Design','Creative','Office',''),
'Creative Collective':('Design','Creative','Collective',''),'Creative Research':('Design','Creative','Research','Type 불명'),'Creative Label':('Design','Creative','Label',''),
'Creative Producer':('Design','Creative','Producer',''),'Creative Studio':('Design','Creative','Studio',''),'Creative Consultancy':('Design','Creative','Consultancy',''),
'Design Group':('Design','Design','Group',''),'Design Company':('Design','Design','Company',''),'Design Director':('Design','Design','Director',''),
'Production Company':('Film','Production','Company',''),'Production House':('Film','Production','House',''),'Production Studio':('Film','Production','Studio',''),
'Production Designer':('Film','Production Design','Designer',''),'Video Editor':('Film','Video','Editor',''),'Video Production':('Film','Video','Production','Production은 분야/유형 겹침'),
'Film Production':('Film','Film','Production','Production은 분야/유형 겹침'),'Audio-visual Production':('Film','Audio-visual','Production','Production은 분야/유형 겹침'),
'Audio-visual Maker':('Film','Audio-visual','Maker',''),'Animation Studio':('Film','Animation','Studio',''),'Animator':('Film','Animation','Animator',''),
'D.O.P.':('Film','Cinematography','D.O.P.',''),'EP':('Film','','Producer','Executive Producer로 추정'),'Screen Writer':('Film','Screenwriting','Writer',''),
'Actor':('Film','Acting','Actor',''),'Filmmaker':('Film','Film','Filmmaker',''),'Film Researcher':('Film','Film','Researcher',''),'Sound Director':('Film','Sound','Director',''),
'Moving Image Critic':('Film','Moving Image','Critic',''),'Film Critic':('Film','Film','Critic',''),'Film Magazine':('Media','Film','Magazine',''),
'Fashion Critique':('Media','Fashion','Critique','Critic과 같은 Type?'),'Fashion Critic':('Media','Fashion','Critic',''),'Fashion Director':('Fashion','Fashion','Director',''),
'Fashion Journalism':('Media','Fashion','Journalism','Type 불명'),'Music Journalism':('Media','Music','Journalism','Type 불명'),'Music Critique':('Media','Music','Critique','Critic과 같은 Type?'),
'Critique':('Media','','Critique','Critic과 같은 Type?'),'Critic':('Media','','Critic',''),'Culture Critic':('Media','Culture','Critic',''),'Literary Critic':('Media','Literature','Critic',''),'Art Critic':('Media','Art','Critic',''),
'Critique Magazine':('Media','','Magazine',''),'Blogger':('Media','','Blogger',''),'Youtuber':('Media','','Youtuber',''),'Journalist':('Media','Journalism','Journalist',''),
'Book Editor':('Media','Publishing','Editor',''),'Editorial Director':('Media','Editing','Director',''),'Editor':('Media','Editing','Editor',''),'Editor-in-Chief':('Media','Editing','Editor',''),
'Publisher':('Media','Publishing','Publisher',''),'Publishing Company':('Media','Publishing','Company',''),'Publishing Compnay':('Media','Publishing','Company','오타(Company로 이미 수정)'),
'Design Award':('Design','Design','Award',''),'Architecture Award':('Architecture','Architecture','Award',''),'Architecture Prize':('Architecture','Architecture','Prize',''),'Music Award':('Music','Music','Award',''),
'Comptetition':('','','Competition','오타(Competition), 분야 불명'),'Festival':('Culture','','Festival',''),'Event':('Culture','','Event',''),'Award':('Culture','','Award',''),'Association':('','','Association',''),'Collective':('','','Collective',''),'Consultancy':('Business','','Consultancy',''),'Company':('','','Company',''),'Agency':('Business','','Agency',''),'Studio':('','','Studio',''),'Brand':('','','Brand',''),'Director':('','','Director',''),'School':('Education','','School',''),'Production':('Film','Production','','분야/유형 겹침'),'Consulting':('Business','Consulting','',''),'Editing':('Media','Editing','',''),'Styling':('Fashion','Styling','',''),'Publishing':('Media','Publishing','',''),
'Music Genre':('Music','','','Genre 값'),'Space':('Tech','Space','','분류 불명'),'Space Design':('Design','Space Design','',''),'Spacecraft Company':('Tech','Space','Company',''),
'Human Network':('','','Network','분류 불명'),'Social Network':('Tech','','Network',''),'Communication':('Business','Communication','',''),'Commnications Group':('Business','Communication','Group','오타(Communications)'),
'Growth Invention Company':('Business','Growth','Company',''),'Hotel Company':('Business','Hotel','Company','신규 값'),'Luxury Goods Company':('Fashion','Luxury Goods','Company',''),'Automobile Company':('Tech','Automobile','Company',''),
'Instruments Company':('Music','Instruments','Company',''),'Font Marketplace':('Design','Typography','Marketplace',''),'Venue Operator':('Culture','','Operator',''),'Venue':('Culture','','Venue',''),
'Media Art':('Art','Media Art','',''),'Interior Architecture Company':('Architecture','Interior Architecture','Company',''),'Architecture Office':('Architecture','Architecture','Office',''),'Architecture Studio':('Architecture','Architecture','Studio',''),
'Architecture Firm':('Architecture','Architecture','Firm',''),'Architect':('Architecture','Architecture','Architect',''),'Architecture School':('Education','Architecture','School',''),'Architecture Magazine':('Media','Architecture','Magazine',''),
'Sports Team':('Sports','Sports','Team',''),'Sports League':('Sports','Sports','League',''),'Sports Magazine':('Media','Sports','Magazine',''),
'Design Studio':('Design','Design','Studio',''),'Design Agency':('Design','Design','Agency',''),'Design Festival':('Design','Design','Festival',''),'Design Week':('Design','Design','Week',''),'Design Association':('Design','Design','Association',''),'Design Magazine':('Media','Design','Magazine',''),
'Product Designer':('Design','Product Design','Designer',''),'Furniture Designer':('Design','Furniture Design','Designer',''),'Industrial Designer':('Design','Industrial Design','Designer',''),'Type Designer':('Design','Type Design','Designer',''),
'Graphic Designer':('Design','Graphic Design','Designer',''),'Hair Designer':('Fashion','Hair','Designer',''),'Set Designer':('Film','Set Design','Designer',''),'3D Designer':('Design','3D Design','Designer',''),
'3D Artist':('Art','3D','Artist',''),'Sculptor':('Art','Sculpture','Sculptor',''),'Curator':('Art','Curating','Curator',''),'Tattooist':('Art','Tattoo','Tattooist',''),
'Programmer':('Tech','Programming','Programmer',''),'Software Engineer':('Tech','Software','Engineer',''),'AI Engineer':('Tech','AI','Engineer',''),'Computer Scientist':('Tech','Computer Science','Scientist',''),'CTO':('Tech','','CTO','직무·분야 없음'),
'Software Company':('Tech','Software','Company',''),'AI Company':('Tech','AI','Company',''),'Tech Company':('Tech','Tech','Company',''),'Tech Product Company':('Tech','Tech','Company',''),'Tech Magazine':('Media','Tech','Magazine',''),'Tech':('Tech','Tech','',''),
'Philosopher':('Culture','Philosophy','Philosopher',''),'Sociologist':('Culture','Sociology','Sociologist',''),'Political Theorist':('Culture','Political Theory','Theorist',''),'Cultural Theorist':('Culture','Cultural Theory','Theorist',''),
'Culture Magazine':('Media','Culture','Magazine',''),'Culture Festival':('Culture','Culture','Festival',''),'Culture':('Culture','Culture','',''),'Investor':('Business','Investment','Investor',''),
'Web & UI/UX':('Design','Web & UI/UX','',''),'Singer-Songwriter':('Music','','Singer-Songwriter',''),'A&R':('Music','A&R','',''),'Music Producer':('Music','Music Production','Producer',''),'Music Critic':('Media','Music','Critic',''),
'Music Festival':('Music','Music','Festival',''),'Music Magazine':('Media','Music','Magazine',''),'Art Magazine':('Media','Art','Magazine',''),'Fashion Magazine':('Media','Fashion','Magazine',''),'Art School':('Education','Art','School',''),'University':('Education','','University',''),
'Managing Label':('Entertainment','Management','Label',''),'Photographer':('Art','Photography','Photographer','Category 확인'),'Stylist':('Fashion','Styling','Stylist',''),'Fashion Designer':('Fashion','Fashion Design','Designer',''),'Fashion Brand':('Fashion','Fashion','Brand',''),'Fashion Week':('Fashion','Fashion','Week',''),
'Creative Director':('Design','Creative Direction','Director',''),'Art Director':('Design','Art Direction','Director',''),'Visual Director':('Design','Visual Direction','Director',''),'Video Director':('Film','Video','Director',''),'Film Director':('Film','Film','Director',''),
'Digital Design':('Design','Digital Design','',''),'Motion Design':('Design','Motion Design','',''),'Product Design':('Design','Product Design','',''),'Typography':('Design','Typography','',''),'Editorial Design':('Design','Editorial Design','',''),'Graphic Design':('Design','Graphic Design','',''),'Furniture':('Design','Furniture','',''),'Furniture Design':('Design','Furniture Design','',''),'Brand Design':('Design','Brand Design','',''),'Industrial':('Design','Industrial','','분류 불명'),
'Book & Editorial Design':('Design','Book & Editorial Design','',''),'Art Direction':('Design','Art Direction','',''),'Visual Direction':('Design','Visual Direction','',''),'Creative':('Design','Creative','',''),
'Magazine':('Media','','Magazine',''),'Architecture':('Architecture','Architecture','',''),'Art':('Art','Art','',''),'Designer':('Design','','Designer','직무, 분야 없음'),'Writer':('Media','Writing','Writer',''),'Architectural Design':('Architecture','Architectural Design','',''),'Consultancy Collective':('Business','','Collective','Consultancy와 Collective 복합'),
}
rows=[]
for v,n in sorted(c.items(),key=lambda x:(-x[1],x[0])):
    if v in OV: cat,fld,typ,memo=OV[v]
    elif v.endswith(' Program'):
        fld=v[:-8]; cat,typ,memo='Education','Program',''
    else: cat=fld=typ=''; memo='자동 분류 실패'
    if v.startswith('http'): memo='topic에 URL이 들어간 입력 오류'
    if not cat and not memo: memo='분류 불명'
    rows.append([v,n,cat,fld,typ,grp(typ) if typ else '',memo])
with open('topic-classification.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f); w.writerow(['Topic(현재 값)','노트 수','Category','Field','Type','Type 구분','확인 필요 메모']); w.writerows(rows)
print(len(rows),'행; 자동실패',[r[0] for r in rows if r[6]=='자동 분류 실패'],'; 메모 있는 행',sum(1 for r in rows if r[6]))
print('Category',collections.Counter(r[2] for r in rows).most_common())
