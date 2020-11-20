import scrapy


class TestSpider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response 
        :return: Title Text
        """
        # 아래 4개 다 가능
        # response.css('div.post-header h2 a::text').getall() <-> get()
        # response.css('div.post-header h2 a::text').extract() <-> extract_first()
        # response.xpath('//div[@class="post-header"]/h2/a/text()').getall() <-> get()
        # response.xpath('//div[@class="post-header"]/h2/a/text()').extract() <-> extract_first()

        # 예제1
        # for text in response.css('div.post-header h2 a::text').getall():
        #     # Return Type : Request, BaseItem, dictionary, None
        #     yield {'text': text}

        # 예제2
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
            # Return Type : Request, BaseItem, dictionary, None
            yield {
                'num': i,
                'text': text
            }

        # 출력 옵션
        # -o 파일명.확장자 -t 파일 타입(json, jsonline, jl, csv, xml, marshal, pickle)
