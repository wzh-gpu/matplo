import numpy as np
import re
import matplotlib.pyplot as plt
'''
豆瓣电影top250
日期：2020/4/28
'''
t1=np.loadtxt("text25.txt",dtype=str,encoding="utf-8",delimiter=", ",usecols=2,unpack=True)
t2=np.loadtxt("text25.txt",dtype=str,encoding="utf-8",delimiter=", ",usecols=3,unpack=True)
t3=np.loadtxt("text25.txt",dtype=str,encoding="utf-8",delimiter=", ",usecols=4,unpack=True)
numb=re.findall(': "(.*?)"',str(t1))#评分
years=re.findall(': "(.*?)"',str(t2))#年份
Country=re.findall(': "(.*?)"',str(t3))#国家

'''
设置图片大小以及字体
'''
# plt.rcParams['savefig.dpi'] = 120
# plt.rcParams['figure.dpi'] = 120
plt.rcParams["font.family"]=["SimHei"]
plt.rcParams['axes.unicode_minus']=False
# plt.figure(figsize=(12,9))
c1=[]
c2=[]
y=0
for i in set(years):#统计每年多少个
    if int(i) >=2000:
        c1.append(i)
        y+=years.count(i)
c1.sort()
for i in c1:
    c2.append(years.count(i))

"""
扇形统计图
"""
plt.pie(c2,labels=c1,labeldistance=1.05,autopct="%.2f%%",pctdistance=0.8)

plt.title("豆瓣评分榜Top250中2000年后出品的电影")#图片标题

plt.legend(["总数：%d" %y],loc="upper left",frameon=False,fontsize=10)

plt.savefig("豆瓣评分榜Top250中2000年后出品的电影")#保存图片
plt.show()#显示图片
'''
条形统计图
'''
k=range(0,len(c1))
plt.xticks(k,c1,rotation=45,fontsize=14)
shuzhis=plt.bar(k,c2,label="当年出品的电影进入Top250的数量",width=0.7,color=['r','b','y','g','#00C5CD','#FFDAB9','#708090','#000000'])
plt.title("豆瓣评分榜Top250中2000年后出品的电影")#图片标题
plt.xlabel("年份",fontsize=14)
plt.ylabel("数量")
# 设置文字
for shuzhi in shuzhis:
    height = shuzhi.get_height()
    plt.text(shuzhi.get_x() + shuzhi.get_width()/2, height+0.25, str(height),fontsize=14, ha="center", va="bottom")
    plt.text(shuzhi.get_x() + shuzhi.get_width()/2, height, "("+str((height / y)*100)[:4]+"%)",fontsize=12, ha="center", va="bottom")
plt.legend(["总数：%d" %y],loc="upper left",frameon=False,fontsize=16)
plt.savefig("豆瓣评分榜Top250中2000年后出品的电影(条形)")#保存图片
plt.show()#显示图片
'''
折线统计图
'''
# k=range(0,len(c1))
# plt.xticks(k,c1,rotation=45)
# plt.plot(c1,c2,"bo--")
# plt.show()
