# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import re
class MmtuPipeline(object):
    def __init__(self):
        self.filepath = 'F:\mmimg'
    def process_item(self, item, spider):
        for k,v in item.items():
            newfilepath = os.path.join(self.filepath, k)
            if os.path.exists(newfilepath):
                print('%s:存在'%newfilepath)
            else:
                try:
                    os.mkdir(newfilepath)
                    for src in v:
                        try:
                            r = requests.get(src)
                            imgname = re.findall(r'.*/(.*?.jpg)@.*',src)[0]
                            imgfilename = os.path.join(self.filepath,k,imgname)
                            with open(imgfilename,'wb')as f:
                                f.write(r.content)
                        except:
                            continue
                except:
                    print('文件夹创建出现异常')
        return item
