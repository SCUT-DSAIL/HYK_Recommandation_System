
import requests
import json
import time
import hmac
import hashlib
import random
def generate_signature(appid, noncestr, timestamp, appsecret):
    # 按指定格式拼接参数
    sign_str = f"appid={appid}&noncestr={noncestr}&timestamp={timestamp}"

    # sign_str = f"{appid}{noncestr}{timestamp}"
    
    # 使用HMAC-SHA256算法生成签名
    hmac_obj = hmac.new(
        key=appsecret.encode("utf-8"),
        msg=sign_str.encode("utf-8"),
        digestmod=hashlib.sha256
    )
    
    # 返回十六进制格式的签名字符串
    print(sign_str)
    return hmac_obj.hexdigest()
timestamp = int(time.time())
#推荐API密钥信息：
noncestr=str(random.random())
appid="2000000000000293"
appsecret="eeaec6a22f2152e1c57300ecc972f337c729876feee01b38e3b7dac3a393a1ad"
adtag="hyk.zxtj"
query = "乳腺癌"
signature = generate_signature(appid, noncestr, timestamp, appsecret)
url = 'https://preview.baike.qq.com/api/access/json/cmd/SearchV2'
text = {
    "header": {
        "version": "1.0.0", 
        "flag": 0
    }, 
    "body": {
        "seq": 0, 
        "cmd": "SearchV2", 
        "token": "", 
        "client": {
            "clientIP": "", 
            "adtag": "hyk.zxtj"
        }, 
        "payload": {
            "timestamp": str(timestamp), 
            "noncestr": noncestr, 
            "signature": signature, 
            "appid": appid,
            "search_req": {
                "query": query, 
                "offset": 0, 
                "count": 10, 
                "adtag": "hyk.zxtj", 
                "type": 0, 
                "searchid": "b67ee785-40ab-4cc9-8c73-c2b1ba3fbdc2"
            }
        }
    }
}
headers = {'Content-Type': 'application/json'}
 
response = requests.post(url, headers=headers, data=json.dumps(text))
 
# 打印响应内容
print(response.text)
