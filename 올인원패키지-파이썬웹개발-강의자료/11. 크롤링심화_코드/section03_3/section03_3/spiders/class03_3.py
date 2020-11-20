import scrapy


# xpath 선택자 도움 사이트
# https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
# http://www.nextree.co.kr/p6278/

# css 선택자 도움 사이트
# https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors

# 정규 표현식 중요
# https://www.w3schools.com/python/python_regex.asp

# 타겟 데이터는 크롬 개발자 도구 사용

# 선택자 연습 팁 : scrapy shell에서 테스트(효율성)
# scrapy shell 도메인

class TestSpider(scrapy.Spider):
    # 스파이더 이름(실행)
    name = 'test5'
    # 허용 도메인
    allowed_domains = ['w3schools.com/']
    # 시작 URL
    start_urls = ['https://www.w3schools.com/']

    # CSS 선택자
    # A B : 자손
    # A > B : 자식
    # ::text -> 노드 텍스트만 추출
    # ::attr(name) -> 노드 속성 값 추출
    # get(), getall() 사용 숙지
    # get(default='') 사용 가능

    # 예)
    # response.css('title::text').get() : 타이틀 태그의 텍스트만 추출
    # response.css('div > a::attr(href)').getall() : div 태그의 자식 a 태그 href 속성 값 전부 추출

    # Xpath 선택자
    # nodename : 이름이 nodename 선택
    # text() : -> 노드 텍스트만 추출
    # / : 루트부터 시작
    # // : 현재 node 부터 문서상의 모든 노드 조회
    # . : 현재 node
    # .. : 현재 node의 부모 노드
    # @ : 속성 선택자
    # excract(), extract_first() 사용 숙지

    # 예)
    # response.xpath('//div') : 루트 노드부터 모든 div 태그 선택
    # response.xpath('//div[@id="id1"]/a/text()').get() : div 태그 중 id가 'id1' 인 자식 a 태그의 텍스트 추출

    # 중요
    # get() == extract_first()
    # getall() == extract()

    # 혼합 사용 가능
    # response.css('img').xpath('@src').getall()

    # nav 메뉴 이름 크롤링 실습
    # 쉘 실행 -> 선택자 확인 -> 코딩 -> 데이터 저장
    def parse(self, response):
        # 둘다 가능
        # response.css('nav#mySidenav > div a::text').getall()
        # response.css('nav#mySidenav').xpath('./div//a/text()').extract()

        for n, text in enumerate(response.css('nav#mySidenav > div a::text').getall(), 1):
            # Return Type : Request, BaseItem, dictionary, None
            yield {'num': n, 'learn Title': text}
