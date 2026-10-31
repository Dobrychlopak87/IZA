import re,json,hashlib,time,urllib.parse,requests,sys
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
S=requests.Session(); S.headers.update({'User-Agent':UA})
BASE='https://opus4.kobv.de'

def solve(html,redir):
    m=re.search(r'<script id="anubis_challenge" type="application/json">(.*?)</script>',html,re.S)
    ch=json.loads(m.group(1))
    c=ch['challenge']; diff=c['difficulty']; data=c['randomData']; cid=c['id']
    p=diff//2; odd=diff%2
    n=0; t0=time.time()
    while True:
        h=hashlib.sha256((data+str(n)).encode()).digest()
        ok=all(h[i]==0 for i in range(p))
        if ok and odd and (h[p]>>4)!=0: ok=False
        if ok: break
        n+=1
    resp=h.hex()
    url=f"{BASE}/.within.website/x/cmd/anubis/api/pass-challenge"
    q={'id':cid,'response':resp,'nonce':n,'redir':redir,'elapsedTime':int((time.time()-t0)*1000)}
    r=S.get(url,params=q,allow_redirects=False,timeout=60)
    return r.status_code, r.headers.get('set-cookie','')[:80], n

def get(url,redir=None):
    r=S.get(url,timeout=120)
    if 'anubis_challenge' in r.text[:2000] or 'not a bot' in r.text[:200]:
        st,ck,n=solve(r.text, redir or url)
        print('  solved',st,ck,'nonce',n,flush=True)
        r=S.get(url,timeout=120)
    return r

if __name__=='__main__':
    u=sys.argv[1]; out=sys.argv[2]
    r=get(u)
    print(r.status_code,len(r.content),r.headers.get('content-type'))
    open(out,'wb').write(r.content)
