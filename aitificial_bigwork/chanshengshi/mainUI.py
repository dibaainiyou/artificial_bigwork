import tkinter as tk
import recognize
from aitificial_bigwork.chanshengshi import animal_add
import attribute_add
import delete
import datebaseshow
from PIL import Image, ImageTk

window=tk.Tk()
window.title('产生式系统')
window.geometry('1200x950')

#库内内容
def show():
    contentdatebase1Label=tk.Label(window,text="动物库",font=20,height=4)
    contentdatebase1Label.grid(row=10,column=1)
    contentdatebase1Label=tk.Label(window,text="动物特性",width=21,bg='yellow')
    contentdatebase1Label.grid(row=11,column=0)
    contentdatebase1Label=tk.Label(window,text="动物名称",width=21,bg='yellow')
    contentdatebase1Label.grid(row=11,column=2)
    datebase11=tk.StringVar()
    datebase11.set(datebaseshow.animalsdatebaseshow1())
    datebase12=tk.StringVar()
    datebase12.set(datebaseshow.animalsdatebaseshow2())
    contentdatebase11=tk.Label(window,textvariable=datebase11)
    contentdatebase11.grid(row=12,column=2)
    contentdatebase12=tk.Label(window,textvariable=datebase12)
    contentdatebase12.grid(row=12,column=0)

    contentdatebase2Label=tk.Label(window,text="属性库",font=20,height=4)
    contentdatebase2Label.grid(row=13,column=1)
    contentdatebase2Label=tk.Label(window,text="动物属性",width=21,bg='yellow')
    contentdatebase2Label.grid(row=14,column=0)
    contentdatebase2Label=tk.Label(window,text="动物特性",width=21,bg='yellow')
    contentdatebase2Label.grid(row=14,column=2)
    datebase21=tk.StringVar()
    datebase21.set(datebaseshow.attributedatebaseshow1())
    datebase22=tk.StringVar()
    datebase22.set(datebaseshow.attributedatebaseshow2())
    contentdatebase21=tk.Label(window,textvariable=datebase21)
    contentdatebase21.grid(row=15,column=2)
    contentdatebase22=tk.Label(window,textvariable=datebase22)
    contentdatebase22.grid(row=15,column=0)
    window.after(10000,show)
show()

#识别动物
animals_name=tk.Entry()
animals_attribute=tk.Entry()
animals_attribute2=tk.Entry()
animals_attribute3=tk.Entry()
animals_attribute4=tk.Entry()
annimalsrecognizeresult=[]
annimalsrecognizeresult=tk.StringVar()


def annimalsrecognize_hit():
    animalinput = []
    animalinput.append(animals_name.get())
    animalinput.append(animals_attribute.get())
    animalinput.append(animals_attribute2.get())
    animalinput.append(animals_attribute3.get())
    animalinput.append(animals_attribute4.get())
    annimalsrecognizeresult.set(recognize.recognizefunction(animalinput))


animalsRecognizeButton=tk.Button(window,text='动物识别',command=annimalsrecognize_hit )
animalsRecognizeButton.grid(row=0,column=0)
animalsRecognizeLabel=tk.Label(window,text="动物特征",bg='yellow')
animalsRecognizeLabel.grid(row=1,column=0)
animals_name.grid(row=2,column=0)
animals_attribute.grid(row=3,column=0)
animals_attribute2.grid(row=4,column=0)
animals_attribute3.grid(row=5,column=0)
animals_attribute4.grid(row=6,column=0)
animalsResultLabel=tk.Label(window,text="识别结果",bg='yellow')
animalsResultLabel.grid(row=7,column=0)
animalsResultOut=tk.Label(window,textvariable=annimalsrecognizeresult)
animalsResultOut.grid(row=8,column=0)



#增添动物
animaladd_name=tk.Entry()
animaladd_attribute=tk.Entry()
animaladd_attribute2=tk.Entry()
animaladd_attribute3=tk.Entry()
annimaladdresult=[]
annimaladdresult=tk.StringVar()

def annimaladd_hit():
    animaladdinput =[]
    animaladdinput.append(animaladd_name.get())
    animaladdinput.append(animaladd_attribute.get())
    animaladdinput.append(animaladd_attribute2.get())
    animaladdinput.append(animaladd_attribute3.get())
    animal_add.animalsadd(animaladdinput)
    if animaladdinput[0]!='':
        annimaladdresult.set(animaladdinput[0]+'已经被添加进动物库')

animaladdButton=tk.Button(window,text='添加动物',command=annimaladd_hit )
animaladdButton.grid(row=0,column=1)
animaladdLabel=tk.Label(window,text="动物名称",bg='yellow')
animaladdLabel.grid(row=1,column=1)
animaladd_name.grid(row=2,column=1)
animaladdLabel=tk.Label(window,text="动物特性",bg='yellow')
animaladdLabel.grid(row=3,column=1)
animaladd_attribute.grid(row=4,column=1)
animaladd_attribute2.grid(row=5,column=1)
animaladd_attribute3.grid(row=6,column=1)
animaladdOut=tk.Label(window,textvariable=annimaladdresult)
animaladdOut.grid(row=8,column=1)



#增添属性
attributesadd_name=tk.Entry()
attributesadd_attribute=tk.Entry()
attributesadd_attribute2=tk.Entry()
attributesadd_attribute3=tk.Entry()
attributesaddresult=[]
attributesaddresult=tk.StringVar()

def attributesadd_hit():
    attributesaddinput =[]
    attributesaddinput.append(attributesadd_name.get())
    attributesaddinput.append(attributesadd_attribute.get())
    attributesaddinput.append(attributesadd_attribute2.get())
    attributesaddinput.append(attributesadd_attribute3.get())
    attribute_add.attributesadd(attributesaddinput)
    if attributesaddinput[0] != '':
        attributesaddresult.set(attributesadd_name.get()+'已经被添加进属性库')

attributesaddButton=tk.Button(window,text='添加属性',command=attributesadd_hit )
attributesaddButton.grid(row=0,column=2)
attributesaddLabel=tk.Label(window,text="属性名称",bg='yellow')
attributesaddLabel.grid(row=1,column=2)
attributesadd_name.grid(row=2,column=2)
attributesaddLabel=tk.Label(window,text="属性特性",bg='yellow')
attributesaddLabel.grid(row=3,column=2)
attributesadd_attribute.grid(row=4,column=2)
attributesadd_attribute2.grid(row=5,column=2)
attributesadd_attribute3.grid(row=6,column=2)
attributesaddOut=tk.Label(window,textvariable=attributesaddresult)
attributesaddOut.grid(row=8,column=2)



#删减
contentdelete=tk.Entry()
contentdeleteresult=[]
contentdeleteresult=tk.StringVar()

def contentdelete_hit():
    contentdeleteinput =[]
    contentdeleteinput=contentdelete.get()
    contentdeleteresult.set(delete.content_delete(contentdeleteinput))


contentdeleteButton=tk.Button(window,text='删除',command=contentdelete_hit)
contentdeleteButton.grid(row=0,column=3)
contentdeleteLabel=tk.Label(window,text="删除内容",bg='yellow')
contentdeleteLabel.grid(row=1,column=3)
contentdelete.grid(row=2,column=3)
contentdeleteOut=tk.Label(window,textvariable=contentdeleteresult)
contentdeleteOut.grid(row=3,column=3)

#刷新


load = Image.open('ddas.jfif')
render = ImageTk.PhotoImage(load)
img = tk.Label(window,image=render)
img.place(x=680,y=150)

window.mainloop()