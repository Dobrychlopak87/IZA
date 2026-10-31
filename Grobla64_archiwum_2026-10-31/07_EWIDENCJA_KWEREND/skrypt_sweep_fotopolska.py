import re,html,time,urllib.request,json,csv
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
def get(u):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode('utf-8','ignore')
        except Exception:
            time.sleep(2)
    return ''
idx={}
for N in range(0,1400,40):
    u=('https://fotopolska.eu/zdjecia/m49476,Krosno_Odrzanskie.html' if N==0
       else f'https://fotopolska.eu/zdjecia,{N},40/m49476,Krosno_Odrzanskie.html')
    s=get(u)
    tiles=re.findall(r'<div class="fitMini fm_(\d+)_\d+".*?class="fitMiniTytul"[^>]*>(.*?)<div style="margin-top:3px">.*?id="ft\d+">(\d{3,4})</div>',s,flags=re.S)
    new=0
    for pid,cap,yr in tiles:
        if pid not in idx:
            idx[pid]={'yr':yr,'cap':re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',cap))).strip()}; new+=1
    if len(tiles)==0: break
    if new==0 and N>40: break
    time.sleep(0.25)
rows=sorted(idx.items(), key=lambda kv:(kv[1]['yr'], int(kv[0])))
with open('fotopolska_Krosno_indeks_1137.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter=';')
    w.writerow(['rok','id_karty','podpis_oryginalny','url'])
    for pid,v in rows:
        w.writerow([v['yr'],pid,v['cap'],f'https://fotopolska.eu/{pid},foto.html'])
print('fotopolska rows',len(rows))
json.dump({k:v for k,v in idx.items()},open('fp_idx.json','w'),ensure_ascii=False)
