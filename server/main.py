# -*- coding:utf-8 -*-
from flask import request, Flask
import os
import config
import json
from settingser import Settingser

class UniqueIndexList(list):

    def __init__(self, key):
        self.key = key
        super().__init__(self)

    def append(self, p_object):

        tmp_port = None
        for index, item in enumerate(self):
            if item[self.key] == p_object[self.key]:
                tmp_port = item['squid_port']
                del self[index]

        p_object['squid_port'] = tmp_port or len(self) + 3128
        super().append(p_object)


#==================================================================
#==================================================================
#==================================================================

# check setting
if not all([config.PROXY_PWD, config.PROXY_USER]):
    raise ValueError("未指定代理账号")


app = Flask(__name__)
proxy_pool = UniqueIndexList('id')


@app.route('/record', methods=['GET'])
def record():
    """
    获取代理节点的IP，并更新到squid配置中
    """
    try:
        item = dict()
        item['ip'] = request.remote_addr
        item['id'] = request.args['id']
        item['port'] = request.args['port']
        item['mac'] = request.args.get('mac')
        item['city'] = request.args.get('city')
        item['operators'] = request.args.get('operators')
        item['province'] = request.args.get('province')
        item['user'] = '17liuxue'
        item['pwd'] = '17liuxue'
        proxy_pool.append(item)

        update_settings(proxy_list=proxy_pool, output_file=config.SQUID_CONFILE, template_path=config.SQUIDCONF_EXAMPLE)
        return "ok"

    except KeyError:
        return "argument error"

def update_settings(proxy_list, output_file, template_path):
    """更新squid配置"""

    if not os.path.exists(template_path):
        raise FileNotFoundError("The template file does not exist")

    settingser = Settingser(template_file=template_path)
    content = settingser.generate(proxy_list)
    settingser.save(content, output_file)

    # 重载squid配置， 仅适用于linux系统, 必须root权限
    password = config.OS_PASSWORD

    if not config.DEBUG:
        os.system('echo %s |sudo -S %s' % (password, config.COMMAND))
        print('reload settings success.')


@app.route('/getip', methods=['GET'])
def get_proxy():
    result = json.dumps(proxy_pool)
    # TODO: 加入获取指定分类，指定ID的IP
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)
