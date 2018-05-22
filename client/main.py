from flask import Flask
from config import *
from redial import Redial


# TODO 只在初始化的时候获取地区参数，后面就调用内存中的数据
app = Flask(__name__)
status = None

adsl = Redial()

@app.route('/redial', methods=['GET'])
def redial():
    global status
    if status:
        return "正在拨号中..."

    else:
        status = True

        adsl.start()
        status = False
        return "redial sucess!"


if __name__ == '__main__':

    # # init connect
    redial()

    # http server app
    app.run(host='0.0.0.0', port=HTTP_PORT)
