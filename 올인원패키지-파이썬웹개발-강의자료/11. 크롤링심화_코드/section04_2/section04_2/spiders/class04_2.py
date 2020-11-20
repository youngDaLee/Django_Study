# -*- coding: utf-8 -*-
import scrapy
from ..items import SitesRankItems


class TestSpider(scrapy.Spider):
    name = 'test9'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://www.alexa.com/topsites/']

    def parse(self, response):
        """
        :param : response
        :return: SitesRankItems
        """
        for p in response.css('div.listings.table > div.tr.site-listing'):
            # 아이템 객체 생성
            item = SitesRankItems()
            item['rank_num'] = p.xpath('div[@class="td"]/text()').get()
            item['site_name'] = p.xpath('div[@class="td DescriptionCell"]/p/a/text()').get()
            item['daily_time_site'] = p.xpath('div[@class="td right"]/p/text()').getall()[0]
            item['daily_page_view'] = p.xpath('div[@class="td right"]/p/text()').getall()[1]

            yield item
