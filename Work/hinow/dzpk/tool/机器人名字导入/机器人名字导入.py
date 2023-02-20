#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/11/17
# file: 机器人名字导入.py
# Email:
# Author: rakiwine

import urllib
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import snowflake.client
from Study.pythonReview.a1_complex.database.MysqlModel import MysqlModel
import pymysql

# 目标url
aimUrl = "https://www.qmsjmfb.com/"
# url = "https://www.ip138.com/"
# url = "http://httpbin.org/ip"
testUrl = "http://23.80.5.90/ip.php"

# 使用Cookie，跳过登陆操作
headers = {
    "Cookie": "",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "User-Agent": UserAgent().chrome,
}

data = {
    "xing": "",
    "xinglength": "all",
    "minglength": "all",
    "sex": "all",
    "dic": "default",
    "num": 999
}

Proxy = {'http': '127.0.0.1:7890'}

proxy_support = urllib.request.ProxyHandler(Proxy)

# 参数是一个字典{'类型':'代理ip:端口号'}
opener = urllib.request.build_opener(proxy_support)
# 定制opener
opener.add_handler = [
    ('User-Agent', UserAgent().chrome)
]
# add_handler给加上伪装
urllib.request.install_opener(opener)

publicNetworkIPAddress = urllib.request.urlopen("http://23.80.5.90/ip.php")
publicNetworkIPAddress = BeautifulSoup(publicNetworkIPAddress, "html.parser")
print(publicNetworkIPAddress.text)

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
# 请求对象的定制
request = urllib.request.Request(url=aimUrl, data=data, headers=headers)
# 模拟浏览器向服务器发送请求
html = urllib.request.urlopen(request)

# html = requests.post(aimUrl, data, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

_liList = soup.find("div", class_="name_box").find_all("li")

# 启动雪花服务器
# snowflake_start_server --worker=1 --dc=1 --port=8910
snowflake.client.setup("127.0.0.1", 8910)
_listDict = []
for _li in _liList:
    uuid = snowflake.client.get_guid()
    _listDict.append({
        "id": uuid,
        "name": _li.string,
        "isAI": 1,
    })

print(_listDict)

_username = "root"
_password = "Root_123"

_host = "127.0.0.1"
_database = "poker"

try:
    mysql = MysqlModel(_username, _password, _host, _database)
    mysql.insert_mysql_by_execute_once("User", ["id", "name", "isAI"], _listDict)
except pymysql.err.ProgrammingError as e:
    print("Exception Error is %s" % (e))
except pymysql.err.OperationalError as e:
    print("Exception Error is %s" % (e))
