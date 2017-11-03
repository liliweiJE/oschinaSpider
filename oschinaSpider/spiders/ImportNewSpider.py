import scrapy
from oschinaSpider.items import ImportNewSpiderItem

class ImportNewSpider(scrapy.Spider):
    name = "importNewSpider"
    allowed_domains=["www.importnew.com"]
    start_urls=["http://www.importnew.com/all-posts"]

    def parse(self, response):
       # res=response.text()
       #print(response.text)
       docItems=response.xpath('//div[@id="archive"]//div[@class="post floated-thumb"]')
       #print(len(docItems))
       for doc in docItems:
           importnew=ImportNewSpiderItem()
           imgurls=doc.xpath('.//div[@class="post-thumb"]/a/img/@src').extract()
           if len(imgurls)>0:
               importnew["importnew_imgurl"]=imgurls[0]
           else:
               importnew["importnew_imgurl"]="null"
           importnew["importnew_title"]=doc.xpath('.//div[@class="post-meta"]/p/a[1]/text()').extract()[0]
           importnew["importnew_docurl"]=doc.xpath('.//div[@class="post-meta"]/p/a[1]/@href').extract()[0]
           importnew["importnew_type"]=doc.xpath('.//div[@class="post-meta"]/p/a[2]/text()').extract()[0]
           importnew["importnew_remark"]=doc.xpath('.//div[@class="post-meta"]/span/p/text()').extract()[0]
           yield importnew

       next_url=response.xpath('//div[@class="navigation margin-20"]//a[@class="next page-numbers"]//@href').extract()[0]
       if next_url:
           yield scrapy.Request(next_url, callback=self.parse)
       else:
           pass



