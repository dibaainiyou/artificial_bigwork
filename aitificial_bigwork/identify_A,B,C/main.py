#请运行此程序，此程序是可视化界面，需要可视化库tkinter,图片导入库PIL的支持
#若老师未安装或其它原因不能运行界面，
#请运行main2.py程序





# tkinter实现菜单功能
from tkinter import *
from tkinter import filedialog
from PIL import Image
import twoLayerNet
import numpy as np

#可视化窗口，继承tkinter的Frame
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("识别系统")

        self.pack(fill=BOTH, expand=1)

        # 实例化一个Menu对象，这个在主窗体添加一个菜单
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # 创建File菜单，下面有Save和Exit两个子菜单
        file = Menu(menu)
        file.add_command(label='导入并识别',command=self.daorushibie)
        menu.add_cascade(label='导入并识别', menu=file)



    def daorushibie(self):                                                            #导入识别功能
        object=filedialog.askopenfilename()
        objectphoto=Image.open(object)
        objectphoto =PhotoImage(file=object)
        imgobject = Label(self, image=objectphoto)
        imgobject.image = objectphoto
        imgobject.place(x=0, y=100)
        photo = Image.open(object)                                      # 打开图片A
        photo = np.array(photo)                                        # 将图片转化为数组
        photoNp=[]
        if photo.size>1024:
            for x in range(0, 32):                                  # 因为是三原色，所以本来
                for y in range(0, 32):                              # 数组形状为（32，32，3），
                    photoNp.append(photo[x][y][0])
        else:                                                        #对于灰度图像的处理
            for x in range(0, 32):
                for y in range(0, 32):
                    photoNp.append(photo[x][y])
        for j in range(0, 1024):
            photoNp[j] = (255 - photoNp[j]) / 255

        network = twoLayerNet.TwoLayerNet(input_size=1024, hidden_size=50, output_size=3)
        network.params['W1']=np.loadtxt(open("paramsW1.csv"),delimiter="," , skiprows=0)
        network.params['b1'] = np.loadtxt(open("paramsb1.csv"), delimiter=",", skiprows=0)
        network.params['W2'] = np.loadtxt(open("paramsW2.csv"), delimiter=",", skiprows=0)
        network.params['b2'] = np.loadtxt(open("paramsb2.csv"), delimiter=",", skiprows=0)
        daanshuzu=network.predict(photoNp)
        if np.argmax(daanshuzu)==0:
            jieguo='因此我预测结果为A'
        elif np.argmax(daanshuzu)==1:
            jieguo='因此我预测结果为B'
        else:
            jieguo = '因此我预测结果为C'

        text = Label(self, fg='red',text='预测得分:\n'+'A:'+str(daanshuzu[0])+'\nB:'+str(daanshuzu[1])+'\nC:'+str(daanshuzu[2])+'\n\n'+jieguo)
        text.place(x=50, y=0)


        return 0







root = Tk()
root.geometry("500x400")
app = Window(root)
root.mainloop()
