# -*- encoding=UTF-8 -*-

"""
    作者:     赵颜军
    版本:     2.0
    日期:     2018/06/5
"""

from Tkinter import *
import tkFont
from ScrolledText import ScrolledText
from regression_model.reg_model import getData
from hierarchical_cluster.data_vis import data_vis
from hierarchical_cluster.hier_clu import hier_clu
import pandas as pd
import threading
import os
from Tkinter import END

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    print(size)
    root.geometry(size)

def creatthread1():
    th = threading.Thread(target=threadgetDay, args=(stext,))
    th.setDaemon(True)
    th.start()


def threadgetDay(stext):
    stext.delete(1.0, END)
    stext.see(END)
    ncity_list = ['石家庄', '济南', '兰州', '西宁', '呼和浩特', '青岛', '银川', '哈尔滨', '合肥', '武汉', '成都', '长春', '南昌', '南京', '乌鲁木齐', '郑州',
                  '西安', '天津', '太原', '沈阳', '绍兴', '衢州', '长沙', '宁波', '南宁', '昆明','贵阳', '东莞', '中山', '广州', '江门', '肇庆', '台州', '上海', '温州', '佛山', '北京', '湖州', '金华', '重庆', '嘉兴', '杭州', '海口',
                  '福州', '深圳', '珠海', '丽水', '拉萨', '舟山', '厦门', '惠州']
    file_path = '../File_data/ncity_air_quality.csv'
    pf_obj = pd.read_csv(file_path, dtype=str)
    stext.insert(END, '整个城市集为:\n')
    for j in range(len(ncity_list)):
        stext.insert(END, ncity_list[j] + ',')
    stext.insert(END, '\n'+'每天的数据为:\n')
    stext.see(END)
    stext.insert(END, 'co,pm10,grade,o3,date,so2,pm25,city_name,aqi,no2\n')
    stext.see(END)
    for i in range(2000):
        try:
         stext.insert(END, pf_obj.loc[i, 'co'] + ',' + pf_obj.loc[i, 'pm10'] + ',' + pf_obj.loc[i, 'grade'] + ',' +pf_obj.loc[i, 'o3'] + ','+ pf_obj.loc[i, 'date'] + ',' + pf_obj.loc[i, 'so2'] + ',' + pf_obj.loc[i, 'pm25'] + ',' +pf_obj.loc[i, 'city_name'] + ','+ pf_obj.loc[i, 'aqi'] + ',' + pf_obj.loc[i, 'no2'] + '\n')
         stext.see(END)
        finally:
            print '输出每天数据'
    stext.insert(END, '每天的数据输出结束....')
    stext.see(END)

def creatthread2():
    th = threading.Thread(target=threadgetMonth, args=(stext,))
    th.setDaemon(True)
    th.start()

def creatthread(stext):
    th = threading.Thread(target=spiderExample, args=(stext,))
    th.setDaemon(True)
    th.start()

def spiderExample(stext):
    stext.delete(1.0, END)
    stext.see(END)
    stext.insert(END, '爬虫程序开始运行....')
    os.system("python runscrapy.py")
    file_path = '../File_data/ncity_air_quality_add.csv'
    pf_obj = pd.read_csv(file_path, dtype=str)
    stext.insert(END, '\n'+'爬取获得的数据集为:\n')
    stext.see(END)
    stext.insert(END, 'co,pm10,grade,o3,date,so2,pm25,city_name,aqi,no2\n')
    stext.see(END)
    for i in range(pf_obj.shape[0]):
        try:
         stext.insert(END, pf_obj.loc[i, 'co'] + ',' + pf_obj.loc[i, 'pm10'] + ',' + pf_obj.loc[i, 'grade'] + ',' +pf_obj.loc[i, 'o3'] + ','+ pf_obj.loc[i, 'date'] + ',' + pf_obj.loc[i, 'so2'] + ',' + pf_obj.loc[i, 'pm25'] + ',' +pf_obj.loc[i, 'city_name'] + ','+ pf_obj.loc[i, 'aqi'] + ',' + pf_obj.loc[i, 'no2'] + '\n')
         stext.see(END)
        finally:
            print '输出爬虫数据'
    stext.insert(END, '爬虫运行结束....')
    stext.see(END)




def threadgetMonth(stext):
    try:
        stext.delete(1.0, END)
        stext.see(END)
        ncity_list = ['石家庄', '济南', '兰州', '西宁', '呼和浩特', '青岛', '银川', '哈尔滨', '合肥', '武汉', '成都', '长春', '南昌', '南京', '乌鲁木齐', '郑州',
                      '西安', '天津', '太原', '沈阳', '绍兴', '衢州', '长沙', '宁波', '南宁', '昆明','贵阳', '东莞', '中山', '广州', '江门', '肇庆', '台州', '上海', '温州', '佛山', '北京', '湖州', '金华', '重庆', '嘉兴', '杭州', '海口',
                      '福州', '深圳', '珠海', '丽水', '拉萨', '舟山', '厦门', '惠州']
        file_path = '../File_data/ncity_air_quality_month.csv'
        pf_obj = pd.read_csv(file_path, dtype=str)
        stext.insert(END, '整个城市集为:\n')
        for j in range(len(ncity_list)):
            stext.insert(END, str(ncity_list[j])+',')
        stext.insert(END, '\n'+'每个月的数据为:\n')
        stext.see(END)
        stext.insert(END, 'co,pm10,grade,o3,date,so2,pm25,city_name,aqi,no2\n')
        stext.see(END)
        for i in range(pf_obj.shape[0]):
            try:
               stext.insert(END, pf_obj.loc[i, 'co']+','+pf_obj.loc[i, 'pm10']+','+pf_obj.loc[i, 'grade']+','+pf_obj.loc[i, 'o3']+','+ pf_obj.loc[i, 'date']+','+pf_obj.loc[i, 'so2']+','+pf_obj.loc[i, 'pm25']+','+pf_obj.loc[i, 'city_name']+','+ pf_obj.loc[i, 'aqi'] + ','+pf_obj.loc[i, 'no2']+'\n')
               stext.see(END)
            except TclError:
               print('输出每个月的数据')
        stext.insert(END, '每月的数据输出结束....')
        stext.see(END)
    finally:
        print '输出每个月的数据'

root = Tk()
root.title('基于回归模型的城市空气质量的污染程度的分析与实现')
ft1 = tkFont.Font(family='KaiTi', size=13)
center_window(root, 800, 500)
stext = ScrolledText(root, font=ft1,height = 800,width = 500)
stext.pack()
menubar = Menu(root)

# 创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Scrapy爬虫运行", command=lambda: creatthread(stext))
filemenu.add_command(label="城市集每天数据", command=lambda: creatthread1())
filemenu.add_command(label="城市集每个月数据", command=lambda: creatthread2())

# filemenu.add_separator()
menubar.add_cascade(label="数据爬虫模块", menu=filemenu)


# 创建聚类下拉菜单
datamenu = Menu(menubar, tearoff=0)
datamenu.add_command(label="层次聚类", command=lambda: hier_clu(stext))

menubar.add_cascade(label="数据层次聚类模块", menu=datamenu)


# 创建另一个下拉菜单Edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="第一类城市分析折线图", command=lambda: data_vis().broken_line_one(stext))
editmenu.add_command(label="第二类城市分析折线图",command=lambda: data_vis().broken_line_two(stext))
editmenu.add_command(label="第三类城市分析折线图",command=lambda: data_vis().broken_line_three(stext))
editmenu.add_command(label="第四类城市分析折线图",command=lambda: data_vis().broken_line_four(stext))
editmenu.add_command(label="第一类城市分析圆饼图",command=lambda: data_vis().pie_charts('合肥',stext))
editmenu.add_command(label="第二类城市分析圆饼图",command=lambda: data_vis().pie_charts('武汉',stext))
editmenu.add_command(label="第三类城市分析圆饼图",command=lambda: data_vis().pie_charts('上海',stext))
editmenu.add_command(label="第四类城市分析圆饼图",command=lambda: data_vis().pie_charts('深圳',stext))
menubar.add_cascade(label="数据可视化模块", menu= editmenu)

#创建下拉菜单Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="多线性回归模型训练拟合", command=lambda: getData(stext))

# helpmenu.add_command(label="test", command=lambda:test(stext))

menubar.add_cascade(label="回归算法训练拟合", menu=helpmenu)

#显示菜单
root.config(menu=menubar)

#初始说明
flow_doc = open('../File_data/flow_doc.txt', 'r')
help_doc = flow_doc.read()
stext.insert(END, help_doc)
root.font='Times'

# mainloop()
root.mainloop()