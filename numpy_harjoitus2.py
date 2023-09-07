### numpy ile csv dosyasini oku ve yillarin medyanini bul


import csv
import numpy as np
vuosiluvut = []
with open('Henkilöt.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        syntymäaika = row['Birthdate']
        vuosi = syntymäaika[:4]
        try:
            vuosiluku = int(vuosi)
            vuosiluvut.append(vuosiluku)
        except:
            pass
# laske mediaani
taulukko = np.array(vuosiluvut)
mediaani = np.median(taulukko)
print("Syntymävuosien mediaani on:", mediaani)


###################
# benim calismam

import csv
import numpy as np


#taulukko = np.array([])
taulukko = []
with open('Henkilöt.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # taulukko = taulukko + row['Birthdate']
        #print(row['Number'], row['Name'], row['Birthdate'])
        #np.ndarray (row['Number'], row['Name'], row['Birthdate'])
        #data_array = np.ndarray(row)
        taulukko.append(row['Birthdate'])
      

print (taulukko)
#data = np.loadtxt('Henkilöt.csv',delimiter=',')  



#print (data_array)

