from tika import parser
import math
import json

carti = ['carte2.pdf', 'carte3.pdf', 'carte4.pdf', 'carte5.pdf']

dictionar = {}

def entropiePeDouaLitere():
    for carte in carti:

        raw = parser.from_file(carte)

        raw = raw['content']

        startIndex = 0

        while startIndex < len(raw) - 2:

            currenyKey = raw[startIndex] + raw[startIndex + 1] + raw[startIndex + 2]

            # de imbunatatit - currentKey sa fie cuvant de 3/2/1 litera sau sa fie doar cele 3 litere de la inceputul unui cuvant

            if str.isalpha(currenyKey):

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

with open("dateSet3Car.json", "w") as f:
    json.dump(sortedDict, f)