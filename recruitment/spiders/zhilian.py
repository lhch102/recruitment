# -*- coding: utf-8 -*-
import scrapy


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.13187805&x-zp-page-request-id=5d44b73f63294ac78177c0d2e84f2765-1548489193253-419607']

    def parse(self, response):
        # code = response['code']
        print("response:"+len(response))