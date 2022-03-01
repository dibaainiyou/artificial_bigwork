# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import matplotlib.pyplot as plt
from simple_convnet import SimpleConvNet
from common.trainer import Trainer

# データの読み込み
x_train=np.loadtxt(open("x_train.csv"),delimiter="," , skiprows=0)                     #读入训练和测试集
t_train=np.loadtxt(open("t_train.csv"),delimiter="," , skiprows=0)
x_test=np.loadtxt(open("x_test.csv"),delimiter="," , skiprows=0)
t_test=np.loadtxt(open("t_test.csv"),delimiter="," , skiprows=0)
print(x_train)
#对数据进行处理使其符合书上的代码
#normalize=ture
x_train=x_train.astype(np.float32)
x_test=x_test.astype(np.float32)
x_train=(255-x_train)/255.0
x_test=(255-x_test)/255.0

#one_hot_label=false
a=np.zeros(len(t_train))
b=np.zeros(len(t_test))
for x in range(0,len(t_train)):
    if t_train[x][0]==1:
        a[x]=0
    elif t_train[x][1]==1:
        a[x]=1
    else :
        a[x]=2
t_train=a

for x in range(0,len(t_test)):
    if t_test[x][0]==1:
        b[x]=0
    elif t_test[x][1]==1:
        b[x]=1
    else :
        b[x]=2
t_test=b

#flatten=false
x_train=x_train.reshape(-1, 1, 32, 32)
x_test=x_test.reshape(-1, 1, 32, 32)

#将标签转化成整型
t_train=t_train.astype(np.int32)
t_test=t_test.astype(np.int32)

print(x_train,'nihao')
print(t_train,'zaijian')
print(x_test)
print(t_test)


# 処理に時間のかかる場合はデータを削減 
#x_train, t_train = x_train[:5000], t_train[:5000]
#x_test, t_test = x_test[:1000], t_test[:1000]

max_epochs = 20

network = SimpleConvNet(input_dim=(1,32,32),
                        conv_param = {'filter_num': 30, 'filter_size': 5, 'pad': 0, 'stride': 1},
                        hidden_size=100, output_size=3, weight_init_std=0.05)
                        
trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=max_epochs, mini_batch_size=10,
                  optimizer='Adam', optimizer_param={'lr': 0.001})
trainer.train()

# パラメータの保存
network.save_params("params.pkl")
print("Saved Network Parameters!")

# グラフの描画
markers = {'train': 'o', 'test': 's'}
x = np.arange(max_epochs)
plt.plot(x, trainer.train_acc_list, marker='o', label='train', markevery=2)
plt.plot(x, trainer.test_acc_list, marker='s', label='test', markevery=2)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()















#------------------------------------------------------------------导入识别
from PIL import Image
import numpy as np

print(r"请输入图片路径(例如：F:\ruanjian\PyCharm Community Edition 2021.2.3\mycode\ANN\allphotos\A-\A-001.png)")
object=input()
photo = Image.open(object)  # 打开图片A
photo = np.array(photo)  # 将图片转化为数组
photoNp = []
photoNp2=[]
if photo.size > 1024:
    for x in range(0, 32):  # 因为是三原色，所以本来
        for y in range(0, 32):  # 数组形状为（32，32，3），
            photoNp.append(photo[x][y][0])
else:
    for x in range(0, 32):
        for y in range(0, 32):
            photoNp.append(photo[x][y])

for j in range(0, 1024):
    photoNp[j] = (255 - photoNp[j]) / 255
photoNp2.append(photoNp)
photoNp2=np.array(photoNp2)
print(photoNp2)
photoNp2=photoNp2.reshape(-1, 1, 32, 32)
daanshuzu = network.predict(photoNp2)


for daan in daanshuzu:
    if np.argmax(daan) == 0:
        print('我预测结果为A')
    elif np.argmax(daan) == 1:
        print( '我预测结果为B')
    else:
        print('我预测结果为C')