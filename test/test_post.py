# 导入requests模块
import json
import requests
# 请求的url地址
url = 'http://127.0.0.1:8899/public/login'
# 请求头
headers = {"content-filetype": "application/json"}
# payload 为传入的参数
payload = {"username": "root1", "password": "root1"}
# json形式，参数用json
res = requests.post(url, json=payload, headers=headers)
print(res.text)

# rsp = requests.post(url,json=payload,headers=headers,timeout = 3).json()
# code = rsp['status']
# if code != 1000 :
#     print(rsp)
# else:
#     print("管理员列表输出成功")

# json的中文显示
myjson = json.loads(res.text)  # data是向 api请求的响应数据，data必须是字符串类型的
newjson = json.dumps(myjson, ensure_ascii=False)  # ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了

print(newjson)
