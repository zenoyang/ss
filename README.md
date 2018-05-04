# SS

## ChangeLog
	* 2018-05-04 添加User-Agent，修复之前请求问题  
	* 2017-12-30 修复部分正则表达式，又可以正常使用啦～～～  
	* 2017-8-15 h6h6_ss.py脚本失效

## 简介
这是一个利用爬虫自动从网上获取免费ss账号并且配置本机代理的脚本  

## 准备

需要提前装Python3 以及 pip

### 安装Shadowsocks
```
pip install shadowsocks
```
### Chrome安装SwitchyOmega插件并配置
将项目中的SwitchyOmega.crx拖向 设置-扩展程序 即可  
安装好之后Chrome右上角有个圈圈，点击圈圈->选项->新建情景模式->随意取个名字->代理协议:SOCKS5,代理服务器:127.0.0.1,代理端口:1080就可以了。  
运行上面的命令，再选择圈圈中刚在新建的情景模式即可   
![SwitchyOmega](http://oqnf3xv0b.bkt.clouddn.com/17-12-30/45168816.jpg)  


### Firefox安装Foxyproxy standard和配置   
打开Firefox浏览器，进入open menu>Add-ons，搜索框内输入Foxyproxy 选择Foxyproxy standard安装。重启浏览器后再来设置浏览器的配置，此时在菜单栏因该可以看到一个狐狸的头，没有的话也没关系，在浏览器的插件管理中一样可以看到它，点开进行设置。   
点击Add New Proxy，选择手动代理，设置本底服务器地址127.0.0.1和端口1080,同时代理方式设置成socks v5，点击OK，完成设置。   
再选择刚刚添加的模式。  
可以看到插件Foxyproxy的图标变成蓝色，表示代理有效。
![Foxyproxy](http://oe7jbxyeb.bkt.clouddn.com/Using%20Shadowsocks%20to%20gain%20Google%2002.png)

## 使用
### 使用脚本： 
`python3 ishadow_ss.py` 或 `python3 h6h6_ss.py`  

ishadow有12个免费ss可供切换  http://ss.ishadowx.com/  
h6h6有5个免费ss可供切换  http://h6v6.com/   

### 使用命令
爬虫不维护的话很快会失效，所有可以在网上找到免费的SS账号或者购买的ss账号，将账号信息添加到命令中对应位置即可。  
```
sslocal -s 服务器地址 -p 服务器端口 -l 本地端端口 -k 密码 -m 加密方法
```
配合nohup和&可以使之后台运行，关闭终端也不影响：
```
nohup sslocal -s 服务器地址 -p 服务器端口 -l 本地端端口 -k 密码 -m 加密方法 &
```
例如：
```
sslocal -s 104.160.185.150 -p 6123 -l 1080 -k "ntdtv.com" -t 300 -m aes-256-cfb 
```
如果是长期可使用的ss，将命令写进脚本中使用更方便

详细介绍：[Shadowsocks (简体中文)](https://wiki.archlinux.org/index.php/Shadowsocks_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#.E5.91.BD.E4.BB.A4.E8.A1.8C)
