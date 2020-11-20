from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


# 링크 크롤링 예제(중요)
# 사이트 요구에 맞는 환경 설정 세팅(중요)
class NewsSpider(CrawlSpider):
    name = 'test11'
    allowed_domains = ['media.daum.net']
    start_urls = ['https://media.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    rules = [
        # page=\d$ or page=\d+$ : 2자리수 페이지 크롤링
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline'),
    ]

    def parse_headline(self, response):
        # URL 로깅
        self.logger.info('Response URL : %s' % response.url)

        for m in response.css('ul.list_news2.list_allnews > li > div'):
            # 헤드라인
            headline = m.css('strong > a::text').extract_first().strip()
            # 본문 20글자
            contents = m.css('div > span::text').extract_first().strip()

            yield {'headline': headline, 'contents': contents}
