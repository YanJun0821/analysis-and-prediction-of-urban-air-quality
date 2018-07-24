# -*- coding: utf-8 -*-
#导入必要的模块
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filepath = '../File_data/ncity_air_quality.csv'
pf_obj = pd.read_csv(filepath, dtype=str)
# 产生测试数据
fig = plt.figure()
ax1 = fig.add_subplot(111)
#  设置标题
ax1.set_title('Scatter Plot')
# 设置X轴标签
plt.xlabel('co')
# 设置Y轴标签
plt.ylabel('aqi')
# 画散点图
ax1.scatter(list(pf_obj['co']), pf_obj['aqi'], c='r', marker='o')
# 设置图标
plt.legend('x1')
# 显示所画的图
plt.show()