import scrapy


class TestSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        print('dir', dir(response))
        print()
        print('headers', response.headers)
        print()
        print('meta', response.meta)
        print()
        print('encoding', response.encoding)
        print()
        print('status', response.status)
        print()
        # print('body', response.body)
        print()
        print('text', response.body)
