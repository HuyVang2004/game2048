
from mo_hinh import model, ai
from display import menu, play
import pygame

pygame.init()


if __name__ == '__main__':
    WIDTH = 420
    LENGTH = 600

    window = pygame.display.set_mode((WIDTH, LENGTH), pygame.RESIZABLE)

    window.fill((255, 255, 255))
    pygame.display.set_caption("2048")
    surface = pygame.Surface((420, 420))
    surface.fill((175, 175, 175))

    # set logo
    image = pygame.image.load("D:\\projects\\game2048\\images\\2048logo.png")
    pygame.display.set_icon(image)
    clock = pygame.time.Clock()
    fps = 60

    state = model.init()
    score = 0
    a = menu.draw_menu(window)

    if a == 2:
        play.draw_player(window, state)
    elif a == 3:
        window = pygame.display.set_mode((WIDTH * 2 + 50, LENGTH), pygame.RESIZABLE)
        play.draw_2player(window, state)
    elif a == 1:
        play.draw_ai(window, state)

    pygame.quit()