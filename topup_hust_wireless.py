from libhustpass import login
import json
import requests
import re


def get_account(username,password):
    ticket = login(username,password,"http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
    r = requests.session()
    ret = r.get(ticket)
    #print(ret.text)
    account = re.findall('<span class="red">(.*)</span></span>', ret.text)
    print("电子账户余额:"+account[1])

def topup(username,password,value,card_pwd,cardno,acctype):
    ticket = login(username,password,"http://ecard.m.hust.edu.cn/wechat-web/networkpay/network.html")
    r = requests.session()
    ret = r.get(ticket)
    #print(ret.text)
    url = "http://ecard.m.hust.edu.cn/wechat-web/networkpay/paynetgdc.html?"
    aid = '0030000000002101'
    tranamt = '100' #转入金额(分)
    account = '267959'
    sno = 'M202273643'
    netacc = '{"netacc":'+'"'+ sno +'",'+'"bal":null,"pkgid":null,"lostflag":null,"freezeflag":null,"expflag":null,"statustime":null,"duration":null,"starttime":null,"pkgtab":[]}'

    param = 'account=' + account \
            + '&aid=' + aid \
            + '&acctype='+acctype \
            + '&tranamt=' + tranamt \
			+ '&Abstract=缴上网费' \
            + '&netacc=' + netacc\
            + '&pkgflag=none&pkg=&password=' + card_pwd
    #print(param)
    topup_get = r.get(url+param)
    print(topup_get)
if __name__ == '__main__':
    print("充值")

