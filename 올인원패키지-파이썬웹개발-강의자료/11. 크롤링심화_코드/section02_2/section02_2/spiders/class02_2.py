import scrapy


class TestSpider(scrapy.Spider):
    # 페이지 순회 크롤링 예제
    name = 'test3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    # 메인 페이지 순회
    def parse(self, response):
        """
        :param : response
        :return: Request
        """
        # response.css('div.post-item > div > a::attr("href")').getall()
        # response.css('div.post-item > div > a::attr("href")').extract()
        # response.xpath('//div[@class="post-item"]/div/a/@href').getall()
        # response.xpath('//div[@class="post-item"]/div/a/@href').extract()

        for url in response.css('div.post-item > div > a::attr("href")').getall():
            # url 보다 urljoin 사용
            yield scrapy.Request(response.urljoin(url), self.parse_title)

    # 상세 페이지 순회
    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param response: 
        :return Contents Text :
        """
        contents = response.css('div.post-body > span > p::text').extract()[:5]

        yield {'contents': ''.join(contents)}
