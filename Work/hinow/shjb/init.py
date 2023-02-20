#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/17
# file: init.py
# Email:
# Author: rakiwine

import requests
import datetime
import json

opc_data_list = []

result = []

def get_result_by_remote_consul_server(service_name, url, data_parms=None, timeout=None, is_log=False):
    status_code = 0
    message = 'error status code'
    content_result = None
    # 线上/本地
    sessionid = 'nq9aaro2aodxh4gc3pzuuze35n1839pw'
    # # # 切换精益行liyumes
    # service_name_dict = {
    #     # 线上
    #     'liyumes': 'http://222.133.28.202:9094/',
    #     # 本地
    #     # 'liyumes': 'http://192.168.1.111:9000/',
    #     # 'liyumes_offline': 'http://192.168.1.111:9000/',
    #
    #     # 不用管
    #     'liyusf': 'http://222.133.28.202:9094/',
    # }
    # 切换熠之云kpi
    service_name_dict = {
        # 线上
        'jyx_kpi': 'http://192.168.4.50/',

        # 本地
        # 'jyx_kpi': 'http://192.168.1.111:7000/',

        # 不用管
        # 'liyusf': 'http://211.142.91.46:9094/',
    }

    if service_name in service_name_dict.keys():
        base_url = service_name_dict[service_name]
    else:
        return status_code, u'error service', None

    url = base_url + url

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'sessionid': sessionid,
    }

    response = requests.post(
        url=url,
        json=data_parms,
        headers=headers
    )
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        content = json.loads(content)
        status_code = content['status_code']
        message = content['message']
        content_result = content
    elif response.status_code == 404:
        status_code = response.status_code
        message = u'Not Found'
    else:
        pass

    print(message)
    return status_code, message, content_result


def log_append(string, object_1, object_2, object_3):
    if not isinstance(string, str):
        string = json.loads(string)
    print(string)

    if isinstance(object_1, dict):
        for k, v in object_1.items():
            print(k, v)
    elif isinstance(object_1, list):
        for i in object_1:
            print(i)
    elif object_1 == '':
        pass
    else:
        print(object_1)

    if isinstance(object_2, dict):
        for k, v in object_2.items():
            print(k, v)
    elif isinstance(object_2, list):
        for i in object_2:
            print(i)
    elif object_2 == '':
        pass
    else:
        print(object_2)

    if isinstance(object_3, dict):
        for k, v in object_3.items():
            print(k, v)
    elif isinstance(object_3, list):
        for i in object_3:
            print(i)
    elif object_3 == '':
        pass
    else:
        print(object_3)


def save_result_msg(_list):
    for item in _list:
        print(item)
