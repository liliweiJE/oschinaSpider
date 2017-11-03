# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from oschinaSpider import settings

class OschinaspiderPipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True
        )
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        try:
            print("""insert into oschina_blog(blog_title,blog_remark,blog_url)
                value (%s,%s,%s)""",
                (item['bolg_title'],
                item['bolg_remark'],
                 item['bolg_url']))
            self.cursor.execute(
                """insert into oschina_blog(blog_title,blog_remark,blog_url)
                value (%s,%s,%s)""",
                (item['bolg_title'],
                item['bolg_remark'],
                 item['bolg_url']))
            self.connect.commit()
        except Exception as e:
            print(e)
        return item

class DoubanspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ImportnewSpiderPipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True
        )
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into importnew_doc(title,type_c,docurl,imgurl,remark,create_time) value (%s,%s,%s,%s,%s,now())""",
                (item['importnew_title'],
                item['importnew_type'],
                 item['importnew_docurl'],item['importnew_imgurl'],item['importnew_remark']))
            self.connect.commit()
        except Exception as e:
            print(e)
        return item