# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitmentItem(scrapy.Item):
    # define the fields for your item here like:
    table = 'recruitment' # 表名
    id = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    type = scrapy.Field() #工作类型
    number = scrapy.Field()# 招聘人数
    duty = scrapy.Field()
    requirement = scrapy.Field()# 工作要求
    source = scrapy.Field() #来源
    salary = scrapy.Field() #薪水
    experience = scrapy.Field()#工作经验
