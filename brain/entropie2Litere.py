from tika import parser
import math

carti = ['carte2.pdf', 'carte3.pdf', 'carte4.pdf', 'carte5.pdf']

dictionar = {}

def entropiePeDouaLitere():
    for carte in carti:

        raw = parser.from_file(carte)

        raw = raw['content']

        startIndex = 0

        while startIndex < len(raw) - 1:

            currenyKey = raw[startIndex] + raw[startIndex + 1]

            if currenyKey in dictionar:
                dictionar[currenyKey]+=1
            else:
                dictionar[currenyKey]=1
            
            startIndex+=1


entropiePeDouaLitere()

sortedDict = {k: v for k, v in sorted(dictionar.items(), key=lambda item: item[1])}
print(sortedDict)

total = 0

for i, val in sortedDict.items():
    total+=val

entropie = 0

for i, val in sortedDict.items():
    entropie+= (-val/total)*math.log2(val/total)

print(entropie)

#  8.208700929391563 => ~4.1/ litera < 4.53