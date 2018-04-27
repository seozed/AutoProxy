from flask import Flask
from config import *
from redial import Redial

app = Flask(__name__)
status = None

@app.route('/redial', methods=['GET'])
def redial():
    global status
    if status:
        return "正在拨号中..."

    else:
        status = True
        redial = Redial()
        redial.start()
        status = False
        return "redial sucess!"


if __name__ == '__main__':

    # # init connect
    redial()

    # http server app
    app.run(host='0.0.0.0', port=HTTP_PORT)
