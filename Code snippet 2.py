import sys
import pygame

# Dev-log 2:
# Created inline setup function to neaten main()
# Created sprite unwrapper to allow for spritesheets
# rudimentary sprite drawing system using a matrix to store colours
# Currently draws a 40*40 px house with a door

def unwrap_sprites(texture_path,x_rep, y_rep, x_size, y_size,colour_key):
    textures = []
    spritesheet = pygame.image.load(texture_path).convert()
    for i in range(0, y_rep):
        for q in range(0, x_rep):
            image = pygame.Surface((x_size, y_size)).convert()
            image.blit(spritesheet, (0, 0), (q * x_size, i * y_size, x_size, y_size))
            image.set_colorkey(colour_key)
            textures.append(image)
    return(textures)

def setup(x_size, y_size, log, caption):
    # setup pygame
    pygame.init()
    # load and set the logo
    if log is not None:
        pygame.display.set_icon(pygame.image.load(log))
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode((x_size, y_size)).convert()  # ,pygame.FULLSCREEN
    return(screen)


def main():
   # setup pygame
   screen = setup(1000, 700, "C:\\Users\\delta\\PycharmProjects\\Game Client\\Textures\\Icon.png", "Game client")
   texture_path = "C:\\Users\\delta\\PycharmProjects\\Game Client\\Textures\\Walls.png"
   textures = unwrap_sprites(texture_path, 4, 4, 32, 32, (255, 255, 255))
   drawing = [[1, 10, 0, 10, 2], [3, 5, 5, 5, 4], [3, 5, 5, 5, 4], [7, 6, 8, 6, 9]]

   # load and set the logo
   # logo = pygame.image.load("7u56.PNG")
   # pygame.display.set_icon(logo)
   pygame.display.set_caption("Game Client")
   screen = pygame.display.set_mode((1000, 700))

   for i in range(len(drawing)):
       for q in range(len(drawing[0])):
           screen.blit(textures[drawing[i][q]], (q * 32+250, i * 32+250))
   pygame.display.update()

   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()


if __name__ == "__main__":
   main()

