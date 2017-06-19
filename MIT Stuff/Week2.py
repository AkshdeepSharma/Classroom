print('Please think of a number between 0 and 100!')

low = 0
high = 100
while True:
    guess = (low + high) //2
    print('Is your secret number ' + str(guess) + "?")
    
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicated I guessed correctly. ")
    
    if answer == 'h':
        high = guess
    elif answer == 'l':
        low = guess
    elif answer == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    else:
        print('Sorry I did not understand your input.')
        
