import json,re,math,numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPoly
from pyproj import Transformer
from PIL import Image
T=Transformer.from_crs('EPSG:2180','EPSG:4326',always_xy=True)
LAT1,LON1,LAT2,LON2=52.0451,15.0943,52.0474,15.0977   # WMS 1.3.0 EPSG:4326 = lat_min,lon_min,lat_max,lon_max
W=1600
def px(lon,lat): return ((lon-LON1)/(LON2-LON1)*W, (LAT2-lat)/(LAT2-LAT1)*W)
def ring(w):
    m=re.search(r'\(\(([^()]*)\)',w); return [tuple(map(float,q.split())) for q in m.group(1).split(',')]
par=[T.transform(*p) for p in ring(json.load(open('parcel_wkt.json'))['wkt'])]
bl={k:[T.transform(*p) for p in ring(v['wkt'])] for k,v in json.load(open('buildings.json')).items()}
osm=[e for e in json.load(open('../bad/bld.json'))['elements']]
wat=json.load(open('osm_water.json'))['elements']
im=np.array(Image.open('ortho_wide.jpg'))
fig,ax=plt.subplots(figsize=(13,13))
ax.imshow(im,extent=[0,W,W,0])
ax.set_xlim(0,W); ax.set_ylim(W,0)
for e in osm:
    g=e.get('geometry') or []
    if not g: continue
    pts=[px(p['lon'],p['lat']) for p in g]
    ax.add_patch(MPoly(pts,closed=True,facecolor=(1,1,1,.06),edgecolor='white',lw=1,alpha=.85))
    hn=e['tags'].get('addr:housenumber')
    if hn:
        ax.text(sum(p[0] for p in pts)/len(pts),sum(p[1] for p in pts)/len(pts),hn,ha='center',va='center',fontsize=9,color='white',weight='bold')
for e in wat:
    g=e.get('geometry') or []
    if not g or not e['tags'].get('name'): continue
    if e['tags']['name'] not in ('Grobla','Murna'): continue
    pts=[px(p['lon'],p['lat']) for p in g]
    ax.plot([p[0] for p in pts],[p[1] for p in pts],'-',color='#ffe14d',lw=2.5,alpha=.9)
    ax.text(pts[len(pts)//2][0],pts[len(pts)//2][1],e['tags']['name'],fontsize=11,color='#ffe14d',rotation=74)
ax.add_patch(MPoly([px(*p) for p in par],closed=True,facecolor=(0,1,0,.08),edgecolor='#19ff7a',lw=3))
names={'080206_4.0002.92_BUD':('GROBLA 64','121,0 m²','EGiB 92_BUD'),
       '080206_4.0002.921_BUD':('HALA','187,5 m²','EGiB 921_BUD')}
for bid,v in bl.items():
    pts=[px(*p) for p in v]
    ax.add_patch(MPoly(pts,closed=True,facecolor=(1,0.1,0,.30),edgecolor='red',lw=3))
    cx=sum(p[0] for p in pts)/len(pts); cy=sum(p[1] for p in pts)/len(pts)
    n,a,sub=names[bid]
    ax.text(cx,cy-14,n,ha='center',fontsize=15,color='white',weight='bold')
    ax.text(cx,cy+8,a,ha='center',fontsize=14,color='white')
    ax.text(cx,cy+30,sub,ha='center',fontsize=9,color='white',style='italic')
ppm=W/((LON2-LON1)*111320*math.cos(math.radians(52.046)))
sb=25*ppm
ax.add_patch(MPoly([[60,W-100],[60+sb,W-100],[60+sb,W-114],[60,W-114]],closed=True,facecolor='white',edgecolor='black'))
ax.text(60+sb/2,W-130,'25 m',ha='center',fontsize=12,color='white',weight='bold')
ax.annotate('N',xy=(W-70,80),xytext=(W-70,180),ha='center',fontsize=17,color='white',weight='bold',
            arrowprops=dict(arrowstyle='-|>',color='white',lw=3))
ax.text(55,60,'dz. ew. 61/6  ·  1 684,6 m²',fontsize=15,color='#19ff7a',weight='bold')
ax.text(55,90,'granice i obrysy: EGiB (ULDK/GUGiK)  ·  podkład: ortofoto GUGiK  ·  skala ~1:800',fontsize=9,color='white')
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_color('black')
plt.tight_layout(pad=0)
plt.savefig('plan_egib.png',dpi=150,bbox_inches='tight',pad_inches=0)
print('ok')
