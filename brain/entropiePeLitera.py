from tika import parser
import math

carti = ['../carti/carte2.pdf', '../carti/carte3.pdf', '../carti/carte4.pdf', '../carti/carte5.pdf']

dictionar = {}

def entropiePeLitera():
    for carte in carti:

        raw = parser.from_file(carte)

        raw = raw['content']

        startIndex = 0

        while startIndex < len(raw):
            if raw[startIndex] in dictionar:
                dictionar[raw[startIndex]]+=1
            else:
                dictionar[raw[startIndex]] = 1
            startIndex+=1


entropiePeLitera()

total = 0

for i, val in dictionar.items():
    total+=val

entropie = 0

for i, val in dictionar.items():
    entropie+= (-val/total)*math.log2(val/total)

print(entropie)

# 4.53