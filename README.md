# demo16-BingImgDownload
##  作者：梓宸
### 介绍
Bing壁纸下载+利用网盘webdav功能进行转存
---
### 1.  文件说明
BingImage_AutoDownloader.py 必应壁纸下载模块  
ConsoleLog.py 日志写入及输出模块  
index.py 主程序 
---  
### 2.  使用说明
index.py中可以更改写入日志的路径  
程序会先将图片下载至程序所在的文件夹中，上传完毕后再根据.conf文件中"imageDelete"选项的设置来删除或保留图片
---
### Account.conf 文件格式
```
[TeraCloud_Backup]
url = xxx  _需要上传网盘的webdav地址，推荐使用teracloud，当然其他支持webdav的网盘也可以_ 
user = xxx  _用户名_ 
password = xxx  _密码（或授权码）_ 
imageDelete = False  _上传图片至网盘后是否删除用于上传的图片，默认为False（不删除）_ 
```
