import mysql.connector
import json
from shared import transofrmareString

mydb = mysql.connector.connect(
  host="localhost",
  user="iustin",
  password="iustin",
  database="dict"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM entry")

myresult = mycursor.fetchall()

vectorWordsSortat = []

for x in myresult:
  stringDePus = x[1]
  vectorWordsSortat.append(transofrmareString(stringDePus))

vectorWordsSortat.sort()

with open("Dataset.json", "w") as f:
    json.dump(vectorWordsSortat, f)
