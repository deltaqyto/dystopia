import random
import sys

import pygame


# Dev log 3:
# Making a map that has rooms and corridors connecting them

def unwrap_sprites(texture_path, x_rep, y_rep, x_size, y_size, colour_key):
    textures = []
    spritesheet = pygame.image.load(texture_path).convert()
    for i in range(0, y_rep):
        for q in range(0, x_rep):
            image = pygame.Surface((x_size, y_size)).convert()
            image.blit(spritesheet, (0, 0), (q * x_size, i * y_size, x_size, y_size))
            image.set_colorkey(colour_key)
            textures.append(image)
    return (textures)


def setup(x_size, y_size, log, caption):
    # setup pygame
    pygame.init()
    # load and set the logo
    if log is not None:
        pygame.display.set_icon(pygame.image.load(log))
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode((x_size, y_size)).convert()  # ,pygame.FULLSCREEN
    return screen


def count(map, x, y, type):
    output = 0
    for q in range(y):
        for i in range(x):
            if map[q][i] == type:
                output += 1
    return output


def blit(input, x, y, xwidth, ywidth, type):
    for q in range(ywidth):
        for i in range(xwidth):
            input[q + y][i + x] = type
    return input

class Digger:
    def __init__ (self,x,y,heading,settings):
        self.x = x
        self.y = y
        self.heading = heading #1,-1,2,-2,   1/-1 is up down
        self.speed = settings[0]
        self.width = settings[1]
    def move(self):
        if heading == 1 or heading == -1:
            self.y += self.speed*heading
        else:
            self.x += self.speed*heading/2
    def getnextpos(self):
        if heading == 1 or heading == -1:
            tmpy += self.speed*heading
        else:
            tmpx += self.speed*heading/2
        return[tmpx,tmpy]
    def live(self):
        self.move()
    def get_pos(self):
        return([self.x,self.y])
def generate_map(x, y, settings):  # filled, maxX, maxY, minX, minY):
    map = [[]]
    tmp = []
    rects = []
    filled = settings[0]
    maxX = settings[1]
    maxY = settings[2]
    minX = settings[3]
    minY = settings[4]
    border = settings[5]
    for i in range(0, x):
        tmp.append(0)
    map[0] = tmp
    for q in range(0, y - 1):
        tmp = []
        for i in range(0, x):
            tmp.append(0)
        map.append(tmp)
    while count(map, x, y, 1) / count(map, x, y, 0) < filled:
        rectwx = random.randint(minX, maxX)
        rectwy = random.randint(minY, maxY)
        rectx = random.randint(border, x - rectwx - border)
        recty = random.randint(border, y - rectwy - border)
        map = blit(map, rectx, recty, rectwx, rectwy, 1)
    return map


def main():
    # setup pygame
    screen = setup(1000, 700, "C:\\Users\\delta\\PycharmProjects\\Game Client\\Textures\\Icon.png", "Game client")
    texture_path = "C:\\Users\\delta\\PycharmProjects\\Game Client\\Textures\\Generate.png"
    textures = unwrap_sprites(texture_path, 1, 2, 8, 8, (255, 255, 255))
    pygame.display.set_caption("Game Client")
    screen = pygame.display.set_mode((1000, 700))
    settings = [0.01, 5, 5, 3, 3, 5]
    # settings = [0.05, 1, 1, 1, 1]
    map = generate_map(64, 64, settings)
    for y in range(len(map)):
        for x in range(len(map[y])):
            screen.blit(textures[map[y][x]], (x * 8, y * 8))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            map = generate_map(64, 64, settings)

            for y in range(len(map)):
                for x in range(len(map[y])):
                    screen.blit(textures[map[y][x]], (x * 8, y * 8))
            pygame.display.update()


if __name__ == "__main__":
    main()
