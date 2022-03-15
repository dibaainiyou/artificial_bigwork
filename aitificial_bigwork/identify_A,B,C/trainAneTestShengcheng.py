#请不要运行此程序
#此本部分为随机生成训练和测试集并保存到
#x_train.csv,t_train.csv,x_test.csv,t_test.csv，在之前已完成

def tAndT():
    import numpy as np
    photosNp = np.loadtxt(open("allPhotosNp.csv"),delimiter="," , skiprows=0)          #导入之前的所有图片数据集
    x_train,t_train=[],[]                                                              #训练测试数据以及其标签列表
    x_test,t_test=[],[]
    train_haoma=np.random.choice(range(0,630),size=500,replace=False)                  #随机选取500作为训练集
    for i in train_haoma:                                                              #对应生成训练标签
        x_train.append(photosNp[i])
        if i<210:
            t_train.append([1,0,0])
        elif i<420 :
            t_train.append([0,1,0])
        else:
            t_train.append([0,0,1])

    for i in range(0,630):                                                              #其余130个作为测试集
        if i not in train_haoma:                                                        #并生成测试标签
            x_test.append(photosNp[i])
            if i < 210:
                t_test.append([1, 0, 0])
            elif i < 420:
                t_test.append([0, 1, 0])
            else:
                t_test.append([0, 0, 1])

    np.savetxt('x_train.csv',x_train, delimiter = ',')
    np.savetxt('t_train.csv',t_train, delimiter = ',')
    np.savetxt('x_test.csv',x_test, delimiter = ',')
    np.savetxt('t_test.csv',t_test, delimiter = ',')

if __name__ == '__main__':
    tAndT()