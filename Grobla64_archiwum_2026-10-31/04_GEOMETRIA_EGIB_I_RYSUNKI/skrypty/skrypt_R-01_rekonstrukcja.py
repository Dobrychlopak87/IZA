import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patheffects as pe

h=[(0,0,6.5,4.0,'KASA · VORRAUM','26,0 m²','#cfe3ff'),
   (0,4.0,6.5,7.0,'WANNENB. I KL.','45,5 m²','#d8ecff'),
   (0,11.0,6.5,8.0,'WANNENB. II KL.','52,0 m²','#d8ecff'),
   (0,19.0,6.5,8.0,'BRAUSEBÄDER','52,0 m²','#cfe3ff'),
   (0,27.0,6.5,4.1,'DAMPFBAD','26,7 m²','#ffe0c2'),
   (6.5,0,6.5,7.0,'UMKLEIDEHALLE','45,5 m²','#e2e2f5'),
   (6.5,7.0,6.5,10.0,'WASCHANSTALT','65,0 m²','#d9f0d9'),
   (6.5,17.0,6.5,6.0,'KESSELHAUS','39,0 m²','#ffd6d6'),
   (6.5,23.0,6.5,4.0,'SKŁAD PALIWA','26,0 m²','#eeeeee'),
   (6.5,27.0,6.5,4.1,'WC · KORYTARZ','26,6 m²','#eeeeee')]
d=[(22,0,5.4,5.0,'POCZEKALNIA','27,0 m²','#cfe3ff'),
   (27.4,0,5.4,5.0,'MAGAZYN','27,0 m²','#eeeeee'),
   (22,5.0,5.4,6.3,'SIEDŹBA','34,0 m²','#e2e2f5'),
   (27.4,5.0,5.4,6.3,'MIESZKANIE','39,0 m²','#e2e2f5')]
fig,ax=plt.subplots(figsize=(13,8.4))
for (x,y,w,hh,name,area,col) in h+d:
    ax.add_patch(Rectangle((x,y),w,hh,facecolor=col,edgecolor='k',lw=1.5,alpha=.6))
    cx,cy=x+w/2,y+hh/2
    for dy,fs,txt in ((-0.55,9.4,name),(0.65,8.2,area)):
        t=ax.text(cx,cy-dy,txt,ha='center',va='center',fontsize=fs,weight='bold' if fs>9 else 'normal')
        t.set_path_effects([pe.withStroke(linewidth=3.2,foreground='white')])
ax.add_patch(Rectangle((0,0),13.0,31.1,fill=False,edgecolor='k',lw=3))
ax.add_patch(Rectangle((22,0),10.8,11.3,fill=False,edgecolor='k',lw=3))
ax.text(6.5,33.3,'HALA  ·  403,9 m² zabudowy  ·  31,1 × 13,0 m  ·  dwie nawy',ha='center',fontsize=12,weight='bold')
ax.text(6.5,-1.6,'↑ wejście od dziedzińca (od Grobli 64)',ha='center',fontsize=9)
ax.text(-0.5,29.4,'← rzeka / wał',ha='right',fontsize=9)
ax.text(13.5,29.4,'ul. Grobla →',ha='left',fontsize=9)
ax.annotate('',xy=(2.2,32.2),xytext=(2.2,30.6),arrowprops=dict(arrowstyle='-|>',lw=2));ax.text(2.2,33.4,'N',ha='center',fontsize=10,weight='bold')
ax.text(27.4,13.0,'DOM GROBLA 64  ·  121,0 m²  ·  10,8 × 11,5 m',ha='center',fontsize=12,weight='bold')
ax.text(27.4,-1.6,'↑ wejście od ulicy',ha='center',fontsize=9)
ax.plot([22,27],[14.4,14.4],'-',color='k',lw=3); ax.text(22,15.0,'5 m',fontsize=8.5)
ax.text(27.4,17.4,'rekonstrukcja autorska programu wnętrza w skali 1:200',ha='center',fontsize=9.5,style='italic')
ax.text(6.5,-3.9,'rekonstrukcja autorska programu wnętrza w skali 1:200 — hipoteza typologiczna, nie inwentaryzacja',ha='center',fontsize=9.5,style='italic')
ax.set_aspect('equal'); ax.set_xlim(-3,36); ax.set_ylim(-5.5,34.6)
ax.axis('off')
plt.tight_layout(); plt.savefig('fig_reko.jpg',dpi=170,bbox_inches='tight')
print('ok')
