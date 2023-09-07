
###############
import csv
import matplotlib.pyplot as plt
import numpy as np
vuosiluvut = []
vuosikymmenet = []
lukumäärät = []
with open('Henkilöt.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        syntymäaika = row['Birthdate']
        vuosi = syntymäaika[:4]
        try:
            vuosiluku = int(vuosi)
            vuosiluvut.append(vuosiluku)
            vuosikymmen = vuosiluku // 10 * 10
            try:
                indeksi = vuosikymmenet.index(vuosikymmen)
                lukumäärät[indeksi] = lukumäärät[indeksi] + 1
            except:
                vuosikymmenet.append(vuosikymmen)
                lukumäärät.append(1)
        except:
            pass
print(vuosikymmenet)
print(lukumäärät)
plt.rcdefaults()
sarakkeet = vuosikymmenet
y_pos = np.arange(len(sarakkeet))
luvut = lukumäärät
plt.bar(y_pos, luvut, align='center', alpha=0.5)
plt.xticks(y_pos, sarakkeet)
plt.ylabel('Lukumäärä')
plt.title('Henkilöiden syntymävuosikymmenet')
plt.show()

#############
# benim calismam


import matplotlib.pyplot as plt
import numpy as np
import csv


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


taulukko = np.array(vuosiluvut)

print(taulukko)

n_bins = 10
plt.hist(taulukko , bins= n_bins, align='mid', alpha=0.5 , histtype= "bar"  )
plt.ylabel('frequency')
plt.title('Birthdays of people')
plt.show() 




