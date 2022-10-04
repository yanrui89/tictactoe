
import env
import random
import algo
import copy


def main():
    #init environment
    ttt = env.tictactoe()
    turn = random.randint(1,2)

    for i in range(9):
        
        valid = -1

        if turn == 1:
            while valid == -1:                
                box = input(f'it is player {turn}s turn. Please input the box \n')
                print(box)
                valid = ttt.load_pos(turn,int(box))
                if valid == -1:
                    print('the value that you have placed is invalid. Please try again')
        elif turn == 2:
            '''
            ttt.pos[1] = 2
            ttt.pos[3] = 1
            ttt.pos[2] = 2
            ttt.pos[8] = 1
            ttt.pos[9] = 2
            '''
            score, state = algo.minmax(copy.deepcopy(ttt.pos), 2)
            valid = ttt.load_pos(turn, state)

        #check winner
        win = ttt.chk_winner(turn)

        if win == 1:
            print(f'congratulations player {turn} won')
            print('ending game')
            break

        turn = (turn + 1) % 2
        if turn == 0:
            turn = 2
        





if __name__ == "__main__":
    main()