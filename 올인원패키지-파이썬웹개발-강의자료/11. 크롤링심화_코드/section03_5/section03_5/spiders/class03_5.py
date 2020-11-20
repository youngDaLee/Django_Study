import scrapy

from ..items import ItArticle


# Scrapy Feed Export 실습
# https://www.itnews.com/ 크롤링 연습

# 출력 형식
# JSON, JSON lines
# CSV
# XML
# Pickle, Marshal

# 저장 위치
# Local filesystem - (My PC)
# FTP - (Server)
# S3 - (Amazon)
# Standard Console - 기본 콘솔

# 방법 2가지
# 1. 커맨드 이용 (--output, -o + --output-format, -t)
#    로컬 경로시 예) file:///C:/test.csv
#    옵션 설정 예) --set=FEED_EXPORT_INDEX=2 or -s set=FEED_EXPORT_INDEX=2
# 2. Settings.py 설정

class TestSpider(scrapy.Spider):
    name = 'test7'
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

        yield item
