from tika import parser
import math

carti = ['../carti/carte2.pdf', '../carti/carte3.pdf', '../carti/carte4.pdf', '../carti/carte5.pdf']

dictionar = {}

def entropieXLitere(x):
    for carte in carti:

        raw = parser.from_file(carte)

        raw = raw['content']

        startIndex = 0

        while startIndex < len(raw) - x:

            currenyKey = ''

            for i in range(x):
                currenyKey = currenyKey + raw[i + startIndex]

            if currenyKey in dictionar:
                dictionar[currenyKey]+=1
            else:
                dictionar[currenyKey]=1
            
            startIndex+=1

    total = 0

    for i, val in dictionar.items():
        total+=val

    entropie = 0

    for i, val in dictionar.items():
        entropie+= (-val/total)*math.log2(val/total)

    print("Entropy for {} letters in a group is {}".format(x, entropie/x))


for noLitere in range(1, 20):   
    #refresh global data
    dictionar = {}
    entropieXLitere(noLitere)


"""

Entropy for 1 letters in a group is 4.537670096042058
Entropy for 2 letters in a group is 4.1043513622948815
Entropy for 3 letters in a group is 3.7690479753219157
Entropy for 4 letters in a group is 3.4486700324786197
Entropy for 5 letters in a group is 3.1478463018786673
Entropy for 6 letters in a group is 2.867074014521568
Entropy for 7 letters in a group is 2.6051382693988656
Entropy for 8 letters in a group is 2.365439834882504
Entropy for 9 letters in a group is 2.1517800692170486
Entropy for 10 letters in a group is 1.965087134824784
Entropy for 11 letters in a group is 1.8031280290285354
Entropy for 12 letters in a group is 1.6626646912014689
Entropy for 13 letters in a group is 1.54067678202764
Entropy for 14 letters in a group is 1.4342738089379432
Entropy for 15 letters in a group is 1.3409556227728905
Entropy for 16 letters in a group is 1.2586395806683275
Entropy for 17 letters in a group is 1.18561416968905
Entropy for 18 letters in a group is 1.1204502260614086
Entropy for 19 letters in a group is 1.0619901357248756

"""


# PROGRAM AI
# predict n letter based on previous n-1 letters

# predict word based on 10 previous words

# subiect + verb.. etc
