# Scrapy settings for section05_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'section05_1'

SPIDER_MODULES = ['section05_1.spiders']
NEWSPIDER_MODULE = 'section05_1.spiders'

# User_Agent 설정
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# 다운로드 간격
DOWNLOAD_DELAY = 2


# 쿠키 사용
COOKIES_ENABLED = True

# Referer 삽입
DEFAULT_REQUEST_HEADERS = {
  'Referer': 'https://news.daum.net/',
}

# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 한글 쓰기(출력 인코딩)
FEED_EXPORT_ENCODING = 'utf-8'


# 캐시 사용
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
