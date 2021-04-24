from webdav4.client import Client
from webdav4.client import ResourceAlreadyExists
import configparser
import BingImage_AutoDownloader
from os import remove
import ConsoleLog
import sys

log = ConsoleLog.ConsoleLog(
    'C:\\Users\\Administrator\\desktop\\', 'BingImage_AutoDownloader')

#  实例化configParser对象
config = configparser.ConfigParser()
major_Version_Number = 0  # 主版本号
child_Version_Number = 1  # 子版本号
stage_Version_Number = 3  # 阶段版本号
stage_VisionLst = ['base', 'alpha', 'beta', 'RC', 'release']
vision_Date = '210424' + '_' + stage_VisionLst[1]  # 日期和希腊字母版本号
vision = '%s.%s.%s.%s' % (major_Version_Number,
                          child_Version_Number,
                          stage_Version_Number,
                          vision_Date)
log.debug(vision, 'Main')
print('版本:%s' % vision)


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
        client.upload_file(from_path=imagePath, to_path='./%s' %
                           imagePath.split('/')[-1], overwrite=False)
        log.debug('已上传√ (%s)' % imagePath.split('/')
                  [-1], sys._getframe().f_code.co_name)
        print('已上传√ (%s)' % imagePath.split('/')[-1])
        # 读取设置中是否保留下载的文件
        if config['TeraCloud_Backup']['imageDelete'] != 'False':
            log.debug('已删除上传文件(%s)' % imagePath.split('/')[-1],
                      sys._getframe().f_code.co_name)
            print('已删除上传文件(%s)' % imagePath.split('/')[-1])
            remove(imagePath)  # 上传完毕后删除本地文件
        else:
            log.debug('已保留上传文件(%s)' % imagePath.split('/')[-1],
                      sys._getframe().f_code.co_name)
            print('已保留上传文件(%s)' % imagePath.split('/')[-1])

    except ResourceAlreadyExists:
        log.error('检测到 (%s) 已存在网盘中' % imagePath.split(
            '/')[-1], sys._getframe().f_code.co_name)
        print('检测到 (%s) 已存在网盘中' % imagePath.split('/')[-1])
        # 读取设置中是否保留下载的文件
        if config['TeraCloud_Backup']['imageDelete'] != 'False':
            remove(imagePath)  # 上传完毕后删除本地文件
            log.debug('已删除上传文件(%s)' % imagePath.split('/')[-1],
                      sys._getframe().f_code.co_name)
            print('已删除上传文件(%s)' % imagePath.split('/')[-1])
        else:
            log.debug('已保留上传文件(%s)' % imagePath.split('/')[-1],
                      sys._getframe().f_code.co_name)
            print('已保留上传文件(%s)' % imagePath.split('/')[-1])


main_handler(BingImage_AutoDownloader.GetImage(),
             "./Account.conf")
