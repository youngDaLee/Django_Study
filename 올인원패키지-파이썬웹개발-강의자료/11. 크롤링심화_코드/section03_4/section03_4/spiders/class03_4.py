import scrapy

from ..items import ItArticle


# Scrapy Item 실습
# https://www.itnews.com/ 크롤링 연습

class TestSpider(scrapy.Spider):
    name = 'test6'
    allowed_domains = ['itnews.com']
    start_urls = ['https://itnews.com/']

    # 메인 페이지 순회
    def parse(self, response):
        """
        :param : response
        :return: Request
        """

        for url in response.css('div.news-item > div.hed > div.title > a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    # 상세 페이지 순회
    def parse_article(self, response):
        """
        상세 페이지 -> 타이틀, URL, 컨텐츠 추출
        :param response:
        :return Items :
        """

        # 아이템 객체 생성
        item = ItArticle()
        item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item['img_url'] = response.xpath('//img[@itemprop="contentUrl"]/@src').get()
        item['contents'] = ''.join(response.xpath('//div[@itemprop="articleBody"]/p/text()').getall())

        # dict 자료형의 모든 메소드 사용 가능
        # print(dict(item))
        # print(dir(dict(item)))
        yield item
