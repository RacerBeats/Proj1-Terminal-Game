#Print Tic Tac Toe Board
def print_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

def single_game(cur_player):
    values = [' ' for x in range(9)]
    player_pos = {'x':[], 'o':[]}
    while True:
        print_board(values)
        #sanity checks and error handling
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong input, try again")
            continue
        if move < 1 or move > 9:
            print("Wrong input, try again")
            continue
        if values[move-1] != " ":
            print('Place already filled. Try again!!')
            continue
        
        values[move-1] = cur_player
        player_pos[cur_player].append(move)

        #win check
        if check_win(player_pos, cur_player):
            print_board(values)
            print("Player ", cur_player, " has won the game\n")
            return cur_player
        #draw game
        if check_draw(player_pos):
            print_board(values)
            print("Draw Game\n")
            return 'D'
        
def check_win(player_pos, cur_player):
    #winning combos
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            return True
    return False

#draw game check
def check_draw(player_pos):
    if len(player_pos['x']) + len(player_pos['o']) == 9:
        return True
    return False

        
