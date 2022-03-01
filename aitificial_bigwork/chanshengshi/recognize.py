import csv
#输入控制
def recognizefunction(synthesisdatebase):
    result=''
    #判断是否添加属性
    adatebase=list(csv.reader(open('attributes.csv',encoding='utf-8')))
    change=1
    while change==1:
        change=0
        for line in adatebase:
            if line[0] in synthesisdatebase:
                continue
            else:
                attribute = line[0]
                words=0
                wordcount=0

                for word in line[1:]:
                    words +=1
                    if word in synthesisdatebase:
                        wordcount +=1
                    else:
                        break

            if words==wordcount and words !=0:
                synthesisdatebase.append(attribute)
                change=1


    #判断是否有动物符合
    animalsdatebase=list(csv.reader(open('animals.csv',encoding='utf-8')))
    fuhen=0
    for line in animalsdatebase:
        words = 0
        wordcount = 0
        for word in line[1:]:
            words += 1
            if word in synthesisdatebase:
                wordcount += 1
            else:
                break
        if words == wordcount and words != 0:
            result +=line[0]+'符合条件\n'
            fuhen=1
    if  fuhen==0:
        result='寻找不到动物'

    return result







