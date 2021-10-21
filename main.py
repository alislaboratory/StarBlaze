import pygame
import os
pygame.init()

BG_COLOR = (0,255,0) # green for when image is not correctly loaded
BG_SCROLL_VEL = 1


ORIGINAL_BG_POS = 0
WIDTH, HEIGHT = 900, 500
SHIP_SIZE = (100, 85)
SHIP_MOVE_VEL = 3

BG_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'space_back.jpeg')), (WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

SHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'spaceship.png')), SHIP_SIZE)
SHIP_ORIGINAL_POS = ((WIDTH/2) - SHIP_SIZE[0]/2 , (HEIGHT/3)*2)



FPS = 60

def window_handler(spaceship, BG):
    # WIN.fill(BG_COLOR)
    # WIN.blit(BG_IMAGE, (0, BG.y))
    WIN.blit(BG_IMAGE, (0, 250 - BG.height))
    WIN.blit(SHIP_IMG, (spaceship.x, spaceship.y))
    pygame.display.update()




def ship_movement_handler(spaceship, keys_pressed):
    if keys_pressed[pygame.K_w]: # up
        spaceship.y -= SHIP_MOVE_VEL
    if keys_pressed[pygame.K_s]: # down
        spaceship.y += SHIP_MOVE_VEL
    if keys_pressed[pygame.K_a]: # left
        spaceship.x -= SHIP_MOVE_VEL
    if keys_pressed[pygame.K_d]: # right
        spaceship.x += SHIP_MOVE_VEL


def background_scroll_handler(BG):

    BG.y += BG_SCROLL_VEL
    pygame.display.update()
    WIN.blit(BG_IMAGE, (0, BG.y))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    BG = pygame.Rect((0, 0), (ORIGINAL_BG_POS, 0))
    spaceship = pygame.Rect(SHIP_ORIGINAL_POS[0], SHIP_ORIGINAL_POS[1], SHIP_SIZE[0], SHIP_SIZE[1])

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        ship_movement_handler(spaceship, keys_pressed)
        BG.y += BG_SCROLL_VEL
        window_handler(spaceship, BG)




if __name__ == "__main__":
    main()


