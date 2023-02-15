from flask import Flask

app = Flask(__name__)  # 实例化


@app.route('/mock1', methods=['POST'])
def lxf():
    return "我是flask哪吒"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port= 1234, debug=True)
