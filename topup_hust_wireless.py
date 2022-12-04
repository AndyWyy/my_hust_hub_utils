from libhustpass import login
import requests
import re
import json


#获取卡账户余额，电子账户余额，过渡余额
def get_account(username,password):
    ticket = login(username,password,"http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
    r = requests.session()
    ret = r.get(ticket)
    account = re.findall('<span class="red">(.*)</span></span>', ret.text)
    in_account = re.findall('<dd>(.*)元</dd>', ret.text)
    print("卡账户余额:"+account[0])
    print("电子账户余额:"+account[1])
    print("过渡余额:" + in_account[0])

#充值卡账户
def topup_card(username, password, value, cardno, cardpwd):
    ticket = login(username, password,
                   "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
    r = requests.session()
    ret = r.get(ticket)
    
    get_account(username, password)
    
    url = "http://ecard.m.hust.edu.cn/wechat-web/ChZhController/ChongZhi.html?"\
        + 'value=' + str(value) + ',' + cardpwd \
        + '&cardno=' + cardno\
        + '&acctype=1'
    topup_card_get = r.get(url).text.strip("callJson(").strip(" )")
    topup_card_json = json.loads(topup_card_get)
    print(topup_card_json)
    

#充值电子账户
def topup_e_account(username, password, value, cardno, cardpwd):
    ticket = login(username, password,
                   "http://ecard.m.hust.edu.cn/wechat-web/service/card_recharge.html")
    r = requests.session()
    ret = r.get(ticket)

    get_account(username, password)

    url = "http://ecard.m.hust.edu.cn/wechat-web/ChZhController/ChongZhi.html?"\
        + 'value=' + str(value) + ',' + cardpwd \
        + '&cardno=' + cardno\
        + '&acctype=000'
    topup_e_account_get = r.get(url).text.strip("callJson(").strip(" )")
    topup_e_account_json = json.loads(topup_e_account_get)
    print(topup_e_account_json)

#由电子账户向校园网账户转账
def topup_wireless(username,password,tranamt,cardpwd,cardno,sno,aid,acctype):
    ticket = login(username,password,"http://ecard.m.hust.edu.cn/wechat-web/networkpay/network.html")
    r = requests.session()
    ret = r.get(ticket)
    url = "http://ecard.m.hust.edu.cn/wechat-web/networkpay/paynetgdc.html?"
    netacc = '{"netacc":'+'"'+ sno +'",'+'"bal":null,"pkgid":null,"lostflag":null,"freezeflag":null,"expflag":null,"statustime":null,"duration":null,"starttime":null,"pkgtab":[]}'
    param = 'account=' + cardno \
            + '&aid=' + aid \
            + '&acctype=' + acctype \
            + '&tranamt=' + tranamt \
			+ '&Abstract=缴上网费' \
            + '&netacc=' + netacc\
            + '&pkgflag=none&pkg=&password=' + cardpwd
    topup_get = r.get(url+param).text.strip("callJson(").strip(" )")
    print(topup_get)

#一键充值校园网账户(从银行卡到校园网)
def quick_topup_wireless(username, password, tranamt, cardpwd, cardno, sno, aid, acctype):
    value = int(tranamt)/100
    topup_e_account(username, password, value, cardno, cardpwd)
    topup_wireless(username, password, tranamt, cardpwd, cardno, sno, aid, acctype)


