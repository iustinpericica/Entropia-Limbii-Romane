from tika import parser
import math
import json
from shared import transofrmareString
from math import log2
carti = ['../carti/carte2.pdf', '../carti/carte3.pdf', '../carti/carte4.pdf', '../carti/carte5.pdf', '../carti/carte6.pdf', '../carti/carte7.pdf'
, '../carti/carte8.pdf', '../carti/carte9.pdf', '../carti/carte10.pdf', '../carti/carte11.pdf', '../carti/carte12.pdf']

dictionarSufix = {}

prefix = 3

lungimeaTotalaCuvinte = 0
contorCuvinte = 0

for carte in carti:

    raw = parser.from_file(carte)

    raw = raw['content']
    if raw:
        for cuvant in raw.split(' '):
            cuv = transofrmareString(cuvant)
            if cuv != -1 and len(cuv) > prefix:
                if cuv[:prefix] in dictionarSufix:
                    if cuv[prefix:] in dictionarSufix[cuv[:prefix]]:
                        dictionarSufix[cuv[:prefix]][cuv[prefix:]]+=1
                    else:
                        dictionarSufix[cuv[:prefix]][cuv[prefix:]] = 1
                else:
                    dictionarSufix[cuv[:prefix]] = {}
                    dictionarSufix[cuv[:prefix]][cuv[prefix:]] = 1
            elif cuv != -1 and len(cuv) == prefix:
                # de ex ,, pas "
                if cuv in dictionarSufix:
                    if ' ' in dictionarSufix[cuv]:
                        dictionarSufix[cuv][' ']+=1
                    else:
                        dictionarSufix[cuv][' '] = 1
                else:
                    dictionarSufix[cuv] = {}
                    dictionarSufix[cuv][' '] = 1

            if cuv != -1:
                contorCuvinte+=1
                lungimeaTotalaCuvinte+= len(cuv)

# am terminat de analizat sufixele pentru date

# incep sa analizez din dictionar

with open('Dataset.json') as json_file:
    data = json.load(json_file)
    for cuv in data:
        cuv = transofrmareString(cuvant)
        if cuv != -1 and len(cuv) > prefix:
            if cuv[:prefix] in dictionarSufix:
                if cuv[prefix:] in dictionarSufix[cuv[:prefix]]:
                    dictionarSufix[cuv[:prefix]][cuv[prefix:]]+=1
                else:
                    dictionarSufix[cuv[:prefix]][cuv[prefix:]] = 1
            else:
                dictionarSufix[cuv[:prefix]] = {}
                dictionarSufix[cuv[:prefix]][cuv[prefix:]] = 1
        elif cuv != -1 and len(cuv) == prefix:
            if cuv in dictionarSufix:
                if ' ' in dictionarSufix[cuv]:
                    dictionarSufix[cuv][' ']+=1
                else:
                    dictionarSufix[cuv][' '] = 1
            else:
                dictionarSufix[cuv] = {}
                dictionarSufix[cuv][' '] = 1

# am terminat de analizat din dictionar

# ---------------- INCEPERE calculare entropie sufix medie ----------

entropieSufixTotal = 0
nEntropieSufixTotal = 0

for key in dictionarSufix:
    # dictionarSufix[key] = prefix
    nEntropieSufixTotal+=1
    total = 0
    for sufix in dictionarSufix[key]:
        total+=dictionarSufix[key][sufix]

    for sufix in dictionarSufix[key]:
        p = dictionarSufix[key][sufix] / total
        entropieSufixTotal = entropieSufixTotal + (-p*log2(p))

entropieSufixMedie = entropieSufixTotal / nEntropieSufixTotal

# ---------------- TERMINARE calculare entropie sufix medie ----------

# ---------------- INCEPERE calculare entropie prefix medie ----------

entropiePrefixTotal = 0

with open('prefixeCuvinteFrecvente.json') as json_file:
    dictionarPrefix = json.load(json_file)
    totalPrefixeContor = 0

    for prefix in dictionarPrefix:
        totalPrefixeContor += dictionarPrefix[prefix]

    
    for prefix in dictionarPrefix:
        p = dictionarPrefix[prefix] / totalPrefixeContor
        entropiePrefixTotal = entropiePrefixTotal + (-p*log2(p))

# ---------------- TERMINARE calculare entropie prefix medie ----------


lungimeMedieCuvant = lungimeaTotalaCuvinte/contorCuvinte

with open("sufixeFrecvente.json", "w") as f:
    json.dump(dictionarSufix, f)

print("Lungime medie a unui cuvant", lungimeMedieCuvant)

print("Prefix total", entropiePrefixTotal)

print("Sufix total", entropieSufixMedie)

print("Biti pe litera:", ((entropieSufixMedie + entropiePrefixTotal)/lungimeMedieCuvant))