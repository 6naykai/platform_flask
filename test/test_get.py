# 导入requests模块
import json
import requests
# 请求的url地址
url = 'http://127.0.0.1:8899/user/musicDownload/E:\\workspace\\software_course\\Integrated_application_platform' \
      '\\platform_flask\\static\\music\\情人.mp3 '

# r = requests.get(url, stream=True)
r = requests.post(url, stream=True)
f = open("file.mp3", "wb")
for chunk in r.iter_content(chunk_size=512):
    if chunk:
        f.write(chunk)

