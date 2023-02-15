"""
需求：做挡板
url：127.0.0.0.1/test，port=8888，
请求参数：name:张三，返回值：年龄：20，职业：测试，公司：测试公司 信息；请求方式要求post
"""

from flask import Flask,request,json

app = Flask(__name__)

@app.route('/test',methods=['post'])
def get_inf():
    # 获取张三的相关信息
    if request.method=='POST':
        data = {
            "姓名":"张三",
            "年龄":"20",
            "职业":"测试",
            "公司":"测试公司"
        }
    return json.dumps(data)


if __name__ == "__main__":
    app.run(host = '127.0.0.1',port=8888)







