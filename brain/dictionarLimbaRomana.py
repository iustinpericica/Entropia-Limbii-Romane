import mysql.connector
import json

vectorWordsSortat = []
frecvente3LitereDicionar = {}

with open('generators/Dataset.json') as json_file:
    data = json.load(json_file)
    vectorWordsSortat = data

with open('generators/dateSet3Car.json') as json_file:
    data = json.load(json_file)
    frecvente3LitereDicionar = data

def estePrefix(sir, potentialPrefix):
    lungimePotentialPrefix = len(potentialPrefix)
    return sir[:lungimePotentialPrefix] == potentialPrefix

def gasirePosibilitatiPentruCuvant(prefixPentruCandidati):
    for cuvant in vectorWordsSortat:
        if estePrefix(cuvant, prefixPentruCandidati):
            print(cuvant, end = " ")

listaDeCuvinte = ["abecedar", "carte", "mama"]

for cuvant in listaDeCuvinte:
    gasirePosibilitatiPentruCuvant(cuvant[:3])
    print("\n")

# ENTROPIA PE CARE O CAUT ESTE DE FAPT

# ENTROPIA PRIMELOR MIN(3, LEN(CUV)) + ENTROPIA A CEEA CE URMEAZA INDEXATA DUPA CAUTAREA BINARA DIN VECTOR EX:

# PT ANA => ANAB, ANAC, ANAD. ENTROPIA MEA ESTE: PT ..b = 5/12; C = 6/2; D = 1/12 U GOT IT MOTHERFUCKER, AND ALL I FUCKING NEED TO KNOW

# IS THE INDEX
#I MAKE BINARY SEARCH ON EMITTER VICE VERSA ON RECEPTOR FUCK U!