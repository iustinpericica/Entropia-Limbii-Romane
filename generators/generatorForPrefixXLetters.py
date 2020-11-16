from tika import parser
import math
import json
from shared import transofrmareString
from math import log2
carti = ['../carti/carte2.pdf', '../carti/carte3.pdf', '../carti/carte4.pdf', '../carti/carte5.pdf', '../carti/carte6.pdf', '../carti/carte7.pdf'
, '../carti/carte8.pdf', '../carti/carte9.pdf', '../carti/carte10.pdf', '../carti/carte11.pdf', '../carti/carte12.pdf']

dictionarPrefix = {}

prefix = 3

for carte in carti:

    raw = parser.from_file(carte)

    raw = raw['content']
    if raw:
        for cuvant in raw.split(' '):
            cuv = transofrmareString(cuvant)
            if cuv != -1 and len(cuv) > prefix:
                if cuv[:prefix] in dictionarPrefix:
                    dictionarPrefix[cuv[:prefix]]+=1
                else:
                    dictionarPrefix[cuv[:prefix]] = 0
                    dictionarPrefix[cuv[:prefix]]+=1
            elif cuv != -1 and len(cuv) == 3:
                if cuv in dictionarPrefix:
                    dictionarPrefix[cuv]+=1
                else:
                    dictionarPrefix[cuv] = 1
            elif cuv != -1 and len(cuv) == 2:
                if cuv in dictionarPrefix:
                    dictionarPrefix[cuv]+=1
                else:
                    dictionarPrefix[cuv] = 1
            elif cuv != -1 and len(cuv) == 1:
                cuv = '00' + cuv
                if cuv in dictionarPrefix:
                    dictionarPrefix[cuv]+=1
                else:
                    dictionarPrefix[cuv] = 1


with open('Dataset.json') as json_file:
    data = json.load(json_file)
    for cuv in data:
        cuvNou = transofrmareString(cuv)
        if cuvNou!=-1 and len(cuvNou) > prefix and not(cuvNou[:prefix] in dictionarPrefix):
            dictionarPrefix[cuvNou[:prefix]] = 1
            # daca prefixul meu nu apare in 10 romane analizate, atunci ii consider totalul de aparitii fiind 1 .
        elif cuvNou != -1 and len(cuvNou) == 3:
            if cuvNou in dictionarPrefix:
                dictionarPrefix[cuvNou]+=1
            else:
                dictionarPrefix[cuvNou] = 1
        elif cuvNou != -1 and len(cuvNou) == 2:
            cuvNou = '0' + cuvNou
            if cuvNou in dictionarPrefix:
                dictionarPrefix[cuvNou]+=1
            else:
                dictionarPrefix[cuvNou] = 1
        elif cuvNou != -1 and len(cuvNou) == 1:
            cuvNou = '00' + cuvNou
            if cuvNou in dictionarPrefix:
                dictionarPrefix[cuvNou]+=1
            else:
                dictionarPrefix[cuvNou] = 1
        
            

with open("prefixeCuvinteFrecvente.json", "w") as f:
    json.dump(dictionarPrefix, f)




