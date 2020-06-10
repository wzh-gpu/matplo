import matplotlib.pyplot as plt
import numpy as np
# 绘制直方图
x=np.random.randint(1,10,500)
y=np.random.randn(1000)+10


plt.rcParams["font.family"]=["SimHei"]
plt.rcParams['axes.unicode_minus']=False

# plt.hist(x,bins=20,cumulative=True,label="打的")
plt.hist(y,bins=20,label="1号")
plt.hist(y+2,bins=20,alpha=0.4,label="2号")

plt.title("直方图")
plt.xlabel("区间")
plt.ylabel("频数")

plt.legend(loc="upper left")
plt.savefig("直方图")
plt.show()
