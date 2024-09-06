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

# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")

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
        
        #swap players
        if cur_player == 'x':
            cur_player = 'o'
        else:
            cur_player = 'x'
        
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

if __name__ == "__main__":
    print("player 1")
    player1 = input("Enter name: ")
    print('\n')

    print("Player 2")
    player2 = input("Enter name: ")
    print('\n')

    #store game information
    cur_player = player1
    player_choice = {'x' : "", 'o': ""}
    options = ['x','o'] 
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    while True:
        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1
