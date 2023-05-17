from .route_login import route_login
from .route_download import route_download
from .route_public import route_public


# 路由蓝本列表: 用以简化app.py文件,蓝本不需要在app.py中一个一个注册了,可采用for语句完成
route_list = [route_login,
              route_download,
              route_public]
