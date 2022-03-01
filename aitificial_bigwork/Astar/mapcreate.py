import numpy as np
from  random import choice


def createmap():
    map=np.zeros((42,42))       #地图
    for x in range(0,42):       #围墙
        map[x][0]=-1
        map[x][41]=-1
    for y in range(0, 42):
        map[0][y] = -1
        map[41][y] = -1

    for j in range(1,41):        #必定连通
        map[1][j]=2
        map[20][j]=2
        map[40][j]=2
    for i in range(1,21):
        map[i][40]=2
    for i in range(20,41):
        map[i][1]=2

    for i in range(1,41):       #其余随机
        for j in range(1,41):
            if map[i][j]!=2:
                if choice([0,0,0,2])==0:
                    map[i][j]=0
                else :
                    map[i][j]=-2

    for j in range(1,41):        #必定联通
        map[1][j]=0
        map[20][j]=0
        map[40][j]=0
    for i in range(1,21):
        map[i][40]=0
    for i in range(20,41):
        map[i][1]=0
    return map


print(createmap())

