import json,re,math,numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPoly
from pyproj import Transformer
from PIL import Image
T=Transformer.from_crs('EPSG:2180','EPSG:4326',always_xy=True)
LAT1,LON1,LAT2,LON2=52.0451,15.0943,52.0474,15.0977; W=1600
def px(lon,lat): return ((lon-LON1)/(LON2-LON1)*W,(LAT2-lat)/(LAT2-LAT1)*W)
def ring(w):
    m=re.search(r'\(\(([^()]*)\)',w); return [tuple(map(float,q.split())) for q in m.group(1).split(',')]
def dash(w):  # 2180 -> lonlat
    return [T.transform(*p) for p in ring(w)]
p6=dash(json.load(open('parcel_wkt.json'))['wkt'])
p4=dash(open('p61_4.wkt').read())
b92=dash(json.load(open('b_92_BUD.json'))['wkt'])
b921=dash(json.load(open('b_921_BUD.json'))['wkt'])
b920=dash(json.load(open('b_920_BUD.json'))['wkt'])
osm=[e for e in json.load(open('../bad/bld.json'))['elements']]
im=np.array(Image.open('ortho_wide.jpg'))

# ---------- FIG A: annotated ortho ----------
fig=plt.figure(figsize=(11,11)); ax=fig.add_axes([0,0,1,1])
ax.imshow(im)
for e in osm:
    g=e.get('geometry') or []
    if not g: continue
    pts=[px(p['lon'],p['lat']) for p in g]
    ax.add_patch(MPoly(pts,closed=True,fill=False,edgecolor='white',lw=1.1,alpha=.75))
    hn=e['tags'].get('addr:housenumber')
    if hn: ax.text(sum(p[0] for p in pts)/len(pts),sum(p[1] for p in pts)/len(pts),hn,ha='center',va='center',fontsize=9,color='white',weight='bold')
ax.add_patch(MPoly([px(*p) for p in p6],closed=True,fill=False,edgecolor='#19ff7a',lw=3.2))
ax.add_patch(MPoly([px(*p) for p in p4],closed=True,fill=False,edgecolor='#ffd23f',lw=2.6,ls=(0,(6,4))))
ax.add_patch(MPoly([px(*p) for p in b92],closed=True,facecolor=(1,0,0,.25),edgecolor='#ff2b2b',lw=2.6))
ax.add_patch(MPoly([px(*p) for p in b921],closed=True,facecolor=(1,0,0,.25),edgecolor='#ff2b2b',lw=2.6))
ax.add_patch(MPoly([px(*p) for p in b920],closed=True,facecolor=(1,0.55,0,.22),edgecolor='#ff2b2b',lw=2.6,ls=(0,(5,3))))
def txt(poly,s,col='white',dy=0):
    q=[px(*p) for p in poly]; cx=sum(a for a,b in q)/len(q); cy=sum(b for a,b in q)/len(q)
    ax.text(cx,cy+dy,s,ha='center',va='center',color=col,fontsize=10.5,weight='bold',
            bbox=dict(boxstyle='round,pad=0.25',fc=(0,0,0,.55),ec='none'))
txt(b920,'HALA — cz. N\n216,4 m²\n(dz. 61/4)',dy=-18)
txt(b921,'HALA — cz. S\n187,5 m²\n(dz. 61/6)',dy=14)
txt(b92,'GROBLA 64\n121,0 m²',dy=-4)
q=[px(*p) for p in p6]; cx=sum(a for a,b in q)/len(q); cy=sum(b for a,b in q)/len(q)
ax.text(cx-40,cy+150,'dz. 61/6 — 1 684,6 m²',color='#19ff7a',fontsize=12,weight='bold',bbox=dict(boxstyle='round,pad=0.3',fc=(0,0,0,.55),ec='none'))
q4=[px(*p) for p in p4]; ax.text(sum(a for a,b in q4)/len(q4)+120,sum(b for a,b in q4)/len(q4)-60,'dz. 61/4 — 1 421,5 m²',color='#ffd23f',fontsize=11,weight='bold',bbox=dict(boxstyle='round,pad=0.3',fc=(0,0,0,.55),ec='none'))
ppm=W/((LON2-LON1)*111320*math.cos(math.radians(52.046)))
sb=25*ppm
ax.add_patch(MPoly([[70,W-120],[70+sb,W-120],[70+sb,W-136],[70,W-136]],closed=True,facecolor='white',edgecolor='black'))
ax.text(70+sb/2,W-155,'25 m',ha='center',fontsize=12,color='white',weight='bold')
ax.annotate('N',xy=(W-80,90),xytext=(W-80,190),ha='center',fontsize=16,color='white',weight='bold',arrowprops=dict(arrowstyle='-|>',color='white',lw=3))
ax.text(330,880,'granice i obrysy budynków: EGiB (ULDK/GUGiK)  ·  podkład: ortofoto GUGiK 2024/25  ·  kadr ok. 230 × 255 m',fontsize=9.5,color='white',bbox=dict(boxstyle='round,pad=0.3',fc=(0,0,0,.5),ec='none'))
ax.set_xlim(250,1050); ax.set_ylim(910,400)
ax.set_xticks([]); ax.set_yticks([])
plt.savefig('fig_plan_ortho.jpg',dpi=150,facecolor='black')
print('A ok')

# ---------- FIG B: clean vector outline 1:200 ----------
def m2loc(poly,ox,oy):  # 2180 already metres -> shift
    return [(x-ox,y-oy) for x,y in ring(poly)] if False else None
# use 2180 metres
def wr(w): return ring(w)
P6=wr(json.load(open('parcel_wkt.json'))['wkt']); P4=wr(open('p61_4.wkt').read())
B92=wr(json.load(open('b_92_BUD.json'))['wkt']); B921=wr(json.load(open('b_921_BUD.json'))['wkt']); B920=wr(json.load(open('b_920_BUD.json'))['wkt'])
ox,oy=232345,471630
def sh(p): return [(x-ox,y-oy) for x,y in p]
fig,ax=plt.subplots(figsize=(12,10))
ax.add_patch(MPoly(sh(P6),closed=True,fill=False,edgecolor='#1b7f3b',lw=2))
ax.add_patch(MPoly(sh(P4),closed=True,fill=False,edgecolor='#b58500',lw=1.6,ls=(0,(6,4))))
for B,c in ((B920,'#c96b00'),(B921,'#c22'),(B92,'#c22')):
    ax.add_patch(MPoly(sh(B),closed=True,facecolor='#d9d9d9',edgecolor=c,lw=1.4))
# hatch
for B in (B920,B921,B92):
    ax.add_patch(MPoly(sh(B),closed=True,fill=False,hatch='///',edgecolor='#888',lw=0))
lbl=[(B920,'HALA  cz. N  216,4 m²'),(B921,'HALA  cz. S  187,5 m²'),(B92,'GROBLA 64  121,0 m²')]
for B,s in lbl:
    q=sh(B); ax.text(sum(a for a,b in q)/len(q),sum(b for a,b in q)/len(q),s,ha='center',fontsize=9,weight='bold')
ax.text(15,10.5,'dz. 61/6  (1 684,6 m²)',color='#1b7f3b',fontsize=10,weight='bold')
ax.text(24,78,'dz. 61/4  (1 421,5 m²)',color='#b58500',fontsize=10,weight='bold')
ax.text(28,2.6,'ul. Grobla →',fontsize=9,color='#555')
ax.annotate('',xy=(52,4.2),xytext=(44,4.2),arrowprops=dict(arrowstyle='->',lw=1))
ax.annotate('',xy=(3,72),xytext=(3,62),arrowprops=dict(arrowstyle='-|>',lw=2,color='black'))
ax.text(3.5,75,'N',fontsize=12,weight='bold')
ax.plot([12,32],[24,24],'-',color='black',lw=3); ax.text(13,25.4,'20 m',fontsize=9)
ax.set_aspect('equal'); ax.grid(alpha=.25,ls=':'); ax.set_xlabel('m'); ax.set_ylabel('m')
ax.set_title('Obrysy budynków i granice działek — rzut poziomy, dane EGiB (bez podkładu)',fontsize=11)
plt.tight_layout(); plt.savefig('fig_obrys.jpg',dpi=160)
print('B ok')
