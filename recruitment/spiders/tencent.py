# -*- coding: utf-8 -*-
import scrapy
from recruitment.items import RecruitmentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        '''解析当前招聘信息的url地址'''
        detail_urls = response.selector.css('tr.even a::attr(href),tr.odd a::attr(href)').extract()
        # 遍历
        for url in detail_urls:
            #构建绝对的url地址，效果同上（域名加相对地址）
            fullurl = response.urljoin(url)
            yield scrapy.Request(url=fullurl,callback=self.parse_page)
        #获取下一页的url地址
        next_url = response.selector.css('#next::attr(href)').extract_first()
        if next_url != 'javascript:;':
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url,callback=self.parse)
    def parse_page(self,response):
        '''解析具体的招聘信息详情'''
        item = RecruitmentItem()
        item['id'] = response.selector.re_first('applyPosition\(([0-9]+)\)')
        item['title'] = response.selector.css('#sharetitle::text').extract_first()
        item['location'] = response.selector.re_first('<span class="lightblue l2">工作地点：</span>(.*?)</td')
        item['type'] = response.selector.re_first('<span class="lightblue">职位类别：</span>(.*?)</td>')
        item['number'] = response.selector.re_first('<span class="lightblue">招聘人数：</span>([0-9]+)人</td>')
        duty = response.selector.xpath('//table//tr[3]//li/text()').extract()
        item['duty'] = '|'.join(duty)
        requirement = response.selector.xpath('//table//tr[4]//li/text()').extract()
        item['requirement'] = '|'.join(requirement)
        item['source'] = 'tencent'
        # print(hr)
        # 交给管道文件
        yield item