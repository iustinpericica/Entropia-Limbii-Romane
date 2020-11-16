
def transofrmareString(stringDePus):
    if '(' in stringDePus:
        stringDePus = stringDePus[:stringDePus.find('(')]

    if '/' in stringDePus:
        stringDePus = stringDePus[:stringDePus.find('/')]

    index = 0
    while index < len(stringDePus):
            if stringDePus[index] == 'ș':
                stringDePus = stringDePus[:index] + 's' + stringDePus[index + 1:]
            elif stringDePus[index] == 'ț':
                stringDePus = stringDePus[:index] + 't' + stringDePus[index + 1:]
            elif stringDePus[index] in 'ăâ':
                stringDePus = stringDePus[:index] + 'a' + stringDePus[index + 1:]
            elif stringDePus[index] == 'î':
                stringDePus = stringDePus[:index] + 'i' + stringDePus[index + 1:]   

            if not stringDePus[index].isalpha():
                return -1

            if stringDePus[index] == ' ':
                return -1

            index+=1

    if stringDePus == '' or stringDePus == ' ':
        return -1

    return stringDePus.lower()

