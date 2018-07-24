# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


class AirQualityItemCsvPipeline(object):
    # 初始化指定文件
    def open_spider(self, spider):
        self.file = open('../File_data/ncity_air_quality_add.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
    # 处理结束后进行关闭 文件IO流
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    # 进行数据存储
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
