import sys
import pygame

# Dev-log 4:


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
        return([tmp1,tmp2])
    def stop(self,x,y):
        if x is not None and x != 0:
            self.xvel = 0
        if y is not None and y != 0:
            self.yvel = 0
    def get_pos(self):
        return([self.x,self.y])

def main():
    # setup pygame
    screen = setup(1000, 300, "C:\\Users\\Aditya\\PycharmProjects\\Game client\\Textures\\Icon.png", "Game client")
    texture_path = "C:\\Users\\Aditya\\PycharmProjects\\Game client\\Textures\\Generate.png"
    textures = unwrap_sprites(texture_path, 2, 1, 8, 8, (255, 255, 255))
    #drawing = [[1, 0, 0, 0, 2], [3, 5, 5, 5, 4], [3, 5, 5, 5, 4], [7, 6, 8, 6, 9]]
    mapx = 64
    mapy = mapx
    tmpx = 0
    tmpy = 0
    collision_map = generate_map(mapx, mapy)
    # load and set the logo
    # logo = pygame.image.load("7u56.PNG")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Code snippet 4")
    screen = pygame.display.set_mode((1000, 700))
    px = mapx*8/2
    py = mapy*8/2
    player = Pawn(0,0,2,0,0,0.95,20,20)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill((0,0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.movey(0.2)
            tmpy = player.get_next_pos(0,0.2)
        elif keys[pygame.K_DOWN]:
            player.movey(-0.2)
            tmpy = player.get_next_pos(0,-0.2)
        if keys[pygame.K_LEFT]:
            player.movex(0.2)
            tmpx = player.get_next_pos(0.2,0)
        elif keys[pygame.K_RIGHT]:
            player.movex(-0.2)
            tmpx = player.get_next_pos(-0.2,0)
        player.movex(0)
        player.movey(0)
        px = player.get_pos()[0]
        py = player.get_pos()[1]
        for i in range(len(collision_map)):
            for q in range(len(collision_map[0])):
                screen.blit(textures[collision_map[i][q]], (q * 8+px, i * 8+py))
        pygame.draw.rect(screen,(255,255,255),(497,247,6,6))
        print([tmpx,tmpy])
        pygame.draw.rect(screen,(255,255,0),(497-tmpx,247-tmpy,6,6))
        pygame.display.update()


if __name__ == "__main__":
    main()
