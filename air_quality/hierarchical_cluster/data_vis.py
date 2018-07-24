# -*- coding: utf-8 -*-
"""
    作者:     赵颜军
    版本:     1.0
    日期:     2018/04/10
"""
import pandas as pd
import datetime
import sys
from pylab import mpl
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from Tkinter import END
# 数据可视化
reload(sys)

sys.setdefaultencoding('utf8')
# 设置可为中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

filepath = '../File_data/ncity_air_quality_month.csv'
filepath1 = '../File_data/ncity_air_quality.csv'
myfont = matplotlib.font_manager.FontProperties(size=15)
pf_obj = pd.read_csv(filepath, dtype=str)
pf_obj1 = pd.read_csv(filepath1, dtype=str)
one_city = ['济南', '郑州', '石家庄']
two_city = ['合肥', '武汉', '南京' ]
three_city = ['青岛', '上海', '杭州']
four_city = ['厦门', '深圳', '广州']
'''
  
  饼状图
  
'''


class data_vis():
    def pie_charts(self, city_name,stext):
        stext.delete(1.0, END)
        labels = ['one', 'two', 'three', 'four', 'five', 'six']
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        quants = []
        for aqi in pf_obj1['aqi'][pf_obj1['city_name'] == city_name]:
            aqi = float(aqi)
            if  aqi >0 and aqi <= 50:
                one += 1
            if  aqi >50 and aqi <= 100:
                two += 1
            if  aqi >100 and aqi <= 150:
                three += 1
            if  aqi >150 and aqi <= 200:
                four += 1
            if aqi > 200 and aqi <= 300:
                five += 1
            if aqi >= 300:
                six += 1
        quants.append(one)
        quants.append(two)
        quants.append(three)
        quants.append(four)
        quants.append(five)
        quants.append(six)
        print(quants)
        data_vis.draw_pie(self,labels, quants, city_name)


    def draw_pie(self, labels,quants,city_name):
        # make a square figure
        plt.figure()
        plt.figure(1, figsize=(6, 6))
        # For China, make the piece explode a bit
        expl = [0,0.1,0,0,0,0]   #第二块即China离开圆心0.1
        # Colors used. Recycle if not enough.s
        colors = ["blue","red","coral","green","yellow","orange"]  #设置颜色（循环显示）
        # Pie Plot
        # autopct: format of "percent" string;百分数格式
        plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)
        plt.title(unicode(city_name+'饼状图'), bbox={'facecolor':'0.8', 'pad':5})
        # plt.savefig(unicode(city_name)+"pie.jpg")
        plt.show()
        # plt.close()


    '''
    
     绘制折线图
    
    '''


    def broken_line_one(self,stext):
        stext.delete(1.0, END)
        # 设置显示日期格式
        formatter = DateFormatter('%Y-%m')
        # print(pf_obj['aqi'][pf_obj['city_name'] == '济南'])
        plt.figure()
        ax = plt.gca()
        '''
            第一类污染城市折线图
        '''
        for city_name in one_city:
            # plt.figure()
            x = list()
            # print(city_name)
            for date in pf_obj['date'][pf_obj['city_name'] == city_name]:
                # print(date)
                datetimeObj = datetime.datetime.strptime(date, '%Y-%m').date()
                print(datetimeObj)
                x.append(datetimeObj)
                # print(ti.strptime(date, date_format))
            y = pf_obj['aqi'][pf_obj['city_name'] == city_name]
            z = map(lambda x: int(x), list(y))
            plt.plot_date(x, z, fmt="o", linestyle="-", marker="None", label=city_name)
            plt.legend(loc="upper right", prop=myfont)  # 显示图中的标签
            ax.set_xticklabels(x, rotation=30)
            ax.xaxis.set_major_formatter(formatter)
        plt.title(unicode("第一类城市污染情况变化折线图"), fontsize=15, color = 'green',family= 'KaiTi',bbox={'facecolor':'0.8', 'pad':5})
        font = {'family': 'KaiTi',
                  'weight': 'normal',
                  'size': 15,
                  'color': 'blue'
        }
        plt.xlabel('日期', font)
        plt.ylabel('aqi', font)
        fig = plt.gcf()
        fig.set_size_inches(15, 9)
        # fig.savefig(unicode('第一类城市污染情况变化折线图.png'), dpi=100)
        plt.show()

    def broken_line_two(self, stext):
        stext.delete(1.0, END)
        # 设置显示日期格式
        # plt.switch_backend('TKAgg')
        formatter = DateFormatter('%Y-%m')
        # print(pf_obj['aqi'][pf_obj['city_name'] == '济南'])
        fig, ax = plt.subplots()
        '''
           第二类污染城市折线图
        '''
        for city_name in two_city:
            x = list()
            print(city_name)
            for date in pf_obj['date'][pf_obj['city_name'] == city_name]:
                # print(date)
                datetimeObj = datetime.datetime.strptime(date, '%Y-%m').date()
                print(datetimeObj)
                x.append(datetimeObj)
                # print(ti.strptime(date, date_format))
            y = pf_obj['aqi'][pf_obj['city_name'] == city_name]
            z = map(lambda x :int(x), list(y))
            plt.plot_date(x, z, fmt="o", linestyle="-", marker="None", label=city_name)
            plt.legend(loc="upper right", prop=myfont)  # 显示图中的标签
            ax.set_xticklabels(x, rotation=30)
            ax.xaxis.set_major_formatter(formatter)
        plt.title(unicode("第二类城市污染情况变化折线图"), fontsize=15, color = 'green',family= 'KaiTi',bbox={'facecolor':'0.8', 'pad':5})
        font = {'family': 'KaiTi',
                  'weight': 'normal',
                  'size': 15,
                  'color': 'blue'
        }
        plt.xlabel(unicode('日期'), font)
        plt.ylabel('aqi', font)
        fig = plt.gcf()
        fig.set_size_inches(15, 9)
        # fig.savefig(unicode('第二类城市污染情况变化折线图.png'), dpi=100)
        plt.show()


    def broken_line_three(self,stext):
        stext.delete(1.0, END)
        # 设置显示日期格式
        formatter = DateFormatter('%Y-%m')
        # print(pf_obj['aqi'][pf_obj['city_name'] == '济南'])
        fig, ax = plt.subplots()
        '''                                                                              
            第三类污染城市折线图                                                                    
        '''
        for city_name in three_city:
            x = list()
            print(city_name)
            for date in pf_obj['date'][pf_obj['city_name'] == city_name]:
                # print(date)
                datetimeObj = datetime.datetime.strptime(date, '%Y-%m').date()
                print(datetimeObj)
                x.append(datetimeObj)
                # print(ti.strptime(date, date_format))
            y = pf_obj['aqi'][pf_obj['city_name'] == city_name]
            print(type(y))
            z = map(lambda x: int(x), list(y))
            plt.plot_date(x, z, fmt="o", linestyle="-", marker="None", label=city_name)
            plt.legend(loc="upper right", prop=myfont)  # 显示图中的标签
            ax.set_xticklabels(x, rotation=30)
            ax.xaxis.set_major_formatter(formatter)
        plt.title(unicode("第三类城市污染情况变化折线图"), fontsize=15, color = 'green',family= 'KaiTi',bbox={'facecolor':'0.8', 'pad':5})
        font = {'family': 'KaiTi',
                  'weight': 'normal',
                  'size': 15,
                  'color': 'blue'
        }
        plt.xlabel(unicode('日期'), font)
        plt.ylabel('aqi', font)
        fig = plt.gcf()
        fig.set_size_inches(15, 9)
        # fig.savefig(unicode('第三类城市污染情况变化折线图.png'), dpi=100)
        plt.show()

    def broken_line_four(self,stext):
        stext.delete(1.0, END)
        # 设置显示日期格式
        formatter = DateFormatter('%Y-%m')
        # print(pf_obj['aqi'][pf_obj['city_name'] == '济南'])
        fig, ax = plt.subplots()
        '''
            第四类污染城市折线图
        '''
        for city_name in four_city:
            # plt.figure()
            x = list()
            # print(city_name)
            for date in pf_obj['date'][pf_obj['city_name'] == city_name]:
                # print(date)
                datetimeObj = datetime.datetime.strptime(date, '%Y-%m').date()
                print(datetimeObj)
                x.append(datetimeObj)
                # print(ti.strptime(date, date_format))
            y = pf_obj['aqi'][pf_obj['city_name'] == city_name]
            print(type(y))
            z = map(lambda x: int(x), list(y))
            plt.plot_date(x,z, fmt="o", linestyle="-", marker="None", label=city_name)
            plt.legend(loc="upper right",prop=myfont )  # 显示图中的标签
            ax.set_xticklabels(x, rotation=60)
            ax.xaxis.set_major_formatter(formatter)
        plt.title("第四类城市污染情况变化折线图", fontsize=15, color = 'green',family= 'KaiTi',bbox={'facecolor':'0.8', 'pad':5})
        font = {'family': 'KaiTi',
                  'weight': 'normal',
                  'size': 15,
                  'color': 'blue'
        }
        plt.xlabel('日期', font)
        plt.ylabel('aqi', font)
        fig = plt.gcf()
        fig.set_size_inches(16.5, 9.5)
        # fig.savefig(unicode('第四类城市污染情况变化折线图.png'), dpi=100)
        plt.show()


    def hot_spot(self):
        print("热点图")


if __name__ == "__main__":
    broken = data_vis()
    broken.broken_line_one()
    # broken.broken_line_two()
    # broken.broken_line_three()
    # broken.broken_line_four()
    broken.pie_charts('郑州')
    broken.pie_charts('武汉')
    broken.pie_charts('上海')
    broken.pie_charts('深圳')