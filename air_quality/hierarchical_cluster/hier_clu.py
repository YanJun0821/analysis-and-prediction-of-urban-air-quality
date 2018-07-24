# -*- coding: utf-8 -*-
"""
    作者:     赵颜军
    版本:     2.0
    日期:     2018/05/25
"""
import pandas as pd
from scipy.cluster import hierarchy  #用于进行层次聚类，话层次聚类图的工具包
import matplotlib.pyplot as plt
from pylab import mpl
from Tkinter import END
import threading
import sys

reload(sys)

sys.setdefaultencoding('utf8')

def hier_clu(stext):
        stext.delete(1.0,END)
        stext.see(END)
        # 设置可为中文
        mpl.rcParams['font.sans-serif'] = ['SimHei']

        # 数据文件的路径
        filepath = '../File_data/ncity_air_quality_month.csv'

        # 读取csv数据文件
        pf_obj = pd.read_csv(filepath, encoding='utf-8')
        # 读数据进行分组
        final = pf_obj.groupby(by=['city_name'])['aqi'].mean()

        final_data = pd.DataFrame(final, index=final.index)

        Z = hierarchy.linkage(final_data, method='ward', metric='euclidean')
        plt.figure(1, figsize=(15, 7))

        hierarchy.dendrogram(Z, labels=final_data.index)

        # 根据linkage matrix Z得到聚类结果:
        cluster = hierarchy.fcluster(Z, t=1, depth=3)

        print "Original cluster by hierarchy clustering:\n", cluster

        # 暂时没有使用格式
        font = {'family': 'KaiTi',
                  'weight': 'normal',
                  'size': 15,
                  'color': 'blue'
        }

        plt.title("城市污染情况层次聚类图", fontsize=23, color = 'green',family = 'KaiTi')
        plt.xlabel('城市名称', font)
        plt.xticks(fontsize=13, family='KaiTi')
        # plt.savefig('hier_clu.png', dpi=100)
        stext.delete(1.0, END)
        stext.see(END)
        stext.insert(END, '第一类(污染情况严重)：石家庄，济南，郑州。\n第二类(污染情况较严重):乌鲁木齐，天津，北京，西安，太原，成都，武汉，合肥，沈阳，哈尔滨，兰州，南京。\n第三类(污染情况一般):湖州，呼和浩特，银川，长春，长沙，青岛，重庆，上海，杭州，绍兴，嘉兴，金华，西宁等。\n第四类(污染情况较轻):南昌，佛山，东莞，宁波，广州，台州，江门，温州，海口，中山，拉萨，丽水，南宁，厦门，昆明，深圳，珠海等。\n')
        stext.see(END)
        plt.show()


if __name__ == "__main__":
    hier_clu()
