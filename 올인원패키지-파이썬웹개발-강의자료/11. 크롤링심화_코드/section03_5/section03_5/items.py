import scrapy


class ItArticle(scrapy.Item):
    # 제목
    title = scrapy.Field()
    # 이미지 URL
    img_url = scrapy.Field()
    # 본문 내용
    contents = scrapy.Field()
