# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2)
# pip install lxml, requests, cssselect

import requests
from lxml.html import fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """
    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = session.get("https://www.naver.com") # GET, POST

    # 신문사 링크 딕셔너리 획득
    urls = scraps_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)

    # 결과 출력
    for name, url in urls.items():
        # url 출력
        print(name, url)
        # 파일 쓰기

def scraps_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    for a in root.xpath('//div[@class="thumb_area"]/div'):
        # a 구조 확인
        # print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        name, url = extract_contents(a)
        # 딕셔너리 삽입
        urls[name] = url

    return urls

def extract_contents(dom):
    # 링크 주소
    link = dom.xpath('./div/a[3]').get('href')

    # 신문사 명
    name = dom.xpath('./a/img').get('alt')

    return name, link

# 스크랩핑 시작
if __name__ == "__main__":
    main()