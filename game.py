import random
import copy
import pickle
import os
import sys

if getattr(sys, "frozen", False):
    absolute_path = os.path.dirname(sys.executable)
elif __file__:
    absolute_path = os.path.dirname(__file__)
relative_path = "assets"

full_path = os.path.join(absolute_path, relative_path)


class Board():
    def __init__(self, timer):
        self.board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
        ]

        self.blank_pos = (3, 3)

        self.timer = timer
        self.best_time_path = os.path.join(full_path, "besttime")

    def return_curr_pos(self):
        for x, row in enumerate(self.board):
            for y, value in enumerate(row):
                if value == 0:
                    self.pos = [x, y]
        return self.pos


    def return_board(self):
        val_list = []
        for i in self.board:
            for j in i:
                val_list.append(j)

        return val_list

    def solved(self):
        self.timer.stop_timer()
        best_time = round(self.timer.return_value(), 3)
        database = open(self.best_time_path, "ab")
        with open(self.best_time_path, 'rb') as f:
            data = pickle.load(f)
            f.close()
        if best_time < data:
            open(self.best_time_path, "w").close()
            pickle.dump(best_time, database)
            database.close()

    def return_pos_list(self):
        pos_list = []
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                pos_list.append((i,j))
        return pos_list

    def scramble_board(self):
        moves = ['Up', 'Down', 'Left', 'Right']
        for i in range(301):
            move = random.choice(moves)
            self.move(move)
                

    def reset_board(self):
        self.board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
        ]

    def move(self, move):
        self.return_curr_pos()
        prev_pos = self.pos
        prev_no = self.board[prev_pos[0]][prev_pos[1]]
        current_pos = list(prev_pos)

        if move == "Left":
           current_pos[1] -= 1
        elif move == "Right":
           current_pos[1] += 1
        elif move == "Up":
           current_pos[0] -= 1
        elif move == "Down":
           current_pos[0] += 1       

        if 0 <= current_pos[0] < len(self.board) and 0 <= current_pos[1] < len(self.board[0]):
            current_no = self.board[current_pos[0]][current_pos[1]]

            self.board[prev_pos[0]][prev_pos[1]] = current_no
            self.board[current_pos[0]][current_pos[1]] = prev_no

        return prev_pos, current_pos
