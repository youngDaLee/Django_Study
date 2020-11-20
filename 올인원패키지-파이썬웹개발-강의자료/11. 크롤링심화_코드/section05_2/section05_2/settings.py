# Scrapy settings for section05_2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'section05_2'

SPIDER_MODULES = ['section05_2.spiders']
NEWSPIDER_MODULE = 'section05_2.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 다운로드 간격
DOWNLOAD_DELAY = 2

# 쿠키 사용
COOKIES_ENABLED = True

# Referer 삽입
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://media.daum.net',
}

# User-Agent 미들웨어 사용
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}

# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 한글 쓰기(출력 인코딩)
FEED_EXPORT_ENCODING = 'utf-8'

# 캐시 사용
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
