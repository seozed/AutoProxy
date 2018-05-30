import os
import time
from config import *
from urllib.request import urlopen
from urllib import parse
from device import DeviceInfo




class Redial(object):
    def __init__(self):
        self.url = self.build_URL()

    def pushCurrentAddress(self, url, max_try=3):
        """
        向服务器报告自己的IP
        :param url:
        :type url:
        :param port:
        :type port:
        :param name:
        :type name:
        :param category:
        :type category:
        :return:
        :rtype:
        """

        for i in range(max_try):
            try:
                response = urlopen(url, timeout=10)
                if response.read().decode() == 'ok':
                    print('IP PUSH OK')
                    return True

            except:
                print('IP PUSH faild. Try again after 5 seconds.')
                time.sleep(5)

        return False

    def redial(self):
        os.system('sh pppoe.sh')


    def build_URL(self):

        device = DeviceInfo()
        params = {
            "mac": device.mac,
            "id": device.id,
            'operators': device.operators,
            'province': device.province,
            'city': device.city,
            "port": PROXY_PORT,
            'pwd': '17liuxue',
            'user': '17liuxue',
        }

        query = parse.urlencode(params)
        path = "record"
        url = "http://{}/{}?{}".format(SERVICE_ADDRESS, path, query)
        return url

    def start(self, sleep_time=10):
        """重拨逻辑"""

        while 1:
            self.redial()
            result = self.pushCurrentAddress(self.url, max_try=10)

            if result:
                return True

            else:
                time.sleep(sleep_time)

if __name__ == '__main__':
    redial = Redial()
    a = redial.build_URL()
    print(a)