import numpy as np

##############
# a
table1 = np.random.randint(10, size=10)
print (table1)


###############
# b

print (np.sort(table1))


###############
# c
table2 = np.random.randint(10, size=10)
print (table2)

summa = np.sum([table1, table2], axis=0)

print(summa)