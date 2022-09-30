
import env
import random


def main():

    #init environment
    ttt = env.tictactoe()
    turn = random.randint(1,2)

    for i in range(9):
        
        valid = -1

        while valid == -1:
            box = input(f'it is player {turn}s turn. Please input the box')
            valid = ttt.load_pos(int(box))
            print('the value that you have placed is invalid. Please try again')

        #check winner
        win = ttt.chk_winner(turn)

        if win == 1:
            print(f'congratulations player {turn} won')
            print('ending game')

        turn = (turn + 1) % 2
        if turn == 0:
            turn = 2
        





if __name__ == "__main__":
    main()