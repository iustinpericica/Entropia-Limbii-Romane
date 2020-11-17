# Entropia-Limbii-Romane

Pentru a rula acest proiect:

1. pentru entropia pe o singura litera/ pe x litere:
  brain/entropieXLitere
2. pentru entropia cu prefixe si sufixe:

  salvati pe localhost in sql baza de date dex - optional
  Sunt salvate toate cuvintele in generators/Dataset.json
  
  <b>Si la sufixe si la prefixe, punem frecventa 1 pe cuvintele/sufixele/ prefixele pe care le gasim in DEX.</b>
  
  pentru calcularea prefixelor:
    generatorForPrefixXLetters.py => prefixeCuvinteFrecvente.json
    
    cuvantul ou => '0ou'
    cuvantul a => '00a'
    cuvantul pas => 'pas'
    cuvantul casa =>  prefix = 'cas'
    
  pentru calcularea sufixelor:
    calculateEntropy.py
    Acest program face:
      a. calculeaza dictionarul de sufixe pentru carti
      b. calculeaza dictionarul de sufixe pentru dictionarul dex
      c. calculeaza entropia medie pentru sufix
      d. calculeaza entropia medie pentru prefix
      e. entropia finala este: ((entropieSufixMedie + entropiePrefixTotal)/lungimeMedieCuvant))
    
    
