import random

min_dice = 1
max_dice = int(input("Enter Maximum number of faces of dice : "))

dice1 = 1 
dice2 = 1
x=1
while(x != 0) :
	dice1 = random.randint(min_dice,max_dice)
	dice2 = random.randint(min_dice,max_dice)
	print("   ")
	print("On Dice 1 :",dice1,"On Dice 2 :", dice2)
	print("   ")
	print("To exit press 0 ")
	x = int(input("To roll dice again press number from 1 to 9 and hit enter "))
	if(x!=0	):
		continue
	else:
		break
		
		
# no comments added 
# this is the first comment 

# learning to branch 
# this is the first branch message 



	

