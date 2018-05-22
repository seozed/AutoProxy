# -*- coding:utf-8 -*-
"""
DATE: 2018/4/26
"""
from uuid import getnode as get_mac
from urllib.request import urlopen
from urllib.error import URLError
from socket import timeout
import shortuuid


class DeviceInfo(object):

    def __init__(self):
        self.city = None
        self.operators = None
        self.province = None
        self.ip = None
        self.__get_network_info()

    def __get_network_info(self):

        try:
            response = urlopen("https://myip.ipip.net/", timeout=5)
            text = response.read().decode()
            *_, self.province, self.city, self.operators = [val.strip() for val in text.split(' ') if val]

            # 切割出IP字符串
            self.ip = _[1][3:]

        except (URLError, timeout):
            print("get network info request connect timeout!")

    @property
    def mac(self):

        mac = get_mac()
        mac_address = ':'.join(("%012X" % mac)[i:i + 2] for i in range(0, 12, 2))
        return mac_address

    @property
    def id(self):

        return shortuuid.uuid()


if __name__ == '__main__':
    device = DeviceInfo()
    print(device.id)
    print(device.mac)
    print(device.city)
    print(device.province)
    print(device.operators)
    print(device.ip)
