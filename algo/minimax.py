import numpy as np
import env
import copy


def chk_util(play):

    winning_config = np.array([[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]])

    for i in winning_config:
        chk_int = len(np.intersect1d(play,i))
        if chk_int == 3:
            play_win = 1
            break
        else:
            play_win = 0
    return play_win


def chk_winner(pos):
    
    play1 = [t for t,v in pos.items() if v==1]
    play2 = [t for t,v in pos.items() if v==2]

    win_sit1 = chk_util(play1)
    win_sit2 = chk_util(play2)


    winner = 0
    if win_sit1 == 1:
        winner = 1
    elif win_sit2 == 1:
        winner = 2


    return winner

def chk_open_set(curr_pos1):

    filled_spaces = np.union1d([t for t,v in curr_pos1.items() if v==1], [t for t,v in curr_pos1.items() if v==2])
    full_list = [1,2,3,4,5,6,7,8,9]
    open_set1 = list(set(full_list) - set(filled_spaces))

    return open_set1

def minmax(curr_pos, player):

    #Assume the computer is maximizing utility
    curr_open_set = chk_open_set(curr_pos)

    best_state = -1

    if player == 1:
        best_score = -10
    elif player == 2:
        best_score = 10

    for ele in curr_open_set:
        print(curr_open_set)
        curr_pos[ele] = player
        #check if it's the last element
        open_set = chk_open_set(curr_pos)
        if len(open_set) == 0:
            winner = chk_winner(curr_pos)
            if winner == 1:
                score = 1
            elif winner == 2:
                score = -1
            elif winner == 0:
                score = 0
        else:
            winner = chk_winner(curr_pos)
            if winner == 1 or winner == 2:
                break
            player = (player + 1) % 2
            if player == 0:
                player = 2
            score, state = minmax(curr_pos, player)

        curr_pos[ele] = 0

        if player == 1:
            if score > best_score:
                best_score = score
                best_state = ele
        elif player == 2:
            if score < best_score:
                best_score = score
                best_state = ele

    return best_score, best_state

        

