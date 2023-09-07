#######################
#########dogru cevap


import csv
import sqlite3
con = sqlite3.connect("Persons.db")
cur = con.cursor()
# cur.execute("CREATE TABLE persons(number, name, birthdate)")
print("Tietokanta luotu ja taulu lisätty.")
with open('Henkilöt.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Number'], row['Name'], row['Birthdate'])
        # Huom! SQL Injection -hyökkäyksen vaara!
        sql = "INSERT INTO persons VALUES (" + row['Number'] + ", '"+ row['Name'] +"', " + "'" + row['Birthdate'] +"')"
        print(sql)
        cur.execute(sql)
print("INSERT-komennot ajettu, tehdään commit.")
con.commit()
print("Tiedot tallennettu onnistuneesti SQLite-kantaan.")



#######################################

import pandas as pd
import sqlite3

database_connection = sqlite3.connect('testi.db')
c = database_connection.cursor()


Henkilöt_lista =[]
tiedosto = open("Henkilöt.csv", "r")
for rivi in tiedosto:
    Henkilöt_lista.append(rivi)


c.execute('''CREATE TABLE Henkilöt
             (Number, Name, Birthdate)''')

for data_row in Henkilöt_lista:
    c.execute('''INSERT INTO Henkilöt VALUES {0}'''.format(data_row))
database_connection.commit()


sql_query = '''SELECT * FROM Henkilöt'''
dataframe_from_sqlite = pd.read_sql(sql_query, database_connection)
dataframe_from_sqlite