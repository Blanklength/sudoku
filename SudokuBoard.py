import random
import numpy as np
import numpy
import time


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
        num = 0
        while num <= 7:
            np.random.shuffle(standard_list)
            grid[num] = standard_list
            while not self.__are_columns_valid(grid=grid):
                np.random.shuffle(standard_list)
                grid[num] = standard_list
            if num == 2 or num == 5 or num == 8:
                if not self.__are_blocks_valid(grid):
                    grid[num] = SBoard.EMPTY_LIST
                    grid[num - 1] = SBoard.EMPTY_LIST
                    grid[num - 2] = SBoard.EMPTY_LIST
                    num -= 3
            num += 1
        for i in range(9):
            grid[8][i] = self.__find_missing_num(grid.T[i])
        return grid


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
    def __are_columns_valid(grid: numpy.ndarray) -> bool:
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
    def __are_blocks_valid(grid: numpy.ndarray) -> bool:
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
    print(b1.level_board)
    print("--- %s seconds ---" % (time.time() - start_time))
