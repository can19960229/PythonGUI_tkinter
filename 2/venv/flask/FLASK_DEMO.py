# coding:UTF-8
import flask
app = flask.Flask(__name__)      # 创建一个Flask对象
@app.route("/")     # 设置访问路径“/”为根路径（只支持GET请求）
def index():
    return "<h1> 启动了一个flask程序.......<h1>"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True)   #启动flask程序