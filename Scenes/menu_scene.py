import pygame


class MenuScene(object):
    def __init__(self, screen: pygame.display, state: int, difficulty_state: int):
        self.screen = screen
        self.screen.fill((255, 255, 255))
        self.state = state
        self.difficulty = difficulty_state
        self.start_scene()

    def start_scene(self):
        self.draw_title()
        self.draw_options()
        self.draw_difficulty()
        self.select()

    def draw_options(self):
        font = pygame.font.SysFont(None, 40)

        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(120, 150, 400, 50), 2)
        img = font.render('Start Game', True, (0, 0, 0))
        self.screen.blit(img, (250, 160))

        imp = pygame.image.load(
            'C://Users//Erzurum25//PycharmProjects//2023 Erstes Halbjahr//Informatik//sudoku//icons//sudoku_icon.jpg').convert()
        imp = pygame.transform.scale(imp, (40, 40))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(120, 220, 400, 50), 2)
        self.screen.blit(imp, (180, 155))
        imp = pygame.image.load('C://Users//Erzurum25//PycharmProjects//2023 Erstes Halbjahr//Informatik//sudoku//icons//index.png').convert()
        imp = pygame.transform.scale(imp, (40, 40))
        img = font.render('Difficulty', True, (0, 0, 0))
        self.screen.blit(imp, (180, 225))
        self.screen.blit(img, (250, 230))

        imp = pygame.image.load(
            'C://Users//Erzurum25//PycharmProjects//2023 Erstes Halbjahr//Informatik//sudoku//icons//exit.png').convert()
        imp = pygame.transform.scale(imp, (40, 40))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(120, 290, 400, 50), 2)
        img = font.render('Exit', True, (0, 0, 0))
        self.screen.blit(img, (250, 300))
        self.screen.blit(imp, (180, 295))


    def draw_title(self):
        font = pygame.font.SysFont(None, 100)
        img = font.render('Sudoku', True, (255, 0, 0))
        self.screen.blit(img, (205, 20))

    def draw_difficulty(self):
        font = pygame.font.SysFont(None, 24)
        img = font.render("Current Difficulty: {}".format(self.difficulty), True, (255, 0, 0))
        self.screen.blit(img, (0, 400))




    def select(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 121 < pygame.mouse.get_pos()[0] < 515 and 148 < pygame.mouse.get_pos()[1] < 194:
                    self.state = 1
                    print("Hello")
            if event.type == pygame.QUIT:
                quit()


