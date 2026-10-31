import urllib.request, re, time, json, math
def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as r:
                return r.read().decode()
        except Exception as e:
            time.sleep(1.5)
    return ''
def wkt(url):
    s=get(url).strip().split('\n',1)
    if len(s)<2 or not s[0].strip().startswith('0'): return None
    return s[1].strip()
def ring(w):
    m=re.search(r'\(\(([^()]*)\)',w)
    return [tuple(map(float,p.split())) for p in m.group(1).split(',')]
def area(pts):
    return abs(sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts))))/2

PARCEL='080206_4.0002.61/6'
pw=wkt(f'https://uldk.gugik.gov.pl/?request=GetParcelById&id={PARCEL}&result=geom_wkt')
pp=ring(pw)
json.dump({'wkt':pw},open('parcel_wkt.json','w'))
print('PARCEL', PARCEL, 'area m2 =', round(area(pp),1), 'verts',len(pp))
xs=[p[0] for p in pp]; ys=[p[1] for p in pp]
print('bbox', round(min(xs),1),round(min(ys),1),round(max(xs),1),round(max(ys),1))

def inside(x,y,poly):
    c=False
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]; x2,y2=poly[(i+1)%n]
        if ((y1>y)!=(y2>y)) and (x < (x2-x1)*(y-y1)/(y2-y1)+x1): c=not c
    return c

found={}
step=3.0
x=min(xs)
while x<=max(xs):
    y=min(ys)
    while y<=max(ys):
        if inside(x,y,pp):
            s=get(f'https://uldk.gugik.gov.pl/?request=GetBuildingByXY&xy={x:.2f},{y:.2f}&srid=2180&result=id')
            ln=s.strip().split('\n')
            for line in ln:
                for bid in re.findall(r'080206_4\.0002\.[0-9A-Za-z/_]+_BUD', line):
                    found.setdefault(bid,[]).append((x,y))
        y+=step
    x+=step
print('buildings found:',len(found))
out={}
for bid,pts in found.items():
    bw=wkt(f'https://uldk.gugik.gov.pl/?request=GetBuildingById&id={bid}&result=geom_wkt')
    if not bw: print('  no geom',bid); continue
    bp=ring(bw)
    out[bid]={'area':round(area(bp),1),'wkt':bw,'sample':pts[0],'nvert':len(bp)}
    print('  %-32s %8.1f m2  verts=%d' % (bid, out[bid]['area'], len(bp)))
json.dump(out,open('buildings.json','w'))
