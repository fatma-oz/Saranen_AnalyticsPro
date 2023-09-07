
teksti = input("kirjoita jotain\n")

#kolmannen kirjaimen
a = teksti[2]
print (a)


#kaksi viimeista kirjainta
#lopusta alkaen
b = teksti [::-1][0:2]
print (b)
# b = teksti[-2:]
# b = teksti[-2] + teksti[-1]
# b = teksti[len(teksti) - 2:]


#koko merkkijono väärinpäin
c = teksti[::-1]
print (c)
# for i in range(len(teksti)):
#    print(teksti[-1 - i])



