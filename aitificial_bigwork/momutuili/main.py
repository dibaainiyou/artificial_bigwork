def Sludge(a):#污泥
    sludge=[0,0,0]#默认隶属度为0，依次对应SD,MD,LD
    if a<0 or a>100:
        return (print("输入值有误"))
    elif 0<=a<=50:
        sludge[0]=(50-a)/50
        sludge[1]=a/50
    elif 50<a<=100:
        sludge[1]=(100-a)/50
        sludge[2]=(a-50)/50
    return sludge

def Grease(a):#油脂
    grease=[0,0,0]#默认隶属度为0,依次对应NG,MG,LG
    if a<0 or a>100:
        return (print("输入值有误"))
    elif 0<=a<=50:
        grease[0]=(50-a)/50
        grease[1]=a/50
    elif 50<a<=100:
        grease[1]=(100-a)/50
        grease[2]=(a-50)/50
    return grease

def Rules(a,b):#a为污泥隶属度，b为油脂隶属度
    rules_value=[0,0,0,0,0,0,0,0,0]#依次对应9条规则结果VS,M,L,S,M,L,M,L,VL
    if a[0]!=0 and b[0]!=0:
        rules_value[0]=min(a[0],b[0])#返回规则下最小值
    if a[0]!=0 and b[1]!=0:
        rules_value[1]=min(a[0],b[1])
    if a[0]!=0 and b[2]!=0:
        rules_value[2]=min(a[0],b[2])
    if a[1]!=0 and b[0]!=0:
        rules_value[3]=min(a[1],b[0])
    if a[1]!=0 and b[1]!=0:
        rules_value[4]=min(a[1],b[1])
    if a[1]!=0 and b[2]!=0:
        rules_value[5]=min(a[1],b[2])
    if a[2]!=0 and b[0]!=0:
        rules_value[6]=min(a[2],b[0])
    if a[2]!=0 and b[1]!=0:
        rules_value[7]=min(a[2],b[1])
    if a[2]!=0 and b[2]!=0:
        rules_value[8]=min(a[2],b[2])
    return rules_value

#每条规则推理输出
def Inference(a):#a为9条规则下的结果隶属度
    time_level=[0,0,0,0,0]#默认时间隶属值为0，依次对应VS,S,M,L,VL
    time_level[0]=a[0]
    time_level[1]=a[3]
    if(a[1]!=0 or a[4]!=0 or a[6]!= 0):#去零值然后取剩下的最小值
        list_1=[a[1],a[4],a[6]]
        for i in range(len(list_1)-1,-1,-1):
            if list_1[i]==0:
                list_1.remove(0)
        time_level[2]=min(list_1)
    if(a[2]!=0 or a[5]!=0 or a[7]!= 0):
        list_2=[a[2],a[5],a[7]]
        for i in range(len(list_2)-1,-1,-1):
            if list_2[i]==0:
                list_2.remove(0)
        time_level[3]=min(list_2)
    time_level[4]=a[8]
    return time_level

def Area_gravity(a):#a为时间隶属度
    time=[0,0,0,0,0,0,0,0]#时间隶属函数八个区间分别对应的时间值
    time[0]=10-10*a[0]
    time[1]=10*a[1]
    time[2]=25-15*a[1]
    time[3]=15*a[2]+10
    time[4]=40-15*a[2]
    time[5]=15*a[3]+25
    time[6]=60-20*a[3]
    time[7]=20*a[4]+40
    sum_1=time[0]*a[0]+time[1]*a[1]+time[2]*a[1]+time[3]*a[2]+time[4]*a[2]+time[5]*a[3]+time[6]*a[3]+time[7]*a[4]
    sum_2=a[0]+2*a[1]+2*a[2]+2*a[3]+a[4]
    result=sum_1/sum_2
    return result#最后返回预测时间

def Maximum(a):#a为时间值
    if 0<=a<=10:
        u1=(10-a)/10
        u2=a/10
        if(u1>u2):
            time_level='VS'
        else:
            time_level='S'
    if 10<a<=25:
        u3=(25-a)/15
        u4=(a-10)/15
        if(u3>u4):
            time_level='S'
        else:
            time_level='M'
    if 25<a<=40:
        u5=(40-a)/15
        u6=(a-25)/15
        if(u5>u6):
            time_level='M'
        else:
            time_level='L'
    if 40<a<=60:
        u7=(60-a)/20
        u8=(a-40)/20
        if(u7>u8):
            time_level='L'
        else:
            time_level='VL'
    return time_level

if __name__ == '__main__':
    sludge =int(input("输入污泥指数:"))
    grease =int(input("输入油脂指数:"))
    rules_value=Rules(Sludge(sludge),Grease(grease))
    time_level=Inference(rules_value)#时间隶属度
    result_1=Area_gravity(time_level)#面积重心法求得的预测时间
    result_2=Maximum(result_1)#最大隶属度法求得的预测时间长短
    result_3={'VS':'很短','S':'短','M':'中等','L':'长','VL':'很长'}
    print("模糊推理系统预测洗涤时间{},预计洗涤时间{}".format(result_3[result_2],int(result_1+0.5)))






