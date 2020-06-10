import matplotlib.pyplot as plt
import timeit

# plt.rcParams['savefig.dpi'] = 500
# plt.rcParams['figure.dpi'] = 500
plt.rcParams["font.family"]=["SimHei"]
plt.rcParams['axes.unicode_minus']=False

nums=[122,164.9,158,250,222,500]
luqu_nums=[100,143,123,165,112,133]
x=range(0,len(nums))
x_tiks=["2010","2011","2012","2013","2014","2015"]
plt.xticks(x,x_tiks)

star=timeit.default_timer()
rects1=plt.bar(x,nums,width=0.4,linewidth=2,label="报考人数")
rects2=plt.bar([i+0.4 for i in x],luqu_nums,width=0.4,label="录取人数",color="#2e98ea")
plt.title(1232)
plt.xlabel("年份")
plt.ylabel("人数/万人")
plt.legend()

#设置文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")

plt.savefig("条形图1")
end=timeit.default_timer()
print("time:",end-star)
plt.show()