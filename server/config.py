PORT=5002
DEBUG=False

# root 用户密码
OS_PASSWORD = "*"
# squid默认配置路径
SQUID_CONFILE = '/etc/squid/squid.conf'
# squid配置模板
SQUIDCONF_EXAMPLE = "squid.conf.example.linux"


# 代理登录账号
PROXY_USER = '17liuxue'
PROXY_PWD = '17liuxue'

# 重拨命令
COMMAND = '/usr/sbin/squid3 -k reconfigure'