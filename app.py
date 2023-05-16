from flask import Flask
from gevent import pywsgi
from apps_route import route_login, route_download
from settings import URL, PORT

app = Flask(__name__)   # app构建
# 注册蓝本
app.register_blueprint(route_login)
app.register_blueprint(route_download)


# 解决跨域问题
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-filetype'
    return environ


if __name__ == '__main__':
    # server = pywsgi.WSGIServer((URL, PORT), app)
    # server.serve_forever()
    app.run(port=PORT, debug=True)
