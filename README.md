# my_hust_hub_utils

写着玩的小工具

## 一键充值网费

topup_hust_wireless.py

由电子账户自动向校园网账户转账

username:学号 

password:HUB密码

tranamt:转账金额，**单位(分)** ~~属实有点蠢~~

cardpwd:校园卡密码

cardno:校园卡id，就是校园卡照片下面的那个No.

acctype:填“000”即可

aid:'0030000000002101'

```python
def topup(username,password,tranamt,cardpwd,cardno,sno,aid,acctype)
```

