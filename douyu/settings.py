# -*- coding: utf-8 -*-

# Scrapy settings for douyu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douyu'

SPIDER_MODULES = ['douyu.spiders']
NEWSPIDER_MODULE = 'douyu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douyu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_6cb79fa400f05b2f8cef7aebfa6e9bc7=1471529135; CNZZDATA1260122357=1353911948-1471527931-http%253A%252F%252Fwww.douyu.com%252F%7C1471527931; acf_usermsgnum1620379=0; acf_auth=26f4KlXyYfnk%2F8MX%2Bx1ugNXuNEY78PkNODex8Nq1d6DSJoGMcsLfWVGgVu%2BjqUISPvyZUQV%2FFfvLG3GTqQ%2BCgB72W8iyFKXCamaEACnKT8KDS2bI6ClCSOA; wan_auth37wan=eff065034ee7Ew78LVMb%2FeMmolOmMlbaO4v485Uq19PRq068ywc1f%2BGWtzJJbJ%2BBppQccA4EnRCOrOT5bOp1KJCo5qzNRew3Khk9mP378etZYnjX; acf_uid=1620379; acf_username=qq_7psqnZvH; acf_nickname=%E8%8B%A6%E7%93%9C%E6%9C%80%E8%BF%91%E5%BE%88%E5%BF%99; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=41740121; acf_biz=1; acf_stk=dfc4626e0e4a94b0; PHPSESSID=8tl8qbrkaa5ojqopg8dv73hnf6; acf_did=83DCFCF061DCA91F875A9113282CEE9D; _dys_lastPageCode=page_live,page_studio_normal; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1478172418,1478344608,1478346757,1478423057; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1478443360; acf_userletnum1620379=0",
    "Host": "www.douyu.com",
    "Referer": "https://www.douyu.com/directory/all",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"
    # X-Requested-With:XMLHttpRequest
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douyu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'douyu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'douyu.pipelines.MongoDBPipeline': 300,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "douyu"
MONGODB_COLLECTION = "all"

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
