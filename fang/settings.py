

BOT_NAME = 'fang'
SPIDER_MODULES = ['fang.spiders']
NEWSPIDER_MODULE = 'fang.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

from fake_useragent import UserAgent
ua = UserAgent().random

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'User-Agent':ua
}

ITEM_PIPELINES = {
   'fang.pipelines.FangPipeline': 300,
    'fang.pipelines.MongoPipeline': 400,
}

MONGO_URI = 'localhost'
MONGO_DB = 'fangtianxia'