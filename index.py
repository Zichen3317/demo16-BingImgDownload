from webdav4.client import Client
import configparser
import traceback
import BingImage_AutoDownloader
from os import remove

#  实例化configParser对象
config = configparser.ConfigParser()
vision = '0.1.0.210418_alpha'


def main_handler(imagePath, configfile):
    '''
    imageStr 图片的二进制文本
    configfile 设置文件路径
    '''

    config.read(configfile, encoding='utf-8')
    # username 为账号，password 为密码
    client = Client(base_url='%sBing壁纸' % config['TeraCloud_Backup']['url'],
                    auth=('%s' % config['TeraCloud_Backup']['user'],
                          '%s' % config['TeraCloud_Backup']['password']))

    # 上传壁纸
    try:
        client.upload_file(from_path=imagePath, to_path='./%s.jpg' %
                           imagePath.split('/')[-1], overwrite=False)
        print('已上传√ (%s)' % imagePath.split('/')[-1])
        if config['TeraCloud_Backup']['imageDelete'] != 'False':
            remove(imagePath)  # 上传完毕后删除本地文件
    except:
        if config['TeraCloud_Backup']['imageDelete'] != 'False':
            remove(imagePath)  # 上传完毕后删除本地文件
        traceback.print_exc()


main_handler(BingImage_AutoDownloader.GetImage(),
             "./Account.conf")
