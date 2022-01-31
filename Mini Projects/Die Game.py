from platform import win32_edition
import random

die1 = random.randint (1,6)
die2 = random.randint (1,6)
die3 = random.randint (1,6)

print (die1, die2, die3)
print (die1 + die2 + die3)

if (die1 + die2 + die3) == 7 or (die1 + die2 + die3)== 11:
    
    print ("you Win")

    print ("you Lost")

