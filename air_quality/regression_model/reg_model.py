# -*- coding: utf-8 -*-
"""
    作者:     赵颜军
    版本:     1.0
    日期:     2018/04/03
"""
import pandas as pd
import numpy as np
import threading
from Tkinter import END
from sklearn.model_selection import train_test_split


'''
AQI等级分类：
1.0-50：优, 绿色
2.51-100：良,黄色
3.101-150：轻度污染,橙色
4.151-200：中度污染,红色
5.201-300:重度污染，紫色
6.>300:严重污染,褐红色
'''
'''
  数据源路径（爬虫后生成的文件）
'''


filepath = '../File_data/ncity_air_quality.csv'
createfile = '../File_data/ccity_air_quality.csv'

'''
  文件的读取 以及数据的预处理,数据格式处理,新的相应的符合要求的文件，可以生成在这里生成文件以便进行测试工作
'''


def load_file():
    # pandas读取数据文件
    pf_obj = pd.read_csv(filepath, encoding='utf-8', dtype=str)
    pf_obj.insert(pf_obj.ix[0].count()-1, 'city_name', pf_obj.pop('city_name'))
    pf_obj.insert(pf_obj.ix[0].count()-1, 'date', pf_obj.pop('date'))
    pf_obj.insert(pf_obj.ix[0].count()-1, 'grade', pf_obj.pop('grade'))
    pf_obj.insert(pf_obj.ix[0].count()-4, 'aqi', pf_obj.pop('aqi'))
    print(pf_obj)
    # pf_obj.to_csv(createfile, index=None, encoding='utf-8')
    return pf_obj

''' 
  损失函数的计算

'''


def compute_cost(x, y, theta):
    m = y.shape[0]   # 计算数据的个数
    # print(m)
    # 计算损失函数总和的值
    J = (np.sum((x.dot(theta)-y)**2))/(2*m)
    # print(J)
    return J

'''
  进行梯度下降
'''


def gradient_descent(X, y, theta, alpha, num_iters):
        m = y.shape[0]
        # print(m)
        # 存储历史误差
        J_history = np.zeros((num_iters, 1))
        for iter in range(num_iters):
            theta = theta - (alpha / m) * (X.T.dot(X.dot(theta) - y))
            J_history[iter] = compute_cost(X, y, theta)
            # print(theta)
        return J_history, theta
# 数据模型的拟合


'''
  数据特征的归一化
'''

def feature_nor(X,stext):
    # 均值的计算
    mea = np.mean(X, axis=0, dtype=float)
    # print(mea)
    # 方差的计算
    std = np.std(X, axis=0, dtype=float)
    # print(std)
    X_nomal = (X-mea)/std
    return X_nomal, mea, std

'''
   数据拟合优度的计算
'''

def r2(y_test, y_true):
    return 1 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum()

def start1(stext):
    stext.delete(1.0, END)
    stext.see(END)
    # 数据处理·
    np.set_printoptions(suppress=True)
    iterations = 10000  # 迭代次数
    alpha = 0.1  # 学习率
    theta = np.zeros((7, 1))
    data = load_file()
    stext.insert(END, '读取数据集.........\n')
    stext.see(END)
    x = np.array(data.iloc[:, 0:6], dtype=float).reshape((-1, 6))
    y = np.array(data.iloc[:, 6], dtype=float).reshape((-1, 1))
    # 交叉验证
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    print '训练集为:'
    stext.insert(END, '交叉验证(7:3).........\n')
    stext.insert(END, '训练集为:\n')
    stext.see(END)
    final_train = np.hstack((X_train, y_train))
    stext.insert(END, str(final_train) + '\n')
    stext.see(END)
    stext.insert(END, '测试集为:\n')
    stext.see(END)
    final_test = np.hstack((X_test, y_test))
    stext.insert(END, str(final_test) + '\n')
    stext.see(END)
    print X_test
    print y_test
    print '训练集为:'
    print X_train
    print y_train
    m = y_train.shape[0]
    stext.insert(END, '特征归一化处理开始........\n')
    stext.see(END)
    X_train, mean, std = feature_nor(X_train,stext)
    stext.insert(END, '特征归一化结果:\n'+str(X_train)+'\n')
    stext.see(END)
    X_train = np.hstack([X_train, np.ones((X_train.shape[0], 1))])
    stext.insert(END, '计算回归模型系数.........\n')
    stext.see(END)
    J_history, theta = gradient_descent(X_train, y_train, theta, alpha, iterations)
    print ('系数为:')
    print type(theta)
    element = ['co','pm10','grade','o3','date','so2','pm25','city_name','aqi','no2']
    stext.insert(END, '回归模型的系数为:\n'+str(theta)+'\n')
    stext.see(END)
    stext.insert(END,'多线性回归模型函数为:\n')
    stext.insert(END, 'aqi=82.74165699+1.45717517*co+15.66493131*pm10+11.07792527*o3+0.13399557*so2+29.98083111*pm25+-0.51221478*no2\n')
    X_test, mean1, std1 = feature_nor(X_test,stext)
    X_test = np.hstack([X_test, np.ones((X_test.shape[0], 1))])
    # 添加一列处理列
    # testx = np.hstack([fin_test, np.ones((fin_test.shape[0], 1))])

    # 计算进行预测
    y_test1 = X_test.dot(theta)
    y_true = y_test

    r = r2(y_test1, y_true)

    # 测试结果的输出
    # print(theta, y_test)
    # compute_Cost(X, y)

    '''
      拟合优度
    '''
    print '拟合优度为:'
    print(r)

    '''
      可视化
    '''
    stext.insert(END,'拟合优度为:\n'+str(r)+'\n')
    stext.see(END)

def getData(stext):
    th = threading.Thread(target=start1, args=(stext,))
    th.setDaemon(True)
    th.start()
