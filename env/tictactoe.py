import numpy as np

######################
# gym environment for tic tac toe
#    1  |  2  |  3
#  ------------------
#    4  |  5  |  6
#  ------------------
#    7  |  8  |  9


class tictactoe:

    def __init__(self):
        self.pos = {}
        for i in range(1,10):
            self.pos[i] = 0

        self.used_pos = []
        self.chke_box = ''

    def chk_winner(self, player):
        winning_config = np.array([[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]])

        if player == 1:
            play = [t for t,v in self.pos.items() if v==1]
        elif player == 2:
            play = [t for t,v in self.pos.items() if v==2]

        for i in winning_config:
            chk_int = len(np.intersect1d(play,i))
            if chk_int == 3:
                play_win = 1
                break
            else:
                play_win = 0

        return play_win


    def load_pos(self, player, position):

        chk_valid = [0 for i in self.used_pos if i == position]
        len_chk_valid = len(chk_valid)
        #check if position is avilable and valid
        if position < 1 or position > 9 or len_chk_valid == 1:
            valid = -1
            return valid 

        self.pos[position] = player

        self.used_pos.append(position)

        a = f"""
        {str(self.pos[1])}   |  {str(self.pos[2])}   |   {str(self.pos[3])}
        -----------------
        {str(self.pos[4])}   |  {str(self.pos[5])}   |   {str(self.pos[6])}
        -----------------
        {str(self.pos[7])}   |  {str(self.pos[8])}   |   {str(self.pos[9])}
        """

        print(a)
        valid = 1

        return valid
    
    def reset_game(self):

        self.__init__()



