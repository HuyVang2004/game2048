import pygame

pygame.init()
WIDTH = 420
LENGTH = 600


def draw_button(screen, x, y, width, height, color):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect, 0, 5)


def draw_menu(window):
    menu = pygame.Surface((WIDTH, LENGTH))
    f = pygame.font.SysFont(None, 27)
    run = True
    a = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 120 <= x <= 300:
                    if 105 <= y <= 195:
                        return 1
                    elif 240 <= y <= 330:
                        return 2
                    elif 375 <= y <= 465:
                        return 3

        menu.fill((255, 255, 255))
        draw_button(menu, 120, 105, 180, 90, (255, 172, 108))
        text = f.render("AI", True, (255, 255, 255))
        menu.blit(text, (200, 140))

        draw_button(menu, 120, 240, 180, 90, (255, 172, 108))
        text = f.render("PLAYER", True, (255, 255, 255))
        menu.blit(text, (170, 275))

        draw_button(menu, 120, 375, 180, 90, (255, 172, 108))
        text = f.render("PLAYER & PLAYER", True, (255, 255, 255))
        menu.blit(text, (130, 410))

        pos_x, pos_y = pygame.mouse.get_pos()
        if 120 <= pos_x <= 300:
            if 105 <= pos_y <= 195:
                draw_button(menu, 120, 105, 180, 90, (224, 224, 224))
            elif 240 <= pos_y <= 330:
                draw_button(menu, 120, 240, 180, 90, (224, 224, 224))
            elif 375 <= pos_y <= 465:
                draw_button(menu, 120, 375, 180, 90, (224, 224, 224))

        window.blit(menu, (0, 0))
        pygame.display.flip()

    return a