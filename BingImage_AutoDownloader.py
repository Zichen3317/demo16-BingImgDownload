# -*- coding:utf-8 -*-
# ==========================================
#       author: ZiChen
#        mail: 1538185121@qq.com
#         time: 2021/04/17
# ==========================================

# 导入爬虫所需库
from bs4 import BeautifulSoup
import requests
import datetime
time = datetime.datetime.now()
str_time = datetime.datetime.strftime(time, "%Y-%m-%d")
print('Time: %s' % str_time)


def GetImage():
    """
    获得Bing壁纸
    """
    url = 'https://cn.bing.com'
    # 请求标头
    # 获取页面并转为dict格式
    req = requests.get(url=url)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, 'html.parser')  # 用BeautifulSoup库解析网页
    head = soup.head
    # 获得壁纸的地址，需要进行拼接
    ul = head.find('link')['href']
    imgUrl = 'https://cn.bing.com' + ul
    print('imgUrl= %s' % imgUrl)

    # 获取图片内容、将图片内容转换为二进制形式返回，以便上传至网盘
    imgRs = requests.get(url=imgUrl)
    path = "./%s.jpg" % str_time
    with open(path, 'wb') as f:
        f.write(imgRs.content)

    print('已将图片写入文件√')
    return path
