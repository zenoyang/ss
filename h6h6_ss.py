# -*- coding: utf-8 -*-
import requests
import re
import os

# yz
# 2017/4/14

url = 'http://h6v6.com/'

try:
    html = requests.get(url)
    os.system('echo get free ss from ' + url)
except:
    os.system('echo ' + url + ' failed')
    exit(0)

# pattern = re.compile(r"<td>([_\da-zA-Z.-]+)</td>")
pattern = re.compile('<td>(.*?)</td>')
elem = pattern.findall(html.text)


ss_info = []
for i in range(0, 35, 7):
    if re.match('[_\da-zA-Z.-]+', elem[i+3]):
        #print (elem[i+3])
        ss_info.append({'ip': elem[i+1], 'port': elem[i+2], 'local_port': '1080', 'password': elem[i+3], 'method': elem[i+4]})

i = 0
if len(ss_info) == 0:
    print (r'没有有效的ss,请访问 http://h6v6.com/ 查看详细信息')
    exit(0)
elif len(ss_info) > 1:
    i = input('请输入要使用的ss序号(0-{})：'.format(len(ss_info)))
    i = int(i)
else:
    i = 1

ss = ss_info[i-1]

command = "sslocal -s %s -p %s -l %s -k %s -m %s" % (ss.get('ip'),
           ss.get('port'), ss.get('local_port'), ss.get('password'), ss.get('method'))

print (command)
os.system('echo ' + command)
os.system(command)


