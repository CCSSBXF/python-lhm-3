import json

#将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_date = json.load(f)
#打印每一天的信息
# for btc_dict in btc_date:
#     date = btc_dict['date']
#     month = btc_dict['month']
#     week = btc_dict['week']
#     weekday = btc_dict['weekday']
#     close = btc_dict['close']
#     print("{} is month {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))
#     #format-----"{} {} {}".format( , , )

# #打印每一天的信息
# for btc_dict in btc_date:
#     date = btc_dict['date']
#     month = int(btc_dict['month'])
#     week = int(btc_dict['week'])
#     weekday = btc_dict['weekday']
#     close = int(float(btc_dict['close']))
#     print("{} is month {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))

#创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
#每一天的信息
for btc_dict in btc_date:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

import pygal
import math

# #日期标签沿顺时针旋转20度，不用显示所有x轴标签
# line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
# line_chart.title = '收盘价对数变换（￥）'
# line_chart.x_labels = dates
# N = 20  # x 坐标每隔20天显示一次
# line_chart.x_lables_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('log收盘价',close_log)
# line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')

from itertools import groupby

def draw_line(x_date,y_date,title,y_legend):
    xy_map = []
    #zip()将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    for x,y in groupby(sorted(zip(x_date,y_date)),key=lambda _:_[0]):
        y_list = [v for _,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],close[:idx_month],'收盘价月日均值（￥）','月日均值')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week],close[1:idx_week],'收盘价周日均值（￥）','周日均值')
line_chart_week

idx_week = dates.index('2017-12-11')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int,close[1:idx_week],'收盘价星期均值（￥）','星期均值')
line_chart_weekday.x_labels = ['周一','周二','周三','周四','周五','周六','周日']
line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')

with open('收盘价Dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图（￥）.svg','收盘价对数变换折线图（￥）.svg','收盘价月日均值（￥）.svg',
        '收盘价周日均值（￥）.svg','收盘价星期均值（￥）.svg'
        ]:
        html_file.write('    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')






