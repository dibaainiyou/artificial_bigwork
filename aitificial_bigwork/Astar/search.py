

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


        for everyzzt in zizhuangtai:   #子状态和列表里相同状态的路程不同
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


    for i in closelist:
        a[i[0]][i[1]]=i[2]

    print(a)
    return a


