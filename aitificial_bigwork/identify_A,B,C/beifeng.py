#本程序为构建神经网络并完成训练

import numpy as np
import matplotlib.pyplot as plt

#sigmoid,softmax、交叉熵函数和梯度函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)

def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

def cross_entropy_error(y,t):

    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]

    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size                 #y[np.arange(batch_size), t]为y第np.arange(batch_size)第t列数的数组


def numerical_gradient(f,x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val
        it.iternext()
    return grad


#两层神经网络
class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

#预测函数，用来预测输入数据属于A、B还是C
    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

#损失函数，用来算预测结果与标签交叉熵函数
    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y, t)

#准确函数，用来算该神经网络对训练集或者测试集的准确度
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

#数值梯度函数，用来调整权重值
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads

    def gradient(self, x, t):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
        grads = {}

        batch_num = x.shape[0]

        # forward
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        # backward
        dy = (y - t) / batch_num
        grads['W2'] = np.dot(z1.T, dy)
        grads['b2'] = np.sum(dy, axis=0)

        dz1 = np.dot(dy, W2.T)
        da1 = sigmoid_grad(a1) * dz1
        grads['W1'] = np.dot(x.T, da1)
        grads['b1'] = np.sum(da1, axis=0)

        return grads







x_train=np.loadtxt(open("x_train.csv"),delimiter="," , skiprows=0)                     #读入训练和测试集
t_train=np.loadtxt(open("t_train.csv"),delimiter="," , skiprows=0)
x_test=np.loadtxt(open("x_test.csv"),delimiter="," , skiprows=0)
t_test=np.loadtxt(open("t_test.csv"),delimiter="," , skiprows=0)
for i in range(0,500):
    for j in range(0,1024):
        x_train[i][j]=(255-x_train[i][j])/255


for i in range(0,130):
    for j in range(0,1024):
        x_test[i][j]=(255-x_test[i][j])/255



network = TwoLayerNet(input_size=1024, hidden_size=50, output_size=3)
iters_num =500
train_size = x_train.shape[0]
batch_size =10
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)
for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]


    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)

    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))


markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()












import os  # 寻找系统文件的库
from PIL import Image  # 导入图片的库
import numpy as np




photosNp=[]
for filename in os.listdir(r"..\ANN\ceshi"):  # 打开图片A存在路径
    path = r"..\ANN\ceshi" + "\\" + filename
    photo = Image.open(path)  # 依次遍历图片A
    photo = np.array(photo)  # 将图片转化为数组
    photoNp = []
    for x in range(0, 32):  # 因为是三原色，所以本来
        for y in range(0, 32):  # 数组形状为（32，32，3），
            photoNp.append(photo[x][y][0])  # 将其转化为（1，32×32）的一维数组
    photosNp.append(photoNp)

for i in range(0,100):
    for j in range(0,1024):
        photosNp[i][j]=(255-photosNp[i][j])/255
print(network.params['b1'])

daan=network.predict(photosNp)







