import random, time
import os

score_player = 0
score_bot = 0

while True:
    print("This is a RPS game, are you ready to start")
    start = str(input('type: "yes" when ready   '))
    if start.lower() != 'yes':
        print('I will wait until you are ready.')
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        break

while True:
    print('What will you choose?')
    choice = str(input('"r", "p", or "s"?   '))
    computer = random.choice(['r', 'p', 's'])
    print('Computer chooses ' + computer)
    if computer == 'r' and choice == 's':
        score_bot += 1
        print('Com wins, the score is ' +  str(score_player) + ' : ' + str(score_bot))
        choice = str(input('Continue? yes/no:    '))
        if start.lower() != 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    
    elif computer == 'r' and choice == 'p':
        score_player += 1
        print('Player wins, the score is ' +  str(score_player) + ' : ' + str(score_bot))
        choice = str(input('Continue? yes/no:    '))
        if start.lower() != 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    
    elif computer == 'p' and choice == 's':
        score_player += 1
        print('Player wins, the score is ' +  str(score_player) + ' : ' + str(score_bot))
        choice = str(input('Continue? yes/no:    '))
        if start.lower() != 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
        
    elif computer == 'p' and choice == 'r':
        score_bot += 1
        print('Com wins, the score is ' +  str(score_player) + ' : ' + str(score_bot))
        choice = str(input('Continue? yes/no:    '))
        if start.lower() != 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    elif computer == 's' and choice == 'p':
        score_bot += 1
        print('Com wins, the score is ' +  str(score_player) + ' : ' + str(score_bot))
        choice = str(input('Continue? yes/no:    '))
        if start.lower() != 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    
    elif computer == 's' and choice == 'r':
        score_player += 1
        print('Player wins, the score is ' +  str(score_player) + ' : ' + str(score_bot))
        choice = str(input('Continue? yes/no:    '))
        if start.lower() != 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    elif choice.lower() not in ['r', 'p', 's'] and choice != '':
        print('Please choose something valid.')
        print(str(score_player) + ' : ' + str(score_bot))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice == '':
        print('Player forfeit, com wins!')
        score_bot += 1
        print(str(score_player) + ' : ' + str(score_bot))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    else:
        print('Draw! ' +  str(score_player) + ' : ' + str(score_bot))
        choice = str(input('Continue? yes/no:    '))
        if start.lower() != 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    
