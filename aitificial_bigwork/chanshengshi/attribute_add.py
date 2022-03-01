import csv

def attributesadd(characteristics):
    if characteristics[0] =='':
        pass
    else:
        with open('attributes.csv','a',encoding='utf-8') as attributescsv :
            attributescsv.write(characteristics[0])
            for word in characteristics[1:]:
                attributescsv.write(','+word)
            attributescsv.write('\n')