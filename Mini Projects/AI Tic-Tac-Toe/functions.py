# DO NOT CHANGE THIS FILE!
import os, time, random

###### Operating System Functions ######


# clear the terminal.
def clearscreen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# wait a set amount of time in seconds 
# to continue execute the program.
def wait(seconds: float) -> None:
    time.sleep(seconds)


################# Game #################


# generate a new game board.
def newgame() -> list:
    return [['n', 'n', 'n'],
            ['n', 'n', 'n'],
            ['n', 'n', 'n']
            ]


# check avaliable space on board
def get_avaliable_space(gameboard: list) -> list:
    avaliable = []
    for one in range(len(gameboard)):
        for two in range(len(gameboard[one])):
            if gameboard[one][two] == 'n':
                avaliable.append((one + 1, two + 1))
    return avaliable


# place a stone on board, will warn if move is invalid.
def place_stone(gameboard: list, row: int, column: int, stone: str) -> list:

    valid = get_avaliable_space(gameboard)

    # if it is not 'n' then there is already a stone.
    if (row, column) not in valid:
        print('Invalid Move.')
        return gameboard
    
    # it is a valid move.
    else:
        gameboard[row - 1][column - 1] = stone
        return gameboard
    

# check if anyone wins
def check_winner(gameboard: list) -> bool:

    row_one = gameboard[0]
    row_two = gameboard[1]
    row_three = gameboard[2]
    if row_one.count(row_one[0]) == len(row_one) and row_one[0] != 'n':
        print(row_one[0] + ' wins by row!')
        return True
    elif row_two.count(row_two[0]) == len(row_two) and row_two[0] != 'n':
        print(row_two[0] + ' wins by row!')
        return True
    elif row_three.count(row_three[0]) == len(row_three) and row_three[0] != 'n':
        print(row_three[0] + ' wins by row!')
        return True
    
    column_one = [gameboard[0][0], gameboard[1][0], gameboard[2][0]]
    column_two = [gameboard[0][1], gameboard[1][1], gameboard[2][1]]
    column_three = [gameboard[0][2], gameboard[1][2], gameboard[2][2]]
    if column_one.count(column_one[0]) == len(column_one) and column_one[0] != 'n':
        print(column_one[0] + ' wins by column!')
        return True
    elif column_two.count(column_two[0]) == len(column_two) and column_two[0] != 'n':
        print(column_two[0] + ' wins by column!')
        return True
    elif column_three.count(column_three[0]) == len(column_three) and column_three[0] != 'n':
        print(column_three[0] + ' wins by column!')
        return True

    cross_one = [gameboard[0][0], gameboard[1][1], gameboard[2][2]]
    cross_two = [gameboard[0][2], gameboard[1][1], gameboard[2][0]]
    if cross_one.count(cross_one[0]) == len(cross_one) and cross_one[0] != 'n':
        print(cross_one[0] + ' wins by cross!')
        return True
    elif cross_two.count(cross_two[0]) == len(cross_two) and cross_two[0] != 'n':
        print(cross_two[0] + ' wins by cross!')
        return True
    return False


def print_board(gameboard: list) -> None:
    print(str(gameboard[0]) + '\n' + str(gameboard[1]) + '\n' + str(gameboard[2]))


################## AI ##################


# AI that randomly place stone.
def random_ai_move(gameboard: list, current_stone: str) -> list:
    
    avaliable = get_avaliable_space(gameboard)
    select = random.choice(avaliable)
    print('placing: '+ str(select))
    return place_stone(gameboard, select[0], select[1], current_stone)


# AI that prioritize winning and centre
def helper_greedy_ai(gameboard, current_stone):
    avaliable = []
    for one in range(len(gameboard)):
        for two in range(len(gameboard[one])):
            if gameboard[one][two] == current_stone:
                avaliable.append((one + 1, two + 1))
    return avaliable


def greedy_ai_move(gameboard: list, current_stone: str) -> list:
    
    avaliable = get_avaliable_space(gameboard)
    select = random.choice(avaliable)
    
    current_stone_location = helper_greedy_ai(gameboard, current_stone)
    print('On board: ' + str(current_stone_location))
    pool = []
    for location1 in current_stone_location:
        for location2 in current_stone_location:
            if (location1 != location2) and (location1[0] == location2[0]):
                pool.extend([location for location in avaliable if location in [(location1[0], 1), (location1[0], 2), (location1[0], 3)]])
            elif (location1 != location2) and (location1[1] == location2[1]):
                pool.extend([location for location in avaliable if location in [(1, location1[1]), (2, location1[1]), (3, location1[1])]])
    if pool != []:
        select = random.choice(pool)
        
    elif gameboard[1][1] == 'n':
        select = (2, 2)

    print('placing: '+ str(select))
    return place_stone(gameboard, select[0], select[1], current_stone)


def change_stone(current_stone: str) -> str:
    if current_stone == 'x':
        return 'o'
    else:
        return 'x'
