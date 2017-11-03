import scrapy
from scrapy import Selector

class JdNotebookSpider(scrapy.Spider):
    name="JDNotebook"
    start_urls = ['https://list.jd.com/list.html?cat=670%2C671%2C672&go=0']

    def parse(self, response):
        note_img=response.xpath('//div[@id="plist"]//ul//li//div[@class="gl-i-wrap j-sku-item"]//div[@class="p-img"]//a//img').extract()
        for n_m in note_img:
            m=Selector(text=n_m)
            if len(m.xpath("//@src"))>0:
                print(m.xpath("//@src").extract())
            else:
                print(m.xpath("//@data-lazy-img").extract())
