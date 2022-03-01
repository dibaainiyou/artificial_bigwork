# -*- coding:utf-8 -*-
# Python实现正态分布
# 绘制正态分布概率密度函数
#cmd /k cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


import collections
def flatten(x):
    result = []
    for el in x:
        if isinstance(x, collections.Iterable) and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

#标准差
Standard_Deviation = 0.001


#求图像压缩值
#一等
u0 = 0  # 均值μ
sig0 = math.sqrt(Standard_Deviation)  # 标准差δ
x0 = np.linspace(0, 1, 50)
y0_sig = (np.exp(-(x0 - u0) ** 2 / (2 * sig0 ** 2)) / (math.sqrt(2 * math.pi) * sig0))

x0 = 0
y00 = (np.exp(-(x0 - u0) ** 2 / (2 * sig0 ** 2)) / (math.sqrt(2 * math.pi) * sig0))
#print(y00)#输出压缩值

correct = y00

#一等
u1 = 0  # 均值μ
sig1 = math.sqrt(Standard_Deviation)  # 标准差δ
x1 = np.linspace(0, 0.39, 50)
y1_sig = (np.exp(-(x1 - u1) ** 2 / (2 * sig1 ** 2)) / (math.sqrt(2 * math.pi) * sig1))/correct

#二等
u2 = 0.33  # 均值μ
sig2 = math.sqrt(Standard_Deviation)  # 标准差δ
x2 = np.linspace(0, 0.59, 50)
y2_sig = (np.exp(-(x2 - u2) ** 2 / (2 * sig2 ** 2)) / (math.sqrt(2 * math.pi) * sig2))/correct

#三等
u3 = 0.67  # 均值μ
sig3 = math.sqrt(Standard_Deviation)  # 标准差δ
x3 = np.linspace(0.4, 1, 50)
y3_sig = (np.exp(-(x3 - u3) ** 2 / (2 * sig3 ** 2)) / (math.sqrt(2 * math.pi) * sig3))/correct

#四等
u4 = 1  # 均值μ
sig4 = math.sqrt(Standard_Deviation)  # 标准差δ
x4 = np.linspace(0.61, 1, 50)
y4_sig = (np.exp(-(x4 - u4) ** 2 / (2 * sig4 ** 2)) / (math.sqrt(2 * math.pi) * sig4))/correct

#画AB的隶属度图像
plt.plot(x1, y1_sig, "rED", linewidth=2)
plt.plot(x2, y2_sig, "black", linewidth=2)
plt.plot(x3, y3_sig, "blue", linewidth=2)
plt.plot(x4, y4_sig, "yellow", linewidth=2)
plt.grid(True)
plt.show()

#求隶属度的四个关键值
x1 = x2 = x3 = x4 = 0
M = (np.exp(-(x1 - u1) ** 2 / (2 * sig1 ** 2)) / (math.sqrt(2 * math.pi) * sig1))/correct
N = (np.exp(-(x2 - u2) ** 2 / (2 * sig2 ** 2)) / (math.sqrt(2 * math.pi) * sig2))/correct
P = (np.exp(-(x3 - u3) ** 2 / (2 * sig3 ** 2)) / (math.sqrt(2 * math.pi) * sig3))/correct
Q = (np.exp(-(x4 - u4) ** 2 / (2 * sig4 ** 2)) / (math.sqrt(2 * math.pi) * sig4))/correct

#取值化简
M = round(M,3)
N = round(N,3)
P = round(P,3)
Q = round(Q,3)

print(M)
print(N)
print(P)
print(Q)

#将取到的值填入矩阵
A1 = np.array([[M,N,P,Q]])
A2 = np.array([[N,M,N,P]])
A3 = np.array([[P,N,M,N]])
A4 = np.array([[Q,P,N,M]])

B1 = np.array([[M,N,P,Q]])
B2 = np.array([[N,M,N,P]])
B3 = np.array([[P,N,M,N]])
B4 = np.array([[Q,P,N,M]])

'''
B4 = np.array([[M,N,P,Q]])
B3 = np.array([[N,M,N,P]])
B2 = np.array([[P,N,M,N]])
B1 = np.array([[Q,P,N,M]])
'''


C1 = np.array([[M,N,P,Q,Q,Q,Q]])
C2 = np.array([[N,M,N,P,Q,Q,Q]])
C3 = np.array([[P,N,M,N,P,Q,Q]])
C4 = np.array([[Q,P,N,M,N,P,Q]])
C5 = np.array([[Q,Q,P,N,M,N,P]])
C6 = np.array([[Q,Q,Q,P,N,M,N]])
C7 = np.array([[Q,Q,Q,Q,P,N,M]])

def hecheng(c,d):
	"""
	求模糊是矩阵a和模糊矩阵b的合成
	"""
	a,b = np.array(c),np.array(d)
	if a.shape[1] == b.shape[0]:
		c=np.zeros_like(a.dot(b))
		for i in range(a.shape[0]): # 遍历a的行元素
			for j in range(b.shape[1]): # 遍历b的列元素
				empty=[]
				for k in range(a.shape[1]):
					empty.append(min(a[i,k],b[k,j])) # 行列元素比小
				c[i,j]=max(empty) # 比小结果取大
		return c
	else:
		print("输入矩阵不能做合成运算！\n请检查矩阵的维度！")


#F1-16为Ai AND Bi
F1 = hecheng(A1.T,B1)
F2 = hecheng(A1.T,B2)
F3 = hecheng(A1.T,B3)
F4 = hecheng(A1.T,B4)
F5 = hecheng(A2.T,B1)
F6 = hecheng(A2.T,B2)
F7 = hecheng(A2.T,B3)
F8 = hecheng(A2.T,B4)
F9 = hecheng(A3.T,B1)
F10 = hecheng(A3.T,B2)
F11 = hecheng(A3.T,B3)
F12 = hecheng(A3.T,B4)
F13 = hecheng(A4.T,B1)
F14 = hecheng(A4.T,B2)
F15 = hecheng(A4.T,B3)
F16 = hecheng(A4.T,B4)

#展平F为G，即R-Ai×Bi
G1 = F1.flatten()
G2 = F2.flatten()
G3 = F3.flatten()
G4 = F4.flatten()
G5 = F5.flatten()
G6 = F6.flatten()
G7 = F7.flatten()
G8 = F8.flatten()
G9 = F9.flatten()
G10 = F10.flatten()
G11 = F11.flatten()
G12 = F12.flatten()
G13 = F13.flatten()
G14 = F14.flatten()
G15 = F15.flatten()
G16 = F16.flatten()

'''
print(G1)
print(G2)
print(G3)
print(G4)
print(G5)
print(G6)
print(G7)
print(G8)
print(G9)
print(G10)
print(G11)
print(G12)
print(G13)
print(G14)
print(G15)
print(G16)
'''

R1 = hecheng((np.mat(G1)).T,C1)
R2 = hecheng((np.mat(G2)).T,C2)
R3 = hecheng((np.mat(G3)).T,C3)
R4 = hecheng((np.mat(G4)).T,C4)
R5 = hecheng((np.mat(G5)).T,C2)
R6 = hecheng((np.mat(G6)).T,C3)
R7 = hecheng((np.mat(G7)).T,C4)
R8 = hecheng((np.mat(G8)).T,C5)
R9 = hecheng((np.mat(G9)).T,C3)
R10 = hecheng((np.mat(G10)).T,C4)
R11 = hecheng((np.mat(G11)).T,C5)
R12 = hecheng((np.mat(G12)).T,C6)
R13 = hecheng((np.mat(G13)).T,C4)
R14 = hecheng((np.mat(G14)).T,C5)
R15 = hecheng((np.mat(G15)).T,C6)
R16 = hecheng((np.mat(G16)).T,C7)





#求总模糊关系R
S1 = np.maximum(R1,R2)
S2 = np.maximum(S1,R3)
S3 = np.maximum(S2,R4)
S4 = np.maximum(S3,R5)
S5 = np.maximum(S4,R6)
S6 = np.maximum(S5,R7)
S7 = np.maximum(S6,R8)
S8 = np.maximum(S7,R9)
S9 = np.maximum(S8,R10)
S10 = np.maximum(S9,R11)
S11 = np.maximum(S10,R12)
S12 = np.maximum(S11,R13)
S13 = np.maximum(S12,R14)
S14 = np.maximum(S13,R15)
S15 = np.maximum(S14,R16)




#模糊计算函数
def function_fuzzy(ax,bx):
    
    ax1 = (np.exp(-(ax - u1) ** 2 / (2 * sig1 ** 2)) / (math.sqrt(2 * math.pi) * sig1))/correct
    ax2 = (np.exp(-(ax - u2) ** 2 / (2 * sig2 ** 2)) / (math.sqrt(2 * math.pi) * sig2))/correct
    ax3 = (np.exp(-(ax - u3) ** 2 / (2 * sig3 ** 2)) / (math.sqrt(2 * math.pi) * sig3))/correct
    ax4 = (np.exp(-(ax - u4) ** 2 / (2 * sig4 ** 2)) / (math.sqrt(2 * math.pi) * sig4))/correct

    bx1 = (np.exp(-(bx - u1) ** 2 / (2 * sig1 ** 2)) / (math.sqrt(2 * math.pi) * sig1))/correct
    bx2 = (np.exp(-(bx - u2) ** 2 / (2 * sig2 ** 2)) / (math.sqrt(2 * math.pi) * sig2))/correct
    bx3 = (np.exp(-(bx - u3) ** 2 / (2 * sig3 ** 2)) / (math.sqrt(2 * math.pi) * sig3))/correct
    bx4 = (np.exp(-(bx - u4) ** 2 / (2 * sig4 ** 2)) / (math.sqrt(2 * math.pi) * sig4))/correct

    Ax = np.array([[ax1,ax2,ax3,ax4]])
    Bx = np.array([[bx1,bx2,bx3,bx4]])

    Ax_AND_Bx = hecheng(Ax.T,Bx)
    
    RAx_AND_Bx = Ax_AND_Bx.flatten()

    C = hecheng((np.mat(RAx_AND_Bx)),S15)
    CC = C.flatten()


#加权平均判决法
    U = (CC[0]*1+CC[1]*2+CC[2]*3+CC[3]*4+CC[4]*5+CC[5]*6+CC[6]*7)/(CC[0]+CC[1]+CC[2]+CC[3]+CC[4]+CC[5]+CC[6])
    V = round(U,3)
    return(V)
    
##开始绘制图像
#定义图像精度与范围
accuracy = 100
mAx = 1
mIn = 0
delta = mAx-mIn

Z = []
for x in np.arange(mIn,mAx,delta/accuracy):
    for y in np.arange(mIn,mAx,delta/accuracy):
        z = function_fuzzy(x,y)
        Z.append(z)

#定义三维数据
x = np.arange(mIn,mAx,delta/accuracy)
y = np.arange(mIn,mAx,delta/accuracy)
X,Y = np.meshgrid(x,y)
ZZ = np.mat(Z)

ZZ.resize((accuracy, accuracy))



fig = plt.figure()  #定义新的三维坐标轴
ax3 = plt.axes(projection='3d')



#作图
ax3.plot_surface(X,Y,ZZ,cmap='rainbow')

plt.show()