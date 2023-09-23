# Sample Solution

from functions import clearscreen, wait, newgame
from functions import get_avaliable_space, place_stone, check_winner, print_board, change_stone
from functions import greedy_ai_move, random_ai_move


def gameloop() -> None:
    'the main game loop of the game.'
    clearscreen()
    playing = True
    current_stone = 'x'
    gameboard = newgame()
    while playing:

        if check_winner(gameboard):
            break
        elif get_avaliable_space(gameboard) == []:
            print('Draw!')
            break

        wait(5)
        gameboard = random_ai_move(gameboard, current_stone)
        print_board(gameboard)
        wait(5)
        print()

        current_stone = change_stone(current_stone)
        wait(5)
        gameboard = greedy_ai_move(gameboard, current_stone)
        print_board(gameboard)
        wait(5)
        print()

        current_stone = change_stone(current_stone)


        

