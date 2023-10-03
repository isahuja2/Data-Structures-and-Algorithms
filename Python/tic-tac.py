

def start_game():

    positions = {'1': ' ', '2': ' ', '3' : ' ', '4' : ' ','5': ' ', '6': ' ', '7' : ' ', '8' : ' ', '9': ' '}
    player1_choice = ''
    player2_choice = ''

    def create_board(positions):
        return ' {} | {} | {} \n   |   |   \n   |   |   \n-----------\n   |   |   \n   |   |   \n   |   |   \n-----------\n   |   |   \n   |   |   \n   |   |   \n'.format(positions['1'], positions['2'], positions['3'], positions['4'], positions['5'], positions['6'], positions['7'], positions['8'], positions['9'],)
    
    def initiate_game():
        global player1_choice
        global player2_choice
        while player1_choice != 'X' or player1_choice != 'O':
            if player1_choice == 'X' or player1_choice == 'O':
                player2_choice = 'O' if player1_choice == 'X' else 'X' 
                break
            else:
                player1_choice = input('Player1: Do you want to be X or O?\n')
        
        return player1_choice + player2_choice


    def greet():
        print('Welcome to Tic Tac Toe!')
        return initiate_game()
        
    return greet()


print(start_game())

