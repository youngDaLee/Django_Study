# -*- coding: utf-8 -*-
import scrapy

# Scrapy 환경설정
# 중요

# 실행방법
# 1.커맨드라인 실행 -> scrapy crawl 크롤러명 -s(--set) <NAME>=<VALUE>
# -> scrapy crawl test8 -s DOWNLOAD_DELAY=3

# 2.Spider 실행 시 직접 설정
# -> 아래 소스 참조

# 3.프로젝트 설정 파일
# -> settings.py

# 4.서브 명령어 (신경 X)

# 5.글로벌 설정 : scrapy.settings.default_settings


class TestSpider(scrapy.Spider):
    name = 'test8'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    # Spider 환경 설정
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 3
    # }

    def parse(self, response):
        # xpath + css 혼합
        for i, v in enumerate(response.xpath('//div[@class="post-summary-content"]').css('div.post-excerpt-container > h3 > a::text').extract(), 1):
            # 인덱스 번호, 헤드라인
            yield dict(num=i, headline=v)

