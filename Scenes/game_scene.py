import pygame
from SudokuBoard_better import SBoard


class GameScene(object):
    def __init__(self, screen: pygame.display, state: int, board: SBoard):
        self.screen = screen
        self.state = state
        self.board = board
        self.start_scene()

    def start_scene(self):
        self.draw_fields()
        self.draw_grid()

    def draw_grid(self):
        pass


    def draw_fields(self):
        y = -20
        for row in range(9):
            y += 50
            x = 30
            for col in range(9):
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, 40, 40))
                font = pygame.font.SysFont(None, 40)
                img = font.render(str(self.board.solved_board[row][col]), True, (255, 255, 255))
                if self.board.level_board[row][col] != 0:
                    self.screen.blit(img, (x+13, y+10))

                x += 65
