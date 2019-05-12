# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:00:31 2019
@author: Administrator
"""
import requests #爬虫库
import xlwt #写excel表库
import time #时间获取转换
from bs4 import BeautifulSoup #爬虫库

# 获取网页内容
def get_html(url):
    #这是一个UA伪装,告诉网站你浏览器和操作系统系统
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url, headers = headers)#用爬虫对象获取网页内容
    if response.status_code == 200:#对象状态码等于200说明获取网页内容成功
        print('读取网页成功!')
        return response.text#返回获取的网页内容
    else:
        print('读网页失败,无数据！')
    return None

# 解析网页内容
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')#创建网页解析器对象
    i = 0
    #查找网页里的tr标签,从第4个tr读到倒数第2个tr,因为通过对网页分析,前三个和最后一个tr没用
    for item in soup.select('tr')[3:-1]:#把查到的tr组成一个列表,item是列表指针,for每循环一次,item就选下一个tr,读完列表本循环结束,函数就结束,
        try:   #不加try和except有的值是&nbsp,是网页里的空白键,会出错,加上调试命令忽略错误,后边统一处理             
            yield{ #yield作用是得到数据立即返回给调用函数,但不退出本循环本函数
                    'issue':item.select('td')[i].text,#item查到的第0个td是开奖期号,写到time列
                    'WinningNumbers':item.select('td')[i+1].text,#0+1个td是中奖号码
                    'sum':item.select('td')[i+2].text,#总和数
                    'Totalsales':item.select('td')[i+3].text,#总销售额
                    'Direct':item.select('td')[i+4].text,#直选中奖注数
                    'Direct_bonus':item.select('td')[i+5].text,#直选总奖金
                    'three_selection':item.select('td')[i+6].text,#组选3中奖注数
                    'three_selection_bonus':item.select('td')[i+7].text,#组选3总奖金
                    'six__selection':item.select('td')[i+8].text,#组选6中奖数
                    'six__selection_bonus':item.select('td')[i+9].text,#组选6总奖金
                    'time':item.select('td')[i+10].text#开奖日期
                    #一组数据读完马上把值返回给调用函数,但没有退出本函数和本循环,
                    #调用函数得到数据,写到excel对象里,然后又回到这里,本次循环结束,开始下一次循环,item列表指针
                    }
        except IndexError:
            pass
              


# 将数据写入excel表
def write_to_excel():
    f = xlwt.Workbook() #创建excel表对象
    sheet1 = f.add_sheet('pl3', cell_overwrite_ok=True)#创建表,名叫3D
    row0 = ['期号','中奖号码','总和','总销售额(元)','直选注数','直选奖金','组选3注数','组选3奖金','组选6注数','组选6奖金','开奖日期']#把所有列名做成一个list表
    # 写入第一行
    for j in range(0, len(row0)):#用循环把每一列的名称按顺序写上去
        sheet1.write(0, j, row0[j])#写第0行,第几列的内容

    # 爬取网页,将结果写入excel对象
    i = 0
    #用fiddler网页抓包得到真实网页地址,一次获取全部历史数据
    url = 'http://datachart.500.com/pls/history/inc/history.php?limit=15116&start=04001&end=19117'
    html = get_html(url)#调用自定义函数,读网页获取网页内容
    print('正在提取保存数据......')
    if html != None:        #如果读网页没出错,读成功,则进行下一步,
        # 写入每一期信息
        '''
        调用自定义函数分析提取网页数据,保存到excel对象表中,item是循环中所调用的parse_html函数里的对象,是一个字典类型数据
        就是提取其它函数的item对象数据,写到excel表对象里
        '''
        for item in parse_html(html):
            #下边的if是为了去掉列表里的乱码&nbsp,在网页里显示为空白,用0代替
            if item['three_selection']=='&nbsp':
                item['three_selection']='0'
                item['three_selection_bonus']='0'
            else:
                item['six__selection']='0'
                item['six__selection_bonus']='0'
            
            item['WinningNumbers']=item['WinningNumbers'].replace(" ", "")#去掉中奖号里的空格
            

            
            sheet1.write(i+1, 0, item['issue'])#写到excel表里第i+1行,第0列,写item的time键数据
            sheet1.write(i+1, 1, item['WinningNumbers'])
            sheet1.write(i+1, 2, item['sum'])
            sheet1.write(i+1, 3, item['Totalsales'])
            sheet1.write(i+1, 4, item['Direct'])
            sheet1.write(i+1, 5, item['Direct_bonus'])
            sheet1.write(i+1, 6, item['three_selection'])
            sheet1.write(i+1, 7, item['three_selection_bonus'])
            sheet1.write(i+1, 8, item['six__selection'])
            sheet1.write(i+1, 9, item['six__selection_bonus'])
            sheet1.write(i+1, 10, item['time'])
            i += 1#写完一轮换行准备下次循环写下一行
                
    try:
        f.save('pl3.xls')
        print('写入EXCEL表pl3.xls成功!')
    except:
        print('写入EXCEL表失败')
        
#主函数就是调用其它函数,作用是将数据写入excel表
def main():
    write_to_excel()#自定义函数,将数据写入excel表

#这是程序真正开始执行处,如果程序被直接执行了而不是被当作库调用,则运行main()函数
if __name__ == '__main__':
    main()
