# -*- coding: utf-8 -*-
from scrapy import cmdline
# 使用scrapy进行调试
name = 'aqi_history_spider_pyqt'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())