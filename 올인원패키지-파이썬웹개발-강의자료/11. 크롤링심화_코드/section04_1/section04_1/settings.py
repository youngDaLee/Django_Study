# -*- coding: utf-8 -*-

# Scrapy settings for section04_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'section04_1'

SPIDER_MODULES = ['section04_1.spiders']
NEWSPIDER_MODULE = 'section04_1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-1
# UserAgent 설정
# USER_AGENT = 'section04_1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 타겟 사이트 Robots.txt 규칙 준수 여부
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 병렬 처리
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 다운로드 딜레이
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# 웹 사이트 도메인 동시 병렬 처리 개수
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 특정 웹 사이트 IP 주소 병렬 처리 개수
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 쿠키 활성화 여부
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 기본 Request 헤더
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 미들웨어 사용 여부
# SPIDER_MIDDLEWARES = {
#    'section04_1.middlewares.Section041SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 특정 다운로드 미들웨어 사용
# DOWNLOADER_MIDDLEWARES = {
#    'section04_1.middlewares.Section041DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# 익스텐션 사용 여부
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 파이프라인 설정
# ITEM_PIPELINES = {
#    'section04_1.pipelines.Section041Pipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 캐시 사용 여부
# 캐시를 사용하면 동일하게 여러 번 요청 시 서버 사이드에 부하 절감 가능(변동사항 없을 경우)
# HTTPCACHE_ENABLED = True
# 캐시 유효 기간
# HTTPCACHE_EXPIRATION_SECS = 0
# 캐시 저장 경로
# HTTPCACHE_DIR = 'httpcache'
# 응답 거부 캐시
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 오류 처리
# 자동 재시도 설정
# RETRY_ENABLED = True

# 재시도 횟수 최대값
# RETRY_TIMES = 2

# 재시도 대상 HTTP 코드
# RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

# 오류 무시 HTTP 상태 코드
# HTTPERROR_ALLOWED_CODES = [404]

# 모든 상태 코드 오류 무시
# HTTPERROR_ALLOW_ALL = FALSE
