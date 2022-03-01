

def mapsearch(a,inx=1,iny=1,outx=40,outy=40,allx=42,ally=42):

    closelist=[]
    def f(x,y):
        return ((outx-x)**2+(outy-y)**2)**0.5
    openlist = [[inx, iny, 1,f(inx,iny),inx,iny]]

    while openlist!=[]:
        n=openlist.pop(0)

        if n[0]==outx and n[1]==outy:
            break
        x,y=n[0],n[1]
        zizhuangtai=[]                                   #生成所有子状态
        if a[x+1][y]==0:
            zizhuangtai.append([x+1,y,n[2]+1,f(x+1,y),x,y])
        if a[x][y+1]==0:
            zizhuangtai.append([x,y+1,n[2]+1,f(x,y+1),x,y])
        if a[x-1][y]==0:
            zizhuangtai.append([x-1,y,n[2]+1,f(x-1,y),x,y])
        if a[x][y-1]==0:
            zizhuangtai.append([x,y-1,n[2]+1,f(x,y-1),x,y])

        if zizhuangtai==[]:
            continue


        for everyzzt in zizhuangtai:   #???子状态和原有相同的路程不同
            case3 = 1
            for everyopen in openlist:
                if everyzzt[0:2] ==everyopen[0:2]:
                    case3 = 0
                    if everyzzt[3] < everyopen[3]:
                        openlist.append(everyzzt)
            for everyclose in closelist:
                if everyzzt[0:2] == everyclose[0:2]:
                    case3 = 0
                    if everyzzt[3]<everyclose[3]:
                        closelist.remove(everyclose)
                        openlist.append(everyzzt)
                        case3=0

            if case3==1:
                openlist.append(everyzzt)
        closelist.append(n)
        openlist.sort(key=lambda x : x[3])
    closelist.append(n)
    maplist=[closelist[-1]]
    while (maplist[0][4] !=inx) or (maplist[0][5] !=iny) :
        for i in closelist:
            if maplist[0][4]==i[0] and maplist[0][5]==i[1]:
                maplist.insert(0,i)
    maplist.insert(0,closelist[0])

    for i in maplist:
        a[i[0]][i[1]]=i[2]
    print(maplist)
    return a

#不可连通情况
Map=np.zeros((42,42))
for x in range(0, 42):  # 围墙
    Map[x][0] = -1
    Map[x][41] = -1
for y in range(0, 42):
    Map[0][y] = -1
    Map[41][y] = -1

for x in range(0, 42):  # 围墙
    Map[x][20] = -2
for y in range(0, 42):
    Map[20][y] = -2