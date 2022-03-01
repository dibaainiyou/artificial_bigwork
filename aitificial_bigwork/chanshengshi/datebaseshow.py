import csv

def animalsdatebaseshow1():
    show11=''
    animalscsv=list(csv.reader(open('animals.csv', 'r', encoding='utf-8')))
    for word in animalscsv:
        show11 +=word[0]+'\n'
    return show11

def animalsdatebaseshow2():
    show12=''
    animalscsv=list(csv.reader(open('animals.csv', 'r', encoding='utf-8')))
    for word in animalscsv:
        for w in word[1:]:
            show12 +=w+','
        show12 +='\n'
    return show12

def attributedatebaseshow1():
    show11=''
    attributecsv=list(csv.reader(open('attributes.csv', 'r', encoding='utf-8')))
    for word in attributecsv:
        show11 +=word[0]+'\n'
    return show11

def attributedatebaseshow2():
    show12=''
    attributecsv=list(csv.reader(open('attributes.csv', 'r', encoding='utf-8')))
    for word in attributecsv:
        for w in word[1:]:
            show12 += w + ','
        show12 += '\n'
    return show12
