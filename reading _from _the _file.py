###################
#reading from the file

numbers = open("/Users/kayttaja/Desktop/Orion-Saranen/Päivä7-Python_Ohjelmointi/data_text", "r")

sum = 0
for rows in numbers:
    print(rows)
    sum = sum + int(rows)

print("--------")
print(sum)


##################

tiedosto = open("/Users/kayttaja/Desktop/Orion-Saranen/Päivä7-Python_Ohjelmointi/data_text", "r")
summa = 0
lukumäärä = 0
for rivi in tiedosto:
  # print(rivi)
  summa = summa + int(rivi)
  lukumäärä = lukumäärä + 1
keskiarvo = summa / lukumäärä
print("------")
print("Summa:", summa)
print("Keskiarvo:", keskiarvo)



######################

## epäluotettava datan käsittely 
## exception handling

tiedosto = open("/Users/kayttaja/Desktop/Orion-Saranen/Päivä7-Python_Ohjelmointi/data_text2", "r")

summa = 0
lukumäärä = 0
for rivi in tiedosto:
  # print(rivi)
    try:
        summa = summa + int(rivi)
        lukumäärä = lukumäärä + 1
    except:
        print("virheellinen rivi tiedostossa!")

keskiarvo = summa / lukumäärä
print("------")
print("Summa:", summa)
print("Keskiarvo:", keskiarvo)