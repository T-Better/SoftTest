import json
from flask import Flask,jsonify,request


# 创建一个应用对象
app = Flask(__name__)

# 定义视图函数，设置路由规则
@app.route("/index")
def index():
    print("访问index主页")
    return "hello mock"

# {"mobile":"13800000002", "password":"123456"}
@app.route("/api/sys/login",methods = ['POST'])
def login():
    # request.get_data()：接收请求过来的参数，这里是等待请求，不是主动发起！
    result = json.loads(request.get_data().decode("utf-8"))  # 字典形式的请求体数据
    mobile = result.get("mobile")
    password = result.get("password")
    print(mobile, password)
    if mobile == "13800000002" and password == "123456":
        data = {
            "success":True,
            "code":10000,
            "message":"操作成功!",
            "token": "ajsdfj-12312-szs-fd-dfs"}
    else:
        data = {
            "success": False,
            "code":99999,
            "message":"抱歉，系统繁忙，请稍后重试,",
            "token": None}
    return data


if __name__ == "__main__":
    # 启动WEB服务器
    app.run()
