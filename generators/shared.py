
def transofrmareString(stringDePus):
    if '(' in stringDePus:
        stringDePus = stringDePus[:stringDePus.find('(')]

    if '/' in stringDePus:
        stringDePus = stringDePus[:stringDePus.find('/')]

    index = 0
    while index < len(stringDePus): 
            if not stringDePus[index].isalpha():
                return -1

            if stringDePus[index] in '+*-*/*.0123456789-=+=-`~!@#$%^&*()[];./?><:"|':
                return -1

            index+=1

    if stringDePus == '' or stringDePus == ' ':
        return -1

    return stringDePus.lower()

