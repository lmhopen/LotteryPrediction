# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:44:16 2019

@author: Administrator
"""

import pandas as pd
import numpy as np #科学计算数据分析库,另起名为np
import matplotlib.pyplot as plt #擅长画二维图曲线,股票均线,另起名为plt
from sklearn.preprocessing import MinMaxScaler #机器学习库,数据预处理,把数据定为0,1之间
from keras.models import Sequential #深度学习库,建立模型,多网络层线性堆叠顺序模型
from keras.layers import LSTM, Dense, Activation #准备用三种神经网络层,长短期记忆网络,全连接网络层,激活层
#from keras.utils import plot_model#模型可视化做图
#from IPython.display import SVG
#from keras.utils.vis_utils import model_to_dot
import xlrd#读excel文件

plt.rcParams['font.family'] = 'SimHei' ## 设置字体

def read_to_excel():#自定义函数,读取excel表里排列三中奖号
    # 设置路径
    path = 'pl3.xls'
    # 打开execl
    workbook = xlrd.open_workbook(path)
    # 根据sheet索引或者名称获取sheet内容
    Data_sheet = workbook.sheets()[0]  # 通过索引获取
    #rowNum = Data_sheet.nrows  # sheet行数
    #colNum = Data_sheet.ncols  # sheet列数
    # 获取整行和整列的值（列表）
    #rows = Data_sheet.row_values(0)  # 获取第一行内容
    cols = Data_sheet.col_values(1)  # 获取第二列内容
    cols=cols[1:]
    # print (rows)
    #print (cols)#打印开奖号
    baiwei=[x[0] for x in cols]
    shiwei=[x[1] for x in cols]
    gewei=[x[2] for x in cols]
    return cols,baiwei,shiwei,gewei

    
def main():
    pl3,baiwei,shiwei,gewei=read_to_excel()#读excel表里的开奖号并做成开奖号,百位,十位,个位,四个数组
    #统计每个数字在个十百位出现次数
    baiweidata={}
    for i in range(10):
        i=str(i)
        print('排列3百位数字 %d 出现次数 %s ' % (int(i),baiwei.count(i)))
        baiweidata [i]= baiwei.count(i)
        i=int(i)
    print(baiweidata)
    shiweidata={}
    for i in range(10):
        i=str(i)
        print('排列3十位数字 %d 出现次数 %s ' % (int(i),shiwei.count(i)))
        shiweidata[i]=shiwei.count(i)
        i=int(i)
    print(shiweidata)
    geweidata={}
    for i in range(10):
        i=str(i)
        print('排列3个位数字 %d 出现次数 %s ' % (int(i),gewei.count(i)))
        geweidata[i]=gewei.count(i)
        i=int(i)
    print(geweidata)
    
    #转换数据类型,转换成做图函数能认识的参数
    baiweidatapd=pd.DataFrame(baiweidata,index = [0])
    shiweidatapd=pd.DataFrame(shiweidata,index = [0])
    geweidatapd=pd.DataFrame(geweidata,index = [0])
    bwcs=baiweidata.values()
    swcs=shiweidata.values()
    gwcs=geweidata.values()
    #画直方图
    plt.figure(figsize=(10,6))
    plt.bar(np.arange(10),bwcs,width=0.3)
    plt.bar(np.arange(10)+0.3,swcs,width=0.3)
    plt.bar(np.arange(10)+0.6,gwcs,width=0.3)
    
    #每个数字出现次数写直方柱上边
    for x,y in zip(np.arange(10),bwcs):
        plt.text(x,y+0.5,'%d'%y, ha='center', va= 'bottom')
    for x,y in zip(np.arange(10),swcs):
        plt.text(x+0.3,y+0.05,'%d'%y, ha='center', va= 'bottom')
    for x,y in zip(np.arange(10),gwcs):
        plt.text(x+0.6,y+0.05,'%d'%y, ha='center', va= 'bottom')
    
    #显示X横轴0到9数字
    new_ticks = np.linspace(0, 9, 10)
    plt.xticks(new_ticks)
    
    #直方图标题等文字信息
    plt.xlabel("0到9,从左到右按百十个位排")
    plt.ylabel("出现次数")
    plt.title("排列三0到9在百十个位出现次数统计表")
    plt.legend(['百位','十位','个位'])
    plt.show()
    
    #百十个位K线图
    #数据切片显示百分之1的数据,因为五千多期号做到一个屏幕上根本看不清
    qiep=int(np.array(baiwei).shape[0] *0.99)#数据切片,设定要切多少
    k=np.array(baiwei)
    k2=np.array(shiwei)
    k3=np.array(gewei)
    baiweik=k[qiep:]#要百分之一的数据
    shiweik=k2[qiep:]
    geweik=k3[qiep:]
    print(baiweik,shiweik,geweik)
    #开始做图
    fig2 = plt.figure(figsize=(14,6))
    zb=['0','1','2','3','4','5','6','7','8','9','10']#校正Y轴,就是竖轴
    plt.grid()  # 生成网格
    plt.plot(zb,'w')
    plt.plot(baiweik,'r')
    plt.plot(shiweik,'g')
    plt.plot(geweik,'b')
    plt.xlabel("最近 %d 0期"%int(np.array(baiwei).shape[0] *0.001))
    plt.ylabel("0到9数字")
    plt.title("排列三K线图")
    plt.legend([' ','百位','十位','个位'])
    plt.show()
    #画大小走势图
#这是程序真正开始执行处,如果程序被直接执行了而不是被当作库调用,则运行main()函数
if __name__ == '__main__':
    main()