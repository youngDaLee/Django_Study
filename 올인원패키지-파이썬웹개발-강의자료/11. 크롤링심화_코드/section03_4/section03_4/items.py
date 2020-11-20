# Scrapy Item
# 장점 
# 1. 수집 데이터를 일관성있게 관리 가능
# 2. 데이터를 사전형(Dict)로 관리, 오타 방지
# 3. 추후 가공 및 DB 저장 용이

import scrapy


# Scrapy Item 연습
class ItArticle(scrapy.Item):
    # 제목
    title = scrapy.Field()
    # 이미지 URL
    img_url = scrapy.Field()
    # 본문 내용
    contents = scrapy.Field()
