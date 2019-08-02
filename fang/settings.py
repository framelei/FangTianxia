

BOT_NAME = 'fang'
SPIDER_MODULES = ['fang.spiders']
NEWSPIDER_MODULE = 'fang.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0.1
CONCURRENT_REQUESTS = 16

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

ITEM_PIPELINES = {
   # 'fang.pipelines.MongoPipeline': 400,
    'fang.pipelines.MysqlTwistedPipline': 420,
}

DOWNLOADER_MIDDLEWARES = {
    'fang.middlewares.UserAgent': 300,
    'fang.middlewares.ProxyMiddleware': 301,
    'fang.middlewares.Captcha_Middleware': 302,
}

# B、建立MongoDB连接
MONGO_URI = 'localhost'
MONGO_DB = 'fangtianxia'
MONGO_USERNAME = 'root'

#在CentOs下写入数据需要使用账号密码连接
# MONGO_URI = '139.155.96.221'
MONGO_PASSWORD = 'Mongo_Lei'
# MONGO_URL = 'mongodb://root:123456@192.168.43.68:27017'

# C、建立MySQL连接
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'fangtianxia'
MYSQL_USER = 'root'

# MYSQL_HOST = '139.155.96.221'
MYSQL_PASSWORD = 'Sql_Lei'


# D、代理url
PROXY_URL = 'http://129.28.200.147:5557/random'

# E、设置日志级别，保存信息
LOG_LEVEL = "INFO"
import datetime
startDate = datetime.datetime.now().strftime('%Y%m%d')
LOG_FILE=f"NewHouse{startDate}.txt"

# F、设置最大等待时间、失败重试次数
#默认响应时间是180s，长时间不释放会占用一个并发量影响效率
DOWNLOAD_TIMEOUT = 10
# 是否进行失败重试
RETRY_ENABLED = True
# 失败重试的次数，连续失败3次后会抛出TimeOut异常被errback捕获
RETRY_TIMES = 3