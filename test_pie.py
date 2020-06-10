import matplotlib.pyplot as plt


x=[2,3,4,5,6]
labels=["aa","bb","cc","dd","dd"]

plt.rcParams["font.family"]=["SimHei"]
plt.rcParams['axes.unicode_minus']=False
plt.pie(x,explode=[0,0,0,0,0.1],labels=labels,labeldistance=1.2,autopct="%.2f%%",
        colors=["b","r","y","g","#FF2159"])
plt.title("饼状图")
plt.savefig("饼状图")
plt.show()