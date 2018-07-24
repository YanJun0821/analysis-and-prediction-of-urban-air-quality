# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirQualityItem(scrapy.Item):
    # 为数据集定义数据变量
    # 城市名称
    city_name = scrapy.Field()
    #
    date = scrapy.Field()
    # AQI数据的时间
    grade = scrapy.Field()
    # 范围
    aqi = scrapy.Field()
    # AQI数据的pm2.5的数值
    pm25 = scrapy.Field()
    # AQI数据的pm10的数值
    pm10 = scrapy.Field()
    # AQI数据的so2的数值
    so2 = scrapy.Field()
    # AQI数据的co的数值
    co = scrapy.Field()
    # AQI数据的no2的数值
    no2 = scrapy.Field()
    # AQI数据的o3的数值
    o3 = scrapy.Field()
    pass
