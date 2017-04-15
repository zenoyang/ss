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
    os.system('echo ' + url + 'failed')


pattern = re.compile("<td>([_\da-zA-Z.-]+)</td>")
elem = pattern.findall(html.text)


ss_info = []
for i in range(0, 20, 4):
    ss_info.append({'ip': elem[i], 'port': elem[i+1], 'local_port': '1080', 'password': elem[i+2], 'method': elem[i+3]})

ss = ss_info[0]

command = "sslocal -s %s -p %s -l %s -k %s -m %s" % (ss.get('ip'),
           ss.get('port'), ss.get('local_port'), ss.get('password'),ss.get('method'))

os.system('echo ' + command)
os.system(command)


