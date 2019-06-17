

BOT_NAME = 'fang'
SPIDER_MODULES = ['fang.spiders']
NEWSPIDER_MODULE = 'fang.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0.25


DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

ITEM_PIPELINES = {
   # 'fang.pipelines.FangPipeline': 300,
   'fang.pipelines.MongoPipeline': 400,
    'fang.pipelines.MysqlTwistedPipline': 420,
}

DOWNLOADER_MIDDLEWARES = {
    'fang.middlewares.UserAgent': 300,
}


# B、建立MongoDB连接
MONGO_URI = 'localhost'
MONGO_DB = 'fangtianxia'
MONGO_USERNAME = 'root'
# MONGO_PASSWORD = '123456'

#在CentOs下写入数据需要使用账号密码连接
# MONGO_URI = '139.155.96.221'
MONGO_PASSWORD = 'Mongo_Lei'
# MONGO_URL = 'mongodb://root:123456@192.168.43.68:27017'

# C、建立MySQL连接
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'fangtianxia'
MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'

# MYSQL_HOST = '139.155.96.221'
MYSQL_PASSWORD = 'Sql_Lei'