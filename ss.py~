# _*_ coding: utf-8 _*_

# yz
# 2017/4/11

import requests
import re
import os
import random


def get_ss_from_ishadow():
    # url = 'http://xyz.ishadow.online/'
    url = 'http://free.ishadow.online/'

    try:
        html = requests.get(url)
    except:
        os.system('echo ' + url + '访问失败')
        return None
    os.system('echo get free ss from ' + url)

    # IP_Address
    pattern = re.compile("<h4>.*?IP Address.*?<span id=.*?>(.*?)</span>")
    ip_address = pattern.findall(html.text)

    # port
    pattern = re.compile("<h4>Port(.*?)</h4>")
    port = pattern.findall(html.text)
    for index, item in enumerate(port):
        port[index] = re.findall("\d+", item)[0]  # 清理'：'乱码

    # local_port
    local_port = "1080"

    # Password
    # 不是每个都有密码，貌似没有提供密码的不能用
    pattern = re.compile("<h4>.*?Password.*?<span id=.*?>(.*?)</span>")
    password = pattern.findall(html.text)

    # Method
    pattern = re.compile("<h4>Method:(.*?)</h4>")
    method = pattern.findall(html.text)

    for i in range(12):
        yield {'IP_Address': ip_address[i], 'port': port[i], 'local_port': local_port,
               'Password': password[i], 'Method': method[i]}


def sslocal_ishadow(index):
    ss_infos = []
    for item in get_ss_from_ishadow():
        ss_infos.append(item)

    ss = ss_infos[index]

    command = "sslocal -s %s -p %s -l %s -k %s -m %s" % (ss.get('IP_Address'),
                                                         ss.get('port'), ss.get('local_port'), ss.get('Password'),
                                                         ss.get('Method'))

    os.system('echo ' + command)
    os.system(command)


def sslocal_h6h6(index):
    url = 'http://h6v6.com/'

    try:
        html = requests.get(url)
    except:
        os.system('echo ' + url + '访问失败')
        return None
    os.system('echo get free ss from ' + url)

    pattern = re.compile("<td>([_\da-zA-Z.-]+)</td>")
    elem = pattern.findall(html.text)

    ss_info = []
    for i in range(0, 20, 4):
        ss_info.append(
            {'ip': elem[i], 'port': elem[i + 1], 'local_port': '1080', 'password': elem[i + 2], 'method': elem[i + 3]})

    ss = ss_info[index]

    command = "sslocal -s %s -p %s -l %s -k %s -m %s" % (ss.get('ip'),
                                                         ss.get('port'), ss.get('local_port'), ss.get('password'),
                                                         ss.get('method'))

    os.system('echo ' + command)
    os.system(command)


def main():
    try:
        # ishadow有12个免费ss可供切换 集体信息在 http://free.ishadow.online/ 中查看
        '''
        UNITEDSTATES    0-2     一般
        JAPAN           3-5     貌似不能用
        SINGAPORE       6-8     貌似速度快点，YouTube 1080p不卡顿
        SSR             9-11    没测试
        '''
        index = random.randint(0, 11) 
        sslocal_ishadow(index)
    except:
        # h6h6有5个免费ss可供切换  0-4
        # 这5个ss相关信息可在 http://h6v6.com/ 中查看
        index = random.randint(0, 4)
        sslocal_h6h6(index)


if __name__ == '__main__':
    main()

