#amazing quizz game

print("Welcome to the Quizz Game")

wanttoplay = input("Hey! Do you want to play the game? Y/N - ").lower()
score = 0

if wanttoplay != 'y':
    quit()
    
else:
    
    que_one = input("What is the full form of CPU? \n =>").lower()
    if que_one == 'central processing unit':
                    score += 1
                    
    que_two = input("\nWhat is the full form of GPU? \n =>").lower()
    if que_two == 'graphical processing unit':
        score += 1 
       
    que_three = input("\nWhat is the full form of RAM? \n =>").lower()
    if que_three == 'random access memory':
        score += 1
        
        
    que_four = input("\nWhat is the full form of ROM? \n =>").lower()
    if que_four == 'read only memory':
        score += 1
        
        
    print('\nHey! You did an amazing job')
    print("Your score is - ", score)
    print("Your score percentage is - ", score / 4 * 100)
