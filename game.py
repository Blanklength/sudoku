import pygame
from SudokuBoard_better import SBoard
from Scenes.menu_scene import MenuScene
from Scenes.game_scene import GameScene

# initialisieren von pygame
pygame.init()

# Fenster öffnen
screen = pygame.display.set_mode((900, 480))

# Titel für Fensterkopf
pygame.display.set_caption("Sudoku")

# solange die Variable True ist, soll das Spiel laufen
is_game_activ = True
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
FPS_CLOCK = pygame.time.Clock()
game_state = 0
difficulty = 1
first_init = True

# Schleife Hauptprogramm
while is_game_activ:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_activ = False
    if game_state == 0:
        m1 = MenuScene(screen=screen, state=game_state, difficulty_state=difficulty)
        game_state = m1.state
    if game_state == 1:
        if first_init:
            b1 = SBoard(difficulty=difficulty)
            first_init = False
        screen.fill(WHITE)
        m2 = GameScene(screen=screen, state=game_state, board=b1)
        game_state = m2.state

    pygame.display.flip()
    pygame.display.update()
    FPS_CLOCK.tick(60)
