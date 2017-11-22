# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OschinaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bolg_title=scrapy.Field()
    bolg_remark=scrapy.Field()
    bolg_url=scrapy.Field()

class VideoItem(scrapy.Item):
    video_name = scrapy.Field()
    video_alias = scrapy.Field()
    video_actor = scrapy.Field()
    video_year = scrapy.Field()
    video_time = scrapy.Field()
    video_rating = scrapy.Field()
    video_votes = scrapy.Field()
    video_tags = scrapy.Field()
    video_url = scrapy.Field()
    video_director =scrapy.Field()
    video_type = scrapy.Field()
    video_bigtype = scrapy.Field()
    video_area = scrapy.Field()
    video_language = scrapy.Field()
    video_length = scrapy.Field()
    video_writer = scrapy.Field()
    video_desc = scrapy.Field()
    video_episodes = scrapy.Field()

class JDNotebookSipder(scrapy.Item):
    note_img=scrapy.Field()
    note_title = scrapy.Field()

class ImportNewSpiderItem(scrapy.Item):
    importnew_title=scrapy.Field()
    importnew_docurl=scrapy.Field()
    importnew_type=scrapy.Field()
    importnew_remark=scrapy.Field()
    importnew_imgurl=scrapy.Field()

class BestHotel58Item(scrapy.Item):
    hotel_title=scrapy.Field()
    hotel_price=scrapy.Field()
    hotel_lable=scrapy.Field()
    hotel_phonenume=scrapy.Field()
    hotel_time=scrapy.Field()
    hotel_lat=scrapy.Field()
    hotel_lon=scrapy.Field()
    hotel_detail=scrapy.Field()




