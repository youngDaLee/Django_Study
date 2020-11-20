# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SitesRankItems(scrapy.Item):
    # 제목
    rank_num = scrapy.Field()
    # 사이트 네임
    site_name = scrapy.Field()
    # 머문 시간
    daily_time_site = scrapy.Field()
    # 페이지뷰
    daily_page_view = scrapy.Field()
    # 파이프라인 통과 여부
    is_pass = scrapy.Field()
