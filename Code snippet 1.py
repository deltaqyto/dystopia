import sys
import pygame


# Dev-Log 1:
# Code simulates gravity and allows for basic jumping
# Basic collision detection and input detection implemented
# Cursor tracking implemented and visualised
# Colour spectrum mapping in progress
# Process quits with error, reason not investigated, error only appears when quitting.

def main():
    # set up environment variables
    player_y = 0.0
    gravity = -0.002
    counter = 0

    # Colour mapping
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    green = (0, 255, 0)

    up_force = 0
    ground = pygame.rect.Rect(0, 600, 1000, 150)
    body = pygame.rect.Rect(500, 0, 25, 100)
    is_touching_ground = False

    # setup pygame
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("7u56.PNG")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Game Client")
    screen = pygame.display.set_mode((1000, 700), pygame.FULLSCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        pygame.draw.rect(screen,green,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],100,50))
        pygame.draw.rect(screen, green, ground)
        body[1] = int(player_y)
        pygame.draw.rect(screen, blue, body)
        pygame.display.update()
        is_touching_ground = ground.colliderect(body)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if is_touching_ground:
                up_force = -0.55
                is_touching_ground = False
        if keys[pygame.K_q]:
            pygame.quit()
        if not is_touching_ground:
            up_force = up_force - gravity
            player_y = player_y + up_force


if __name__ == "__main__":
    main()
