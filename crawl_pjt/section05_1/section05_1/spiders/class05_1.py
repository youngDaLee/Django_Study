import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NewsSpider(CrawlSpider):
    name = 'test11'
    allowed_domains = ['news.daum.net']
    start_urls = ['http://news.daum.net/breakingnews']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    # page = \d$ : 1자리 수
    # page = \d+ : 연속, follow=True
    rules = [
        Rule(LinkExtractor(allow=r'/breakingnews\?page=\d$'), callback='parsd_headline', follow=True),
    ]

    def parse(self, response):
        # URL 로깅
        self.logger.info('Response URL : %s'% response.url)

        for m in response.css('ul.list_news2 list_allnews > li > div'):
            #헤드라인
            headline = m.css('strong > a::text').extract_first().strip()
            #본문 20글자
            contents = m.css('div > span::text ').extract_first().strip()

            yield {'headline':headline, 'contents' : contents}
