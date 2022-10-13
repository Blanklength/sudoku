import random
from threading import Timer
import numpy as np
import numpy
import time
from random import shuffle
import pygame

start_time = time.time()


class SBoard(object):
    DIFFICULTIES = {
        1: 15,
        2: 20,
        3: 30,
    }

    EMPTY_LIST = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])

    def __init__(self, difficulty: int):
        self.solved_board = self.__generate_solved_board()
        self.__solved_board_copy = self.solved_board.copy()
        self.level_board = self.__generate_level_board(self.__solved_board_copy, difficulty_level=difficulty)

    def __generate_solved_board(self):
        standard_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        np.random.shuffle(standard_list)
        grid = np.array([
            standard_list,
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
        np.random.shuffle(standard_list)
        num_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counter_pool = 0
        counter_row = 1
        stuck_counter = 0
        counter_col = 0
        shuffle(num_pool)
        while True:
            if counter_row == 9:
                return grid
            grid[counter_row][counter_col] = num_pool[counter_pool]
            if self.are_columns_valid(grid=grid):
                if self.are_blocks_valid(grid=grid):
                    num_pool.pop(counter_pool)
            if self.are_columns_valid(grid=grid) and not self.are_blocks_valid(grid=grid) or not self.are_columns_valid(
                    grid=grid):
                valid = True
                if not self.are_columns_valid(grid=grid):
                    valid = False
                if not self.are_blocks_valid(grid=grid):
                    valid = False
                while not valid:
                    stuck_counter += 1
                    if stuck_counter == 100:
                        return self.__generate_solved_board()
                    backtrack = False
                    counter_pool += 1
                    try:
                        grid[counter_row][counter_col] = num_pool[counter_pool]
                    except IndexError:
                        backtrack_coord = (counter_row, counter_col)
                        backtrack_valid = False
                        grid[counter_row][counter_col] = 0
                        while not backtrack_valid:
                            counter_col -= 1
                            if counter_col == -10:
                                return self.__generate_solved_board()
                            grid[backtrack_coord[0], backtrack_coord[1]] = grid[counter_row][counter_col]
                            if self.are_columns_valid(grid=grid) and self.are_blocks_valid(grid=grid):
                                until_zero_cord = counter_col
                                counter_col = backtrack_coord[1]
                                while until_zero_cord <= counter_col:
                                    if counter_col != backtrack_coord[1]:
                                        num_pool.append(grid[counter_row][counter_col])
                                    grid[counter_row][counter_col] = 0
                                    counter_col -= 1
                                    backtrack_valid = True
                                counter_pool = 0
                        backtrack = True
                        counter_col += 1
                        shuffle(num_pool)
                    if self.are_columns_valid(grid=grid) and self.are_blocks_valid(grid=grid) and not backtrack:
                        num_pool.pop(counter_pool)
                        valid = True
                counter_pool = 0
            counter_col += 1
            if counter_col == 9:
                counter_col = 0
                counter_row += 1
                num_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                shuffle(num_pool)

    @staticmethod
    def __generate_level_board(grid: numpy.ndarray, difficulty_level: int):
        delete_amount = SBoard.DIFFICULTIES[difficulty_level]
        for i in range(delete_amount):
            grid[random.randint(0, 8)][random.randint(0, 8)] = 0
        return grid

    @staticmethod
    def __find_missing_num(col) -> int:
        missing_num = None
        required_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        col_set = {col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8]}
        for num in required_set.difference(col_set):
            missing_num = num
        return missing_num

    @staticmethod
    def show_grid(grid):
        for row in grid:
            print(row)

    @staticmethod
    def are_columns_valid(grid: numpy.ndarray) -> bool:
        for col_num in range(9):
            column = grid.T[col_num]
            unique, counts = np.unique(column, return_counts=True)
            search_dict = dict(zip(unique, counts))
            search_dict[0] = 1
            for value in search_dict.values():
                if value != 1:
                    return False
        return True

    @staticmethod
    def are_blocks_valid(grid: numpy.ndarray) -> bool:
        '''
        :param grid:
        progress of 3*3 rows
        :return:
        '''
        for block_num_y in range(0, 9, 3):
            for block_num_x in range(0, 9, 3):
                block = grid[block_num_y:block_num_y + 3, block_num_x:block_num_x + 3]
                unique, counts = np.unique(block, return_counts=True)
                search_dict = dict(zip(unique, counts))
                search_dict[0] = 1
                for value in search_dict.values():
                    if value != 1:
                        return False
        return True

    def __clean_grid(self):
        pass

    def __str__(self):
        result = str(self.solved_board)
        result = result[:0] + " " + result[0 + 1:]
        return result

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    b1 = SBoard(difficulty=3)
    print(b1.solved_board)
    print("--- %s seconds ---" % (time.time() - start_time))
