import csv

def animalsadd(attributes):
    if attributes[0]=='':
        pass
    else:
        with open('animals.csv', 'a', encoding='utf-8') as animalscsv :
            animalscsv.write(attributes[0])
            for word in attributes[1:]:
                animalscsv.write(','+word)
            animalscsv.write('\n')


