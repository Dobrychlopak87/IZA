import requests,re,html,time,csv
UA='Mozilla/5.0 Chrome/124'; S=requests.Session(); S.headers.update({'User-Agent':UA})
def page(q,p):
    r=S.get('https://www.zbc.uz.zgora.pl/dlibra/results',
            params={'action':'SimpleSearchAction','type':'-6','q':q,'p':p},timeout=60)
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',r.text,flags=re.S)
    t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',html.unescape(t))
    i=t.find('Dodaj wszystkie do bibliografii'); seg=t[i:] if i>0 else t
    return re.findall(r'([A-ZŻŹĆĄŚĘŁÓŃ][^|]{5,220}?)(\d{4}|\[b\.r\.\]|\[b\. r\.\]|\[1903\]|\[1930\])\s*(pocztówka|czasopismo|czasopisma|artykuł|książka|mapa|katalog|fotografia|dokument|informator|rycina)',seg)
out=[]
for q in ['Crossen','Crossen Oder','Krosno Odrzańskie']:
    for p in range(1,12):
        its=page(q,p)
        if not its: break
        out += [(q,)+x for x in its]; time.sleep(0.3)
seen={}
for q,t,y,ty in out:
    k=re.sub(r'\s+',' ',t).strip()
    seen.setdefault(k,(y,ty,q))
with open('zbc_ZielonaGora_Crossen_tytuly.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter=';'); w.writerow(['tytul','rok','typ','zapytanie'])
    for k,(y,ty,q) in sorted(seen.items()): w.writerow([k,y,ty,q])
print('zbc unique',len(seen))
