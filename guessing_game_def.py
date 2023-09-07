
#######################

bitmedi dahaaa!!!! asagida calisan kod var!!1

def quessing_game ():

    #random integer from 1 to 20
    import random 
    correct_number = random.randint(1, 20)

    print("\nWelcome quessing game. The machine has drawn numbers between 1 and 20. You have 3 guesses.")
    print (correct_number)

    for i in range (1,4):

        estimated_number = input( "Enter the guessed number between 1 and 20 \n" )
        
        if isinstance (estimated_number, int) == True:

            if (0 < estimated_number < 21):

                if correct_number == estimated_number:
                    print ("right guess"),
                    break
                elif correct_number > estimated_number:
                    print ("The correct number is bigger")
                elif correct_number < estimated_number:
                    print ("The correct number is smaller")

                print (f"You have {3-i} guesses")
        
                if i == 3:
                    print (f"you didn't guess, correct number is {correct_number}")

            else:
                print("estimated_number should be between 1-20, try again")

        else:
            print("estimated_number is not an integer, you should enter integer number")
        
         
        
quessing_game()






#######################

import random
def lue_luku():
    while True:
        try:
            syöte = input("Anna arvauksesi välillä 1-20: ")
            luku = int(syöte)
            if luku < 1:
                print("Luku on on liian pieni, sen pitää olla vähintään yksi.")
            elif luku > 20:
                print("Luku on on liian suuri, sen pitää olla enintään 20.")
            else:
                return luku
        except:
            print("Sinun tulee syöttää kelvollinen numero.")
oikea = random.randint(1,20)
# print(oikea)
for x in range(3):
    arvaus = lue_luku()
    if arvaus < oikea:
        print("Oikea luku on suurempi.")
    elif arvaus > oikea:
        print("Oikea luku on pienempi.")
    else:
        print("Arvasit oikein, voitit pelin!")
        break











