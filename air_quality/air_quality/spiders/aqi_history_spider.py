# -*- coding: utf-8 -*-
"""
    作者:     赵颜军
    版本:     1.0
    日期:     2018/03/20
"""
import scrapy
import time
import sys
import pandas as pd
from selenium import webdriver
from air_quality.items import AirQualityItem
reload(sys)
sys.setdefaultencoding('utf-8')


# 基础的数据源地址
# 网站稳定性显示较差
base_url = 'https://www.aqistudy.cn/historydata/daydata.php?city='
base_url1 = 'https://www.aqistudy.cn/historydata/monthdata.php?city='


class AqiHistorySpiderSpider(scrapy.Spider):
    name = "aqi_history_spider"
    allowed_domains = ["aqistudy.cn"]
    start_urls = ['https://www.aqistudy.cn/historydata/']
    # 初始化获取

    def parse(self, response):
        item = AirQualityItem()
        # 解析热门城市的数据地址
        hcity_list = response.xpath('//div[@class="hot"]//div[@class="bottom"]//a//text()').extract()
        # 解析所有的城市的数据地址
        # ncity_list = response.xpath('//div[@class="all"]//div[@class="bottom"]//a//text()').extract()
        ncity_list = ['石家庄', '济南', '兰州','西宁', '呼和浩特', '青岛','银川','哈尔滨', '合肥','武汉','成都','长春','南昌','南京','乌鲁木齐','郑州','西安','天津','太原','沈阳','绍兴','衢州','长沙','宁波','南宁','昆明',
                    '贵阳','东莞','中山','广州','江门','肇庆','台州','上海','温州','佛山','北京','湖州','金华','重庆','嘉兴','杭州','海口','福州','深圳','珠海','丽水','拉萨','舟山','厦门','惠州']
        driver = webdriver.Chrome('D:\guge\chromedriver.exe')

        def get_month_set(city):
            month_set = list()
            month_url = base_url1+city
            driver.get(month_url)
            time.sleep(5)
            dfs = pd.read_html(driver.page_source, header=0)[0]
            time.sleep(5)
            for j in range(0, len(dfs)):
                month_set.append(dfs.iloc[j, 0])
            # for i in range(1, 10):
            #     month_set.append(('2014-0%s' % i))
            # for i in range(10, 13):
            #     month_set.append(('2014-%s' % i))
            # for i in range(1, 10):
            #     month_set.append(('2015-0%s' % i))
            # for i in range(10, 13):
            #     month_set.append(('2015-%s' % i))
            # for i in range(1, 10):
            #     month_set.append(('2016-0%s' % i))
            # for i in range(10, 13):
            #     month_set.append(('2016-%s' % i))
            # for i in range(1, 10):
            #     month_set.append(('2017-0%s' % i))
            # for i in range(10, 13):
            #     month_set.append(('2017-%s' % i))
            # for i in range(1, 4):
            #     month_set.append(('2018-%s' % i))
            # print(month_set)
            return month_set

        def get_city_set(hcity_list):
            city_set = list()
            for line in hcity_list:
                city_set.append(line)
            # city_set.append('北京')
            # print(city_set)
            return city_set

        # print month_set
        city_set = get_city_set(ncity_list)

        for city in city_set:
            month_set = get_month_set(ncity_list)
            print(month_set)
            # file_name = city + '.csv'
            # fp = open(file_name, 'w')
            # 表头
            for i in range(len(month_set)):
                str_month = month_set[i]
                dateurl = base_url+city+'&month='+str_month
                print(dateurl)
                driver.get(dateurl)
                time.sleep(5)
                dfs = pd.read_html(driver.page_source, header=0)[0]
                time.sleep(5)

                for j in range(0, len(dfs)):
                    item['city_name'] = city
                    item['date'] = dfs.iloc[j, 0]  # 检测日期
                    item['aqi'] = dfs.iloc[j, 1]  # AQI
                    item['grade'] = dfs.iloc[j, 2]  # 范围
                    item['pm25'] = dfs.iloc[j, 3]  # PM2.5
                    item['pm10'] = dfs.iloc[j, 4]  # PM10
                    item['so2'] = dfs.iloc[j, 5]  # SO2
                    item['co'] = dfs.iloc[j, 6]  # CO
                    item['no2'] = dfs.iloc[j, 7]  # NO2
                    item['o3'] = dfs.iloc[j, 8]  # O3
                    yield item
                    # print('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (item['date'], item['aqi'], item['grade'], item['pm25'],
                    # item['pm10'], item['so2'], item['co'], item['no2'], item['o3']))
                    # fp.write(('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (date, aqi, grade, pm25, pm10, so2, co, no2, o3)))
                # print('%d---%s,%s---DONE' % (city_set.index(city), city, str_month))
            # fp.close()
        driver.quit()
        print ('爬虫已经爬完！数据已经生成！')






