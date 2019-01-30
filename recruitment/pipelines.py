# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class RecruitmentPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self,host,port,user,password,database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    @classmethod
    def from_crawler(cls,crawler):
        '''@classmethod:依赖注入'''
        return cls(
            host=crawler.settings.get("MYSQL_HOST"),
            port=crawler.settings.get("MYSQL_PORT"),
            user=crawler.settings.get("MYSQL_USER"),
            password=crawler.settings.get("MYSQL_PASS"),
            database=crawler.settings.get("MYSQL_DATABASE")
        )
    def open_spider(self,spider):
        ''' 负责连接数据库 '''
        self.db = pymysql.connect(self.host,self.user,self.password,self.database,self.port)
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        ''' 执行数据表的写入操作 '''
        # 组装SQL语句
        data = dict(item)
        keys = ",".join(data.keys())
        values = ",".join(['%s']*len(data))
        sql = "insert into %s (%s) values (%s)" % (item.table,keys,values)
        self.cursor.execute(sql,tuple(data.values()))
        self.db.commit()
        return item

    def close_spidder(self,spider):
        '''关闭数据库连接'''
        self.db.close()
