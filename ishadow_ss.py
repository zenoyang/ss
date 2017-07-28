# _*_ coding: utf-8 _*_

# yz
# 2017/4/11

import requests
import re
import os


def get_free_ss_info():
    # url = 'http://xyz.ishadow.online/'
    # url = 'http://free.ishadow.online/'
    url = 'http://ss.ishadowx.com/'

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
    ss_infos = []
    for i in range(12):
        # yield {'IP_Address': ip_address[i], 'port': port[i], 'local_port': local_port,
        #        'Password': password[i], 'Method': method[i]}
        ss_infos.append({'IP_Address': ip_address[i], 'port': port[i], 'local_port': local_port,
                         'Password': password[i], 'Method': method[i]})
    return ss_infos


def main():
    # ss_infos = []
    # for item in get_free_ss_info():
    #     ss_infos.append(item)
    ss_infos = get_free_ss_info()

    str = '''
1-3: 美国   
4-6: 日本   
7-9: 新加坡
10-12: SSR
    '''
    print (str)
    i = input('请输入要使用的ss序号：')
    i = int(i)
    ss = ss_infos[i-1]

    command = "sslocal -s %s -p %s -l %s -k %s -m %s" % (ss.get('IP_Address'), ss.get('port'), ss.get('local_port'),
                                                         ss.get('Password'), ss.get('Method'))

    os.system('echo ' + command)
    os.system(command)

if __name__ == '__main__':
    main()
