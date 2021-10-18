import pygame
import os
pygame.init()

BG_COLOR = (0,255,0) # green for when image is not correctly loaded
BG_SCROLL_VEL = 1

ORIGINAL_BG_POS = 0
WIDTH, HEIGHT = 900, 500
BG_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background_space.jpeg')), (WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BG = pygame.Rect((0, 0), (ORIGINAL_BG_POS, 0))

FPS = 60

def window_handler():
    # WIN.fill(BG_COLOR)
    pygame.display.update()

def background_scroll_handler(BG):

    BG.y -= BG_SCROLL_VEL
    WIN.blit(BG_IMAGE, (0, BG.y))
    if BG.y + BG.height < 500:
        WIN.blit(BG_IMAGE, (0, BG.y + BG.height))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # window_handler()
        background_scroll_handler(BG)


main()