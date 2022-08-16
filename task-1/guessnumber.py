import random

max_value =int(input('Enter your level from 1(HIGH) to 10(LOW) : '))

if max_value==0 or max_value>10:
		print("\n\tLevel zero is not available\n\t\tGame over")
		exit()
remaining_attempts=float(1)
remaining_attempts=max_value*2

player_state=bool(False)
bot_state=bool(False)

if max_value<=3:
	level="Hard"
elif max_value>3 and max_value<=6:
	level="Medium"
else:
	level="Easy"


print('Level applied : ',level,"\nYou got ", remaining_attempts," attempts")
print('I am thinking No. between 1-100')
number= random.randint(1, 100)
bot_input=random.randint(1,100)

for I in range(remaining_attempts):
	remaining_attempts=remaining_attempts-1
	try:
			
		guess = int(input('\nEnter your guess '))
		if bot_input==number:
			bot_state=True
		if guess==number:
			player_state=True
			bonus=float(remaining_attempts+10)
			remaining_attempts=remaining_attempts+bonus			
			print("\n Congratulations,You got ",bonus," bonus points")			
			break
		if number%2==0:
		        print("No. is Even")
		else:
		        print("No. is Odd")
		if guess > number:
			print('Your No. is too high')
		if guess < number:
			print('Your No. is too low')

	except ValueError:
		print("\nInvalid Input\n")

	
		remaining_attempts=remaining_attempts+1
print("\nGame over")
if remaining_attempts==0:
	print("You loose the game\n")