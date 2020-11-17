# Entropia-Limbii-Romane

Pentru a rula acest proiect:

1. <p>pentru entropia pe o singura litera/ pe x litere:</p>
  <p>brain/entropieXLitere</p>
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
    
  <p>pentru calcularea sufixelor: calculateEntropy.py</p>
   <p>Acest program face:</p>
   <ul>
  <li>a. calculeaza dictionarul de sufixe pentru carti</li>
      <li>b. calculeaza dictionarul de sufixe pentru dictionarul dex</li>
      <li>c. calculeaza entropia medie pentru sufix</li></li>
      <li>d. calculeaza entropia medie pentru prefix</li>
      <li>e. entropia finala este: ((entropieSufixMedie + entropiePrefixTotal)/lungimeMedieCuvant))</li>
   </ul>
    
    
