#此程序是main不能运行的替补程序，但同样需要图像导入库PIL
#无可视化功能
#需要在运行窗口输入图片路径


from PIL import Image
import twoLayerNet
import numpy as np

print(r"请输入图片路径(例如：F:\ruanjian\PyCharm Community Edition 2021.2.3\mycode\ANN\allphotos\A-\A-001.png)")
object=input()
photo = Image.open(object)  # 打开图片A
photo = np.array(photo)  # 将图片转化为数组
photoNp = []
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

network = twoLayerNet.TwoLayerNet(input_size=1024, hidden_size=50, output_size=3)
network.params['W1'] = np.loadtxt(open("paramsW1.csv"), delimiter=",", skiprows=0)
network.params['b1'] = np.loadtxt(open("paramsb1.csv"), delimiter=",", skiprows=0)
network.params['W2'] = np.loadtxt(open("paramsW2.csv"), delimiter=",", skiprows=0)
network.params['b2'] = np.loadtxt(open("paramsb2.csv"), delimiter=",", skiprows=0)
daanshuzu = network.predict(photoNp)
if np.argmax(daanshuzu) == 0:
    print('预测得分:\n'+'A:'+str(daanshuzu[0])+'\nB:'+str(daanshuzu[1])+'\nC:'+str(daanshuzu[2]))
    print('因此我预测结果为A')
elif np.argmax(daanshuzu) == 1:
    print('预测得分:\n' + 'A:' + str(daanshuzu[0]) + '\nB:' + str(daanshuzu[1]) + '\nC:' + str(daanshuzu[2]) )
    print( '我预测结果为B')
else:
    print('预测得分:\n' + 'A:' + str(daanshuzu[0]) + '\nB:' + str(daanshuzu[1]) + '\nC:' + str(daanshuzu[2]) )
    print('我预测结果为C')