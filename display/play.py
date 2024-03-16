import copy

import pygame

from display import menu
from mo_hinh import model, ai

pygame.init()

WIDTH = 420
LENGTH = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
colors = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (142, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (237, 193, 33)}


def draw_toolbar(screen, pos_x, pos_y):
    surface = pygame.Surface((WIDTH,80))
    surface.fill((255,255,255))
    draw_button(surface,(255, 172, 108), 20, 0, 70, 50, "HOME")
    draw_button(surface,(255, 172, 108), 110, 0, 70, 50, "PAUSE")
    draw_button(surface,(255, 172, 108), 200, 0, 70, 50, "RESTART")

    if LENGTH - 80 <= pos_y <= LENGTH - 30:
        if 20 <= pos_x <= 90:
            draw_button(surface, (224, 224, 224), 20, 0, 70, 50, "HOME")
        if 110 <= pos_x <= 180:
            draw_button(surface, (224, 224, 224), 110, 0, 70, 50, "PAUSE")
        if 200 <= pos_x <= 270:
            draw_button(surface, (224, 224, 224), 200, 0, 70, 50, "RESTART")
    screen.blit(surface, (0, LENGTH - 80))

def draw_text(screen, board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            font = pygame.font.SysFont(None, 60 - 5 * len(str(value)))
            if value > 0:
                document = font.render("{}".format(value), True, (119, 110, 101))
                center = document.get_rect(center=(100 * j + 60, 100 * i + 60))
                screen.blit(document, center)


def draw_block(screen, board):
    for i in range(4):
        for j in range(4):
            value = board[j][i]
            rect = pygame.rect.Rect(100 * i + 20, 100 * j + 20, 80, 80)
            if value < 4098:
                pygame.draw.rect(screen, colors[value], rect, 0, 5)
            else:
                pygame.draw.rect(screen, (0, 0, 0), rect, 0, 5)
            if value > 0:
                pygame.draw.rect(screen, (0, 0, 0), rect, 1, 5)


def draw_button(screen, color, x, y, width, height, str):
    font = pygame.font.SysFont(None, 24)
    text = font.render(str, True, (255, 255, 255))
    pygame.draw.rect(screen, color, (x, y, width, height), 0, 10)
    shape = text.get_rect()
    screen.blit(text, (x + width / 2 - shape.width / 2, y + height / 2 - shape.height / 2))


def draw_score(screen, sc):
    font = pygame.font.SysFont(None, 30)
    text = font.render("SCORE: {}".format(sc), True, (119, 110, 101))
    screen.blit(text, (10, 450))


def draw_player(screen, board):
    run = True
    score = 0
    surface = pygame.Surface((420, 420))
    surface.fill((175, 175, 175))
    home = False
    restart = False
    while run:

        screen.fill((255, 255, 255))
        screen.blit(surface, (0, 0))

        draw_score(screen, score)
        draw_block(screen, board)
        draw_text(screen, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_UP:
                    board, moved, score = model.move(board, score, "up")
                elif event.key == pygame.K_DOWN:
                    board, moved, score = model.move(board, score, "down")
                elif event.key == pygame.K_LEFT:
                    board, moved, score = model.move(board, score, "left")
                elif event.key == pygame.K_RIGHT:
                    board, moved, score = model.move(board, score, "right")
                model.random_value(board, moved)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                if LENGTH - 80 <= pos_y <= LENGTH - 30:
                    if 20 <= pos_x <= 90:
                        home = True
                        run = False
                    if 110 <= pos_x <= 180:
                        pass
                    if 200 <= pos_x <= 270:
                        restart = True
                        run = False
        pos_x, pos_y = pygame.mouse.get_pos()
        draw_toolbar(screen, pos_x, pos_y)
        pygame.display.flip()

    board = model.init()
    if home:
        a = menu.draw_menu(screen)

        if a == 2:
            draw_player(screen, board)
        elif a == 3:
            window = pygame.display.set_mode((WIDTH * 2 + 50, LENGTH), pygame.RESIZABLE)
            draw_2player(window, board)
        elif a == 1:
            draw_ai(screen, board)
    if restart:
        draw_player(screen, board)


def draw_2player(screen, board):
    surface1 = pygame.surface.Surface((WIDTH,LENGTH))
    surface2 = pygame.surface.Surface((WIDTH, LENGTH))
    board1 = copy.deepcopy(board)
    board2 = copy.deepcopy(board)
    run = True
    score1 = 0
    score2 = 0

    surface = pygame.Surface((420, 420))
    surface.fill((175, 175, 175))
    home = False
    restart = False
    while run:
        screen.fill(WHITE)
        surface1.fill(WHITE)
        surface2.fill(WHITE)
        surface1.blit(surface, (0, 0))
        surface2.blit(surface, (0, 0))

        draw_score(surface1, score1)
        draw_score(surface2, score2)

        draw_block(surface1, board1)
        draw_block(surface2, board2)

        draw_text(surface1, board1)
        draw_text(surface2, board2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                moved2 = False
                moved1 = False
                if event.key == pygame.K_UP:
                    board2,moved2, score2 = model.move(board2, score2, "up")
                elif event.key == pygame.K_DOWN:
                    board2, moved2, score2 = model.move(board2, score2, "down")
                elif event.key == pygame.K_LEFT:
                    board2, moved2, score2 = model.move(board2, score2, "left")
                elif event.key == pygame.K_RIGHT:
                    board2, moved2, score2 = model.move(board2, score2, "right")
                elif event.key == pygame.K_a:
                    board1, moved1, score1 = model.move(board1, score1, "left")
                elif event.key == pygame.K_d:
                    board1, moved1, score1 = model.move(board1, score1, "right")
                elif event.key == pygame.K_w:
                    board1, moved1, score1 = model.move(board1, score1, "up")
                elif event.key == pygame.K_s:
                    board1, moved1, score1 = model.move(board1, score1, "down")

                model.random_value(board2, moved2)
                model.random_value(board1, moved1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                if LENGTH - 80 <= pos_y <= LENGTH - 30:
                    if 20 <= pos_x <= 90:
                        home = True
                        run = False
                    if 110 <= pos_x <= 180:
                        pass
                    if 200 <= pos_x <= 270:
                        restart = True
                        run = False

        screen.blit(surface1, (0,0))
        screen.blit(surface2, (WIDTH + 50, 0))
        pos_x, pos_y = pygame.mouse.get_pos()
        draw_toolbar(screen, pos_x, pos_y)
        pygame.display.flip()

    board = model.init()
    if home:
        screen = pygame.display.set_mode((WIDTH,LENGTH))
        a = menu.draw_menu(screen)
        if a == 2:
            draw_player(screen, board)
        elif a == 3:
            window = pygame.display.set_mode((WIDTH * 2 + 50, LENGTH), pygame.RESIZABLE)
            draw_2player(window, board)
        elif a == 1:
            draw_ai(screen, board)
    if restart:
        window = pygame.display.set_mode((WIDTH * 2 + 50, LENGTH), pygame.RESIZABLE)
        draw_2player(window, board)


def draw_ai(screen, board):
    run = True
    surface = pygame.Surface((420, 420))
    surface.fill((175, 175, 175))
    score = 0
    home = False
    restart = False
    pause = False
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                if LENGTH - 80 <= pos_y <= LENGTH - 30:
                    if 20 <= pos_x <= 90:
                        home = True
                        run = False
                    if 110 <= pos_x <= 180:
                        pause = not pause
                    if 200 <= pos_x <= 270:
                        restart = True
                        run = False

        screen.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        draw_block(screen, board)
        draw_text(screen, board)
        draw_score(screen, score)
        if not model.end(board) and not pause:
            _, dir = ai.expectiminimax(board, 4, True)
            state, moved, score = model.move(board, score, dir)
            model.random_value(state, moved)

        pos_x, pos_y = pygame.mouse.get_pos()
        draw_toolbar(screen, pos_x, pos_y)
        pygame.display.flip()

    board = model.init()
    if home:
        a = menu.draw_menu(screen)

        if a == 2:
            draw_player(screen, board)
        elif a == 3:
            window = pygame.display.set_mode((WIDTH * 2 + 50, LENGTH), pygame.RESIZABLE)
            draw_2player(screen, board)
        elif a == 1:
            draw_ai(screen, board)
    if restart:
        draw_ai(screen, board)






