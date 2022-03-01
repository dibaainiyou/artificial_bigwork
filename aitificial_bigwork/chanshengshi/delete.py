import csv

def content_delete(contentdeleteinput):
    result=''
    n=0
#content_delete=input('请输入你想删除的内容')
    #在属性库里寻找
    with open('attributes.csv','r',encoding='utf-8') as attributes:
        attributeslines=attributes.readlines()
    with open('attributes.csv','w',encoding='utf-8') as attributes:
        for l in attributeslines:
            a=''
            for everyzi in l:
                if everyzi != ',':
                    a = a+everyzi
                else:
                    break
            if contentdeleteinput != a:
                attributes.write(l)
            else:
                n=1
                result +=l+'已经被删除\n'

    #在动物库里删除
    with open('animals.csv', 'r', encoding='utf-8') as animals:
        animalslines = animals.readlines()
    with open('animals.csv', 'w', encoding='utf-8') as animals:
        for l in animalslines:
            a=''
            for everyzi in l:
                if everyzi != ',':
                    a = a+everyzi
                else:
                    break
            if contentdeleteinput != a:
                animals.write(l)
            else:
                n=1
                result +=l+'\n'
    if n==1:
        return result+'已经被删除'
    else:
        return '库里没有'+contentdeleteinput