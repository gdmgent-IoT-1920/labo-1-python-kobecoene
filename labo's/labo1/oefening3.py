from random import randint

print("LINGO-BINGO Welcome to the chicken and egg game! ")
def returnMatches(a,b):
	return list(set(a) & set(b))

comp_number = randint(1000, 10000)
# print(comp_number)

user_number = int(input("Guess the 4 digit number:"))
tries = 1 

while user_number != comp_number:
	comp_array = [int(x) for x in str(comp_number)] 
	user_array = [int(y) for y in str(user_number)] 
	
	chickens = len([i for i,j in zip(comp_array, user_array) if i == j])
	eggs = len(returnMatches(comp_array, user_array)) - chickens

	if eggs < 0:
		eggs = 0

	print(f"U have {chickens} chickens and {eggs} eggs, try again")

	user_number = int(input("Guess the 4 digit number:"))
	tries += 1

print(f"Correct, you guessed it in {tries} tries")