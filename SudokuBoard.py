import random
from builtins import type

import numpy
import numpy as np
import time

start_time = time.time()


class SBoard(object):
    DIFFICULTIES = {
        1: 15,
        2: 20,
        3: 30,
    }

    def __init__(self):
        self.solved_board = self.__generate_solved_board()
        self.level_board = self.__generate_level_board(self.solved_board, 'easy')

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

        for num in range(8):
            # first extra row
            np.random.shuffle(standard_list)
            grid[num] = standard_list
            while not self.__check_rows_are_unordered(grid=grid):
                np.random.shuffle(standard_list)
                grid[num] = standard_list

        return grid


    def __generate_level_board(self, grid: numpy.ndarray, difficulty_level: str):
        return ''

    @staticmethod
    def show_grid(grid):
        for row in grid:
            print(row)

    @staticmethod
    def __check_rows_are_unordered(grid: numpy.ndarray):
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
    def __check_squares_are_unordered(grid: numpy.ndarray):
        '''

        :param grid:
        :param state:
        progress of 3*3 rows
        :return:
        '''

        # 3*3 block ranges

        first_block = grid[0:3, 0:3]
        num = np.where(first_block==5)
        print(first_block)
        print(num)

    def __str__(self):
        result = str(self.solved_board)
        result = result[:0] + " " + result[0+1:]
        return result


if __name__ == '__main__':
    b1 = SBoard()
    print(b1)
    print("--- %s seconds ---" % (time.time() - start_time))
