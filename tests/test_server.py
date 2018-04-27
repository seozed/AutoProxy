# -*- coding:utf-8 -*-
"""
DATE: 2018/4/26
"""
import unittest

from server.settingser import Settingser


class TestServer(unittest.TestCase):


    def test_gen(self):
        proxy_items = [{'city': '成都',
                  'id': 'ed1d51ce-9b5c-3496-93e8-fe0537039303',
                  'ip': '127.0.0.1',
                  'mac': '34:97:F6:34:F2:25',
                  'operators': '电信',
                  'port': '62222',
                  'province': '四川',
                  'pwd': '17liuxue',
                  'squid_port': 3128,
                  'user': '17liuxue'}]

        template_file = "D:\scripts\AutoProxy_new\server\squid.conf.example.linux"
        output_file = "squid.conf.test"
        settings = Settingser(template_file=template_file)
        content = settings.generate(proxy_items)
        settings.save(content, output_file)
        self.assertIsNotNone(content)



if __name__ == '__main__':
    unittest.main()
