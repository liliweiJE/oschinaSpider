import  scrapy
import re
from oschinaSpider.items import BestHotel58Item


class BestHotelSpider(scrapy.Spider):
    name="bestHotelSpider"

    allowed_domains = ["bj.58.com"]
    start_urls = ["http://bj.58.com/pinpaigongyu/"]

    def parse(self, response):
        hotel_list=response.xpath('//ul[@class="list"]//li//a//@href').extract()
        if hotel_list:
            for hotel_href in hotel_list:
                yield scrapy.Request("http://bj.58.com{}".format(hotel_href), callback=self.parse_item)
        next_url = response.xpath('//div[@class="page"]//a[@class="next"]//@href').extract()
        print(next_url)
        if next_url:
            yield scrapy.Request("http://bj.58.com{}".format(next_url[0]), callback=self.parse)

    def parse_item(self,response):
        hotel_title=response.xpath('//h2//text()').extract()
        hotel_lables=response.xpath('//div[@class="tags"]//ul[@class="tags-list"]//li//text()').extract()
        hotel_time=response.xpath('//div[@class="tags"]//span[@class="tips"]//text()').extract()
        hotel_price=response.xpath('//div[@class="detail_header"]//span[@class="price"]//text()').extract()
        hotel_phone=response.xpath('//div[@class="phonenum "]//text()').extract()
        hotel_details=response.xpath('//ul[@class="house-info-list"]//li//span//text()').extract()
        searchGroup=re.findall(r"____json4fe.lon = '\d+.\d+|____json4fe.lat = '\d+.\d+",response.text)
        item = BestHotel58Item()
        if len(searchGroup) ==2:
            item['hotel_lon']=searchGroup[0][searchGroup[0].find("'")+1:]
            item['hotel_lat']=searchGroup[1][searchGroup[1].find("'") + 1:]


        item['hotel_title']=hotel_title
        hotel_lable=','.join(hotel_lables)
        item['hotel_lable']=hotel_lable
        item['hotel_time']=hotel_time
        item['hotel_price']=hotel_price
        item['hotel_phonenume']=hotel_phone
        hotel_detail = ','.join(hotel_details)
        item['hotel_detail']=hotel_detail
        yield item

if __name__=="__main__":
    # url="http://bj.58.com/pinpaigongyu/32115538462670x.shtml?psid=165077117198038349587830901&iuType=p_0&PGTID=0d3111f6-0000-1f54-c5ec-3606c5ef7266&ClickID=1"
    # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    # headers = {'User_Agent': user_agent, 'Host': 'bj.58.com'}
    # req = urllib.request.Request(url=url, headers=headers)
    # response = urllib.request.urlopen(req)
    # res = response.read().decode()
    # searchGroup=re.findall(r"____json4fe.lon = '\d+.\d+|____json4fe.lat = '\d+.\d+",res)
    # print(searchGroup[0][searchGroup[0].find("'")+1:])
    # print(searchGroup[1][searchGroup[1].find("'") + 1:])
    #print(ProxyPoolUtil.get_proxy().decode())
    a=['1','2','3','4']
    b=','.join(a)
    print(b)