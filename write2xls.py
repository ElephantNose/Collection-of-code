#!/usr/bin/env python
# coding=utf-8
# i=0 为第一行
# j=0 为第一列 

from xlwt import *

f = Workbook(encoding='utf-8')  # 打开文件
table = f.add_sheet('record')  # 创建表

with open('./data/' + nowstr + '/' + hours, 'r') as data:
    contents_list = data.readlines()

for i, contents in enumerate(contents_list):
    content = contents.split('\t')
    for j, everydata in enumerate(content):
        table.write(i, j , everydata)  # 用表的.write方法向第i+1行，j+1列写入数据

f.save('活动监控' + nowstr + '.xls')  # 保存文件

