# my_hust_hub_utils

写着玩的小工具

## 一键充值网费

由银行卡直接向校园网账户转账（~~再也不需要在企业微信里操作两次了~~）

### 依赖

python3.6+ 以及 [Tesseract](https://tesseract-ocr.github.io/)

```shell
python setup.py install
```

### 使用方法

调用topup_hust_wireless.py中quick_topup_wireless即可

```python
def quick_topup_wireless(username, password, tranamt, cardpwd, cardno, sno, aid, acctype)
```

username:统一身份认证用户名

password:统一身份认证密码

tranamt:充值金额，**单位是分，不是元**

cardpwd:校园卡密码

cardno:校园卡六位卡号，即校园卡照片右下角No.xxx

sno:学号

aid:'0030000000002101'

acctype: '000'
