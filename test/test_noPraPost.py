# 导入requests模块
import json
import requests
# 请求的url地址
url = 'http://127.0.0.1:8899/userAdmin/usersSelect'
# 请求头
headers = {"content-filetype": "application/json"}
# json形式，参数用json
res1 = requests.post(url, headers=headers)
print(res1.text)

# json的中文显示
myjson1 = json.loads(res1.text)  # data是向 api请求的响应数据，data必须是字符串类型的
newjson1 = json.dumps(myjson1, ensure_ascii=False)  # ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了

print(newjson1)
