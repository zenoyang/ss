# SS

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
![SwitchyOmega](http://i1.piimg.com/1949/3075a58fc94b937a.png)


### Firefox安装Foxyproxy standard和配置
打开Firefox浏览器，进入open menu>Add-ons，搜索框内输入Foxyproxy 选择Foxyproxy standard安装。重启浏览器后再来设置浏览器的配置，此时在菜单栏因该可以看到一个狐狸的头，没有的话也没关系，在浏览器的插件管理中一样可以看到它，点开进行设置。
点击Add New Proxy，选择手动代理，设置本底服务器地址127.0.0.1和端口1080,同时代理方式设置成socks v5，点击OK，完成设置。
再选择刚刚添加的模式。
可以看到插件Foxyproxy的图标变成蓝色，表示代理有效。
![Foxyproxy](http://oe7jbxyeb.bkt.clouddn.com/Using%20Shadowsocks%20to%20gain%20Google%2002.png)

## 使用
### 使用脚本： 
./run.sh  或  python3 ss.py  等等
ishadow有12个免费ss可供切换  http://free.ishadow.online/ 
需注意的是，ishadow几天换一次域名，所以需要复制点击上面地址跳转到的地址，更改ss.py或ishadow_ss.py中的URL即可
h6h6有5个免费ss可供切换  http://h6v6.com/ 
可在ss.py的main方法中配置，默认是随机使用某个ss

//2017/06/21 周三 add
发现爬虫已经全部失效了，但是又懒得维护，直接在下方分享了一些免费的ss账号信息

### 使用命令
爬虫不维护的话很快会失效，所有可以在网上找到免费的SS账号或者购买的ss账号，将账号信息添加到命令中对应位置即可。
下面是分享一些免费的ss账号的信息，使用期限未知：
```
服务器1：67.21.78.208 端口：7493 密码：dongtaiwang.com 加密方式：aes-256-cfb 
服务器2：104.160.185.150 端口：6123 密码：ntdtv.com 加密方式：aes-256-cfb 
服务器3：67.21.78.149 端口：1978 密码：dongtaiwang.com 加密方式：aes-256-cfb SSR协议：auth_sha1_v4 混淆：tls1.2_ticket_auth 
服务器4：104.160.185.80 端口：4810 密码：ntdtv.com 加密方式：aes-256-cfb SSR协议：auth_sha1_v4 混淆：tls1.2_ticket_auth 
服务器5：104.160.185.160 端口：6832 密码：ntdtv.com 加密方式：aes-256-cfb SSR协议：auth_sha1_v4 混淆：tls1.2_ticket_auth 
服务器6：47.74.132.157 端口：2345 密码：dongtaiwang.com 加密方式：aes-256-cfb SSR协议：auth_sha1_v4 混淆：tls1.2_ticket_auth 
服务器7：107.175.95.241 点此查看连接信息 
服务器8：107.175.94.126 点此查看连接信息 
服务器9：us.bilibilitv.pw 端口：16862 密码：namaho.org 加密方式：aes-256-cfb
服务器10：hk.bilibilitv.pw 端口：16862 密码：namaho.org 加密方式：aes-256-cfb
服务器11：jp.bilibilitv.pw 端口：16862 密码：namaho.org 加密方式：aes-256-cfb
服务器12：47.74.128.250 端口：2333 密码：ntdtv.com 加密方式：aes-256-cfb SSR协议：auth_sha1_v4 混淆：tls1.2_ticket_auth 
```
一个命令解决问题：	
```
sslocal -s 104.160.185.150 -p 6123 -l 1080 -k "ntdtv.com" -t 300 -m aes-256-cfb
```
买/找一个ss账号，将命令写在记事本中，重命名为ss.bat/ss.sh，运行即可
