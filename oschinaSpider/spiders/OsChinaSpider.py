import scrapy

from oschinaSpider.items import OschinaspiderItem

class OsChinaSpider(scrapy.Spider):
    name="oschina"
    allowed_domains = ['www.oschina.net']
    start_urls = ['https://www.oschina.net/action/ajax/get_more_recent_blog?classification=5611447&p=1']

    def parse(self, response):
        item=OschinaspiderItem()
        bolg_title=response.xpath('//div[@class="box item"]//div[@class="box-aw"]//header//a//@title').extract()
        bolg_href = response.xpath('//div[@class="box item"]//div[@class="box-aw"]//header//a//@href').extract()
        bolg_remark = response.xpath('//div[@class="box item"]//div[@class="box-aw"]//section//text()').extract()
        for i in range(len(bolg_title)):
            item['bolg_title']=bolg_title[i]
            item['bolg_remark']=bolg_remark[i]
            item['bolg_url']=bolg_href[i]
            yield item

        for i in range (2,31):
            new_url="https://www.oschina.net/action/ajax/get_more_recent_blog?classification=5611447&p={0}".format(i)
            yield scrapy.Request(new_url,callback=self.parse)
