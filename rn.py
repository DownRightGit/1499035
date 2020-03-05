import random
guessTaken = True
msg = "Hello, let us play a game of Guess the number."
print(msg)
number = random.randint(1,20)
print('Guess a number between 1 and 20')
print(number)

while guessTaken:
    print ('Take a guess')
    guess = input()
    guess = int(guess)
    
   
    if guess < number:
        print ('Your guess is too low')
     
    if guess > number:
        print ('Your guess is too high')
        
    if guess == number:
        print ('Correct')
        guessTaken = False