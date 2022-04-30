import os
import json
import time
import requests
from bs4 import BeautifulSoup as parser

p = '\033[1;37m'
t = '\033[0;32m'
k = '\033[1;33m'
q = '\033[30m'
u = '\033[0;37m'
z = '\033[2;107m'
o = '\033[90m'
v = '\033[0m'
r = '\033[0;36m'

class Fire(object):
    def __init__(self,email=None):
        self.ses = requests.Session()
        self.bus = []
        if email is None:
           if not os.path.exists(".email"):
              open(".email","w").write(input("[•] Input email/: "))

    def parsLogin(self,email):
        self.url = "https://firebitcoin.xyz/"
        self.req = parser(self.ses.post(self.url,data={"email":email,"submit":""}).text,"html.parser")
        if self.req.findAll("div",attrs={"class":"form-control"}) is not None:
           for self.bal in self.req.findAll("div",attrs={"class":"form-control"}):
               self.bus.append(self.bal.text)
           return self.bus
        else:
           os.remove(".email")

    def timedown(self,second):
        while second:
            mins,secs = divmod(second,60)
            timer = "  {}⏣ {}Limit {}⟨{}{:02}:{:02d}{}⟩ ".format(t,p,o,p,mins,secs,o)
            print(timer,end="\r")
            time.sleep(1)
            second -= 1

    def parsClaim(self):
        __import__("os").system("clear")
        self.account = self.parsLogin(open(".email").read())
        print(f"""{r}\n  {r}▄    ▄▄▄▄▄▄▄    ▄\n {r}▀▀▄─▄█████████▄─▄▀▀  {r}╔╗ {p}┬┌┬┐┌┐ ┌─┐┬ ┬   {r}╔═╗{p}┬ ┬┌─┐┌┐┌┌─┐┬\n {r}    ██ {k}▀{r}███{k}▀ {r}██      {r}╠╩╗{p}│ │ ├┴┐│ │└┬┘{q}───{r}║  {p}├─┤├─┤│││├┤ │\n {r}  ▄─▀████{k}▀{r}████▀─▄    {r}╚═╝{p}┴ ┴ └─┘└─┘ ┴    {r}╚═╝{p}┴ ┴┴ ┴┘└┘└─┘┴─┘\n {u}▀█    ██▀█▀██   █▀   {z}{q} By : Kingtebe | Yt : Bitboy Channel {v}{p}\n\n  {t}⏣ {p}Username {o}: {p}{open('.email').read()}\n  {t}⏣ {p}Referral {o}: {p}{self.account[2]}\n  {t}⏣ {p}Balance  {o}: {p}{self.account[0]}\n""")
        while True:
            print(f"  {t}⏣ {p}Trying bypass captcha",end="\r")
            self.lur = "https://firebitcoin.xyz/assets/src/captcha-request.php"
            self.qer = self.ses.post(self.lur,headers={"x-requested-with":"XMLHttpRequest"},data={"cID":"0","rT":"1","tM":"light"}).json()
            self.sat = self.qer[0];self.dua = self.qer[1];self.tig = self.qer[2];self.pat = self.qer[3];self.lim = [4]
            self.ret = self.ses.post(self.lur,headers={"x-requested-with":"XMLHttpRequest"},data={"cID":"0","pC":self.sat,"rT":"2"})
            self.url = "https://firebitcoin.xyz/faucet.php"
            self.req = parser(self.ses.post(self.url,headers={"content-type":"application/x-www-form-urlencoded"},data={
               "captcha-hf":self.sat,
               "captcha-idhf":"0",
               "claim":"Claim"
            }).text,"html.parser")
            try:
                self.earn = self.req.find("div",attrs={"class":"alert alert-success"})
                self.updt = parser(self.ses.get(self.url).text,"html.parser").findAll("div",attrs={"class":"form-control"})[0]
                print(f"  {t}⏣ {p}{self.earn.text} {o}[ {t}{self.updt.text} {o}]")
                self.timedown(int(60*5))
            except AttributeError:
                print(f"  {t}⏣ {p}Incorrect captcha         ",flush=True,end="\r")
                continue

if __name__=='__main__':
   Fire().parsClaim()

