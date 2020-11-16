from tika import parser
import math

carti = ['carte2.pdf', 'carte3.pdf', 'carte4.pdf', 'carte5.pdf']

dictionar = {}

def entropiePeOLitera():
    for carte in carti:

        raw = parser.from_file(carte)

        for litera in raw['content']:

            if litera in dictionar:
                dictionar[litera]+=1
            else:
                dictionar[litera]=1


entropiePeOLitera()

sortedDict = {k: v for k, v in sorted(dictionar.items(), key=lambda item: item[1])}
print(sortedDict)

total = 0

for i, val in sortedDict.items():
    total+=val

entropie = 0

for i, val in sortedDict.items():
    entropie+= (-val/total)*math.log2(val/total)

print(entropie)


# 4.537672935303226