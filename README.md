# LotteryPrediction
Network Crawler Grabs Lottery Data and Analyses and Predictions 网络爬虫抓取彩票数据并且分析预测


pl3.py是爬虫程序

pl3tj.py是统计分析图形化



首先找一家比较大型的网站,500彩票网,因为是美国上市公司,轻易不会黄,这样写的代码用的时间能长些.

http://datachart.500.com/pls/

分析一下这个网页的内容,可以输入开奖期号一次查看排列3全部历史数据,但是网页代码我看不太懂,于是我开了一个http抓包程序Fiddler.

得到真实url

http://datachart.500.com/pls/history/inc/history.php?limit=15116&start=04001&end=19117

上边连接中04001是排列3上市第一期的期号,19117是我写这个程序时当天的开奖期号.

然后开始写Python代码,需要注意的是,有时候访问这个网页会失败,这是因为一次要求获取的数据太多了,打不开就重试,一定能成.

保存到本地的文件名是pl3.xls,数据全抓出来了,下一步如何分析预测就看网友们的集体智慧了

人工智能分析彩票算不出来,那只能人为的统计统计彩票数据了,可以统计彩票还能练练手.
之前写过一篇文章,用python爬虫程序网上抓取排列3全部历史数据,保存到本地,现在这篇是读取本地文件,开始展开分析.
反正程序写完之后,我感觉python最乱的是各种数据的互相转换,python的数据类型非常多,然后光看代码也不知道是什么数据类型,你调用不同的库函数,参数得是函数指定数据类型,所以数据类型得转换来转换去,转的我头晕眼花,说到底还是基础功力薄弱,光想着调用各种库模块,却不知道基本功不好的话库模块都调用不动.
试了多种python的IDE感觉还是spyder最好,主要它在调试运行程序时,显示各种数据的类型,写的非常详细全面.否则程序写长了光各种数据类型的转换就能把人搞的头晕眼花,怪不得连python之父都不想用python了.
