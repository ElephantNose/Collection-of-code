# encoding:utf-8

import csv
import codecs  # 支持写入中文

fileHeader = ['i号', '规则', '活动/资源位', '发出时间']
with open("jiankong.csv", "w") as csvFile:
    csvFile.write(codecs.BOM_UTF8)  # 支持写入中文
    writer = csv.writer(csvFile)  # 获取writer
    writer.writerow(fileHeader)  # 用.writerow方法写入数据，数据为列表，依次写入列表中的元素，写完列表自动换行
    with open('./data/' + nowstr + '/' + hours, 'r') as data:
        contents_list = data.readlines()
        for content in contents_list:
            writer.writerow(content.split('\t'))
