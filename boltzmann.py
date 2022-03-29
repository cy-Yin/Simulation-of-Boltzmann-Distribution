import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# ====== 模拟Boltzmann分布 ====== #
num=1000
list1=[]
for i in range(10000):
    list1.append(20)
for index in range(10000000):
    i=random.randint(0,len(list1)-1)
    j=random.randint(0,len(list1)-1)
    while(i==j):
        i=random.randint(0,len(list1)-1)
        j=random.randint(0,len(list1)-1)
    if list1[i]>0:
        list1[i]-=1
        list1[j]+=1

list1.sort()

# =========   绘柱状图   ======== #
plt.rcParams['font.sans-serif']=['SimHei'] #正常显示中文
plt.rcParams['axes.unicode_minus']=False #正常显示负号
plt.title("Boltzmann分布")
index=np.arange(len(list1))
plt.bar(index,list1,width=0.5,color='r',)

plt.show()
