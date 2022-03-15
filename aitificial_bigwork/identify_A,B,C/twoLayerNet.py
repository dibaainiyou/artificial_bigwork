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


    def network_train(self):
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



        network = TwoLayerNet(input_size=1024, hidden_size=50, output_size=3)              #实例化神经网络
        iters_num =500
        train_size = x_train.shape[0]
        batch_size =10
        learning_rate = 0.1

        train_loss_list = []
        train_acc_list = []
        test_acc_list = []

        iter_per_epoch = max(train_size / batch_size, 1)
        for i in range(iters_num):                                                          #训练500次
            batch_mask = np.random.choice(train_size, batch_size)                           #随机选取minibatch
            x_batch = x_train[batch_mask]
            t_batch = t_train[batch_mask]


            #grad = network.numerical_gradient(x_batch, t_batch)
            grad = network.gradient(x_batch, t_batch)                                       #求取梯度

            for key in ('W1', 'b1', 'W2', 'b2'):                                             #更新权重和偏置
                network.params[key] -= learning_rate * grad[key]


        np.savetxt('paramsW1.csv',network.params['W1'], delimiter = ',')
        np.savetxt('paramsb1.csv',network.params['b1'], delimiter = ',')
        np.savetxt('paramsW2.csv',network.params['W2'], delimiter = ',')
        np.savetxt('paramsb2.csv',network.params['b2'], delimiter = ',')




if __name__=='__main__':
    network = TwoLayerNet(input_size=1024, hidden_size=50, output_size=3)
    network.network_train()
