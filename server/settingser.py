# -*- coding:utf-8 -*-
"""
DATE: 2018/4/26
"""


class Settingser(object):

    def __init__(self, template_file):

        if not template_file:
            print("template can't is none")

        self.template_file = template_file


    def save(self, content, path):
        with open(path, 'w') as file:
            file.write(content)

    def read_template(self, path):
        with open(path, encoding='utf8') as file:
            return file.read()

    def generate(self,proxy_items):

        settings = self.read_template(self.template_file)

        for item in proxy_items:
            port = "http_port {squid_port}".format(**item)
            acl = "acl PORT_{id} myport {squid_port}".format(**item)
            http_access = "http_access allow PORT_{id}".format(**item)
            cache_peer = "cache_peer {ip} parent {port} 0 allow-miss round-robin connect-fail-limit=1 login={user}:{pwd} no-query no-digest name={id}".format(**item)
            cache_peer_access = "cache_peer_access {id} allow PORT_{id}".format(**item)
            settings += '\n'.join([port, acl, http_access, cache_peer, cache_peer_access])

        settings += "\nhttp_access deny all"
        settings += "\nnever_direct allow all"
        self.settings = settings
        return settings

