import matplotlib.pyplot as plt
import numpy as np
import re

t2=np.loadtxt("text25.txt",dtype=str,encoding="utf-8",delimiter=", ",usecols=3,unpack=True)
years=re.findall(': "(.*?)"',str(t2))#年份

plt.rcParams['savefig.dpi'] = 500
plt.rcParams['figure.dpi'] = 500
plt.rcParams["font.family"]=["SimHei"]
plt.rcParams['axes.unicode_minus']=False

c1=[]
c2=[]
j=2000
for i in set(years):#统计每年多少个
    if int(i) >=2000:
        c1.append(int(i))
        # c2.append(years.count(i))
        # print(i,years.count(i))
c1.sort()
print(c1)
k=0
for i in range(c1):
    if c1[k]==int(i):
        c2.append(years.count(i))
        print(i, years.count(i))
        k+=1
# x=np.array(c1)
# y=np.array(c2)
# print(x,y)
# plt.xticks(x,y)
# # plt.xticks(y,x,rotation=45)
# plt.plot(x,y,"bo--")
#
# plt.show()