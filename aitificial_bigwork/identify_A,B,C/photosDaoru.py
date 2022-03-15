#请不要运行此程序
#此程序为导入630张图片并转化为数组存在allPhotoNp.CSV形式存在
#在提交之前已经做好

def daorutupian():
    import os                                                      #寻找系统文件的库
    from PIL import Image                                          #导入图片的库
    import numpy  as np

    photosNp=[]
    for filename in os.listdir(r"..\ANN\allphotos\A-"):              #打开图片A存在路径
        path=r"..\ANN\allphotos\A-"+"\\"+filename
        photo=Image.open(path)                                      #依次遍历图片A
        photo=np.array(photo)                                       #将图片转化为数组
        photoNp=[]
        for x in range(0,32):                                       #因为是RGB图像，所以本来
            for y in range(0,32):                                   #数组形状为（32，32，3），
                photoNp.append(photo[x][y][0])                      #将其转化为（1，32×32）的一维数组

        photosNp.append(photoNp)                                     #将一个图片数组放入总的图片数组中


    for filename in os.listdir(r"..\ANN\allphotos\B-"):              #图片B依然像图片A一样处理
        path=r"..\ANN\allphotos\B-"+"\\"+filename
        photo=Image.open(path)
        photo=np.array(photo)
        photoNp=[]
        for x in range(0,32):
            for y in range(0,32):
                photoNp.append(photo[x][y][0])
        photosNp.append(photoNp)

    for filename in os.listdir(r"..\ANN\allphotos\C-"):              #图片C依然像图片A一样处理
        path=r"..\ANN\allphotos\C-"+"\\"+filename
        photo=Image.open(path)
        photo=np.array(photo)
        photoNp=[]
        for x in range(0,32):
            for y in range(0,32):
                photoNp.append(photo[x][y][0])
        photosNp.append(photoNp)                                    #最后获得一个630个图片的图片数组集合


    np.savetxt('allPhotosNp.csv',photosNp, delimiter = ',')

if __name__=='__main__':
    daorutupian()