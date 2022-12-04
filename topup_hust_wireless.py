from libhustpass import login
import requests
import re


def get_account(username,password):
    ticket = login(username,password,"http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
    r = requests.session()
    ret = r.get(ticket)
    #print(ret.text)
    account = re.findall('<span class="red">(.*)</span></span>', ret.text)
    print("卡账户余额:"+account[0])
    print("电子账户余额:"+account[1])




def topup(username,password,tranamt,cardpwd,cardno,sno,aid,acctype):
    ticket = login(username,password,"http://ecard.m.hust.edu.cn/wechat-web/networkpay/network.html")
    r = requests.session()
    ret = r.get(ticket)
    #print(ret.text)
    url = "http://ecard.m.hust.edu.cn/wechat-web/networkpay/paynetgdc.html?"
    netacc = '{"netacc":'+'"'+ sno +'",'+'"bal":null,"pkgid":null,"lostflag":null,"freezeflag":null,"expflag":null,"statustime":null,"duration":null,"starttime":null,"pkgtab":[]}'
    param = 'account=' + cardno \
            + '&aid=' + aid \
            + '&acctype='+acctype \
            + '&tranamt=' + tranamt \
			+ '&Abstract=缴上网费' \
            + '&netacc=' + netacc\
            + '&pkgflag=none&pkg=&password=' + cardpwd
    #print(param)
    topup_get = r.get(url+param)
    print(topup_get)



