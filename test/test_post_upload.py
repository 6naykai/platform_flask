import json
import requests

# 请求的url地址
url = 'http://127.0.0.1:8899/upload'
# 请求头
headers = {"content-filetype": "multipart/form-data"}

myfiles = {
    'file': open('E:/workspace/software_course/Integrated_application_platform/platform_flask/static/music'
                 '/情人.mp3', 'rb')
}

# mydata = {
#         'orgId': 'xxx',
#         'roleIds': 'xxx',
#         'userGroupIds': 'xxx',
#         'invalidTime': 'xxx',
# }


# res = requests.post(url, headers=headers, data=mydata, files=myfiles)
res = requests.post(url, headers=headers, files=myfiles)
print(res.text)


