import sys
import pygame
import math
import random

# Dev-log 4:
# Designed a physics object that can move and accelerate
# Rendered a basic map
# Basis of the pawn
# Performance tester: makes additional pawns that sap system resources, to see how efficient the code is.
# Q to add a pawn, w to print number of pawns. My computer could run fine after 100 pawns, this number could be used to
# calculate maximum number of pawns rendered for a given computer?
# White square is the player, yellow is the predicted position next frame, green is the square chosen for collision checks


def unwrap_sprites(texture_path, x_rep, y_rep, x_size, y_size, colour_key):
    textures = []
    spritesheet = pygame.image.load(texture_path).convert()
    for i in range(0, y_rep):
        for q in range(0, x_rep):
            image = pygame.Surface((x_size, y_size)).convert()
            image.blit(spritesheet, (0, 0), (q * x_size, i * y_size, x_size, y_size))
            image.set_colorkey(colour_key)
            textures.append(image)
    return textures

def setup(x_size, y_size, log, caption):
    # setup pygame
    pygame.init()
    # load and set the logo
    if log is not None:
        pygame.display.set_icon(pygame.image.load(log))
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode((x_size, y_size)).convert()  # ,pygame.FULLSCREEN
    return (screen)

def blit(input,x,y,xwidth,ywidth,type):
    x = int(x)
    y = int(y)
    for q in range(ywidth):
        for i in range(xwidth):
            input[q+y][i+x] = type
    return input

def generate_map(x, y):# filled, maxX, maxY, minX, minY):
    map = [[]]
    tmp = []
    for i in range(0, x):
        tmp.append(0)
    map[0] = tmp
    for q in range(0, y - 1):
        tmp = []
        for i in range(0, x):
            tmp.append(0)
        map.append(tmp)
    map = blit(map,x/2-2,0,4,y,1)
    map = blit(map,0,y/2-2,x,4,1)
    return map

class Pawn:
    def __init__(self,x,y,type,xvel,yvel,braking,maxx,maxy):
        self.x = x
        self.y = y
        self.type = type
        self.xvel = xvel
        self.yvel = yvel
        self.braking = braking
        self.maxx = maxx
        self.maxy = maxy
    def movex(self,xforce):
        self.xvel = self.xvel*self.braking
        if self.xvel<self.maxx:
            self.xvel += xforce
        self.x += self.xvel
    def movey(self,yforce):
        self.yvel = self.yvel*self.braking
        if self.yvel<self.maxy:
            self.yvel += yforce
        self.y += self.yvel
    def get_next_pos(self,xforce,yforce):
        tmp1 = self.xvel*self.braking
        if tmp1<self.maxx:
            tmp1 += xforce
        tmp1 += float(self.xvel)
        tmp2 = self.yvel*self.braking
        if tmp2<self.maxy:
            tmp2 += yforce
        tmp2 += float(self.yvel)
        return[tmp1,tmp2]
    def stop(self,x,y):
        if x is not None and x != 0:
            self.xvel = 0
        if y is not None and y != 0:
            self.yvel = 0
    def get_pos(self):
        return([self.x,self.y])

def gridlock(gridx,gridy,gridsx,gridsy,x,y,mode):
    if mode:
        output = [0,0]
        output[0] = round(x / gridsx)
        output[1] = round(y / gridsy)
    return output

def main():
    # setup pygame
    screen = setup(1000, 300, "C:\\Users\\Delta\\PycharmProjects\\Game client\\Textures\\Icon.png", "Game client")
    texture_path = "C:\\Users\\Delta\\PycharmProjects\\Game client\\Textures\\Generate.png"
    textures = unwrap_sprites(texture_path, 2, 1, 8, 8, (255, 255, 255))
    #drawing = [[1, 0, 0, 0, 2], [3, 5, 5, 5, 4], [3, 5, 5, 5, 4], [7, 6, 8, 6, 9]]
    mapx = 64
    mapy = mapx
    tmp = [0,0]
    collision_map = generate_map(mapx, mapy)
    # load and set the logo
    # logo = pygame.image.load("7u56.PNG")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Code snippet 4")
    screen = pygame.display.set_mode((1000, 700))
    px = mapx*8/2
    py = mapy*8/2
    flags = 0
    pawns = [Pawn(0, 0, 2, 0, 0, 0.95, 20, 20)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill((0,0,0))
        keys = pygame.key.get_pressed()
        for w in range(len(pawns)):
            if keys[pygame.K_UP]:
                pawns[w].movey(0.2)
                tmp[1] = 0.2
            elif keys[pygame.K_DOWN]:
                pawns[w].movey(-0.2)
                tmp[1] = -0.2
            else:
                tmp[1] = 0
            if keys[pygame.K_LEFT]:
                pawns[w].movex(0.2)
                tmp[0] = 0.2
            elif keys[pygame.K_RIGHT]:
                pawns[w].movex(-0.2)
                tmp[0] = -0.2
            else:
                tmp[0] = 0
            if keys[pygame.K_q]:
                if flags == 0:
                    pawns.append(Pawn(random.randint(-20,20),random.randint(-20,20),2,0,0,0.95,20,20))
                flags = 1
            else:
                flags = 0
            if keys[pygame.K_w]:
                print(len(pawns))
            screen.fill((0,0,0))
            tmp = pawns[w].get_next_pos(tmp[0],tmp[1])
            pawns[w].movex(0)
            pawns[w].movey(0)
        for i in range(len(collision_map)):
            for q in range(len(collision_map[0])):
                screen.blit(textures[collision_map[int(i)][int(q)]], (int(round(q * 8+px)), int(round(i * 8+py))))
        for w in range(len(pawns)):
            px = pawns[w].get_pos()[0]
            py = pawns[w].get_pos()[1]
            tmp2 = gridlock(0, 0, 8, 8, math.ceil(px + tmp[0]), math.ceil(py + tmp[1]), 1)
            pygame.draw.rect(screen, (0, 255, 0),(int(round(497 - tmp2[0] * 8 + px)), int(round(247 - tmp2[1] * 8 + py)), 6, 6))
            pygame.draw.rect(screen,(255,255,255),(497,247,6,6))
            pygame.draw.rect(screen,(255,255,0),(int(round(497-tmp[0])),int(round(247-tmp[1])),6,6))
        pygame.display.update()


if __name__ == "__main__":
    main()