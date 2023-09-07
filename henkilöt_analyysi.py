

#########################


import pandas as pd
import numpy as np

data = pd.read_csv("Henkilöt.csv",sep=',', on_bad_lines='skip')   #, skipinitialspace =True
df = pd.DataFrame(data)
#print(df)

# a. onko kaikilla henkilöillä uniikki numerokoodi ( ensimmäinen sarake) ?

print( df["Number"].nunique()) 
print( df["Number"].is_unique ) 


# b. listää kuinka monta henkilöä on syntynyt kullakin vuosikymmenellä?

#print(df)
df_copy = df.copy()
df_copy = df_copy.drop([31]).reset_index()
# print(df_copy)

from datetime import datetime

df_copy['Birthdate'] = df_copy['Birthdate'].apply (lambda x: datetime.strptime(x,'%Y-%m-%d'))
#print(df_copy.dtypes)


df_copy['year'] = pd.DatetimeIndex(df_copy["Birthdate"]).year
#print(df_copy)



# c.mikä on syntymävuosien mediaani?
#df_copy.groupby(['year']).median

df_copy.groupby("year").median()


#######################



#tehtävän osa A

tiedosto = open("Henkilöt.csv", "r")
rivi_numero = 1
löytyneet_numerot = []
for rivi in tiedosto:
  if rivi_numero > 1:
    # print(rivi)
    pilkku = rivi.index(",")
    id_numero = int(rivi[:pilkku])
    try:
        löytyneet_numerot.index(id_numero)
        print("Löytyi tupla-numero:", id_numero)
    except:
       löytyneet_numerot.append(id_numero)
  rivi_numero = rivi_numero + 1

# tehtävän osa B
rivi_numero = 1
vuosikymmenet_lista = []
lukumäärät_lista = []
for rivi in tiedosto:
    if rivi_numero > 1:
       try:
          vuosi = int(rivi[-11:-7])
          vuosikymmen = vuosi // 10 * 10
          try:
             indeksi = vuosikymmenet_lista.index(vuosikymmen)
             lukumäärät_lista[indeksi] = lukumäärät_lista[indeksi] + 1
          except:
             vuosikymmenet_lista.append(vuosikymmen)
             lukumäärät_lista.append(1)
       except:
          pass
    rivi_numero = rivi_numero + 1
# tulostus
indeksi = 0
for vuosikymmen in vuosikymmenet_lista:
   lkm = lukumäärät_lista[indeksi]
   print(vuosikymmen, ":", lkm)
   indeksi = indeksi + 1