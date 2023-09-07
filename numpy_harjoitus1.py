
import numpy as np

##############
# taulukon määrittely
table1 = np.random.randint(10, size=10)
print (table1)
# t1 = np.array( [1,2,4,5])
# t2 = np.array( [3,2,7,5])

###############
# taulokon lajittelu

print (np.sort(table1))


###############
# kahden taulukon laskeminen yhteen
table2 = np.random.randint(10, size=10)
print (table2)

summa = np.sum([table1, table2], axis=0)
# summa = np.add (t1,t2)

print(summa)