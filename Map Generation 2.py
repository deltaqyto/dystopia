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


def maze_from_here(grid, explored, x, y, type):
    moved = True
    moves = 0
    while moved:
        heading = [0,1,2,3]
        while len(heading):
            print(heading)
            move = random.randint(0,len(heading)-1)
            if heading[move] == 0:
                if x - 3 > 0:
                    grid[y][x] = type
                    grid[y][x - 1] = type
                    grid[y][x - 2] = type
                    move += 1
                else:
                    heading.pop(move)

            elif heading[move] == 1:
                if x + 4 < len(grid[0]):
                    grid[y][x] = type
                    grid[y][x + 1] = type
                    grid[y][x + 2] = type
                    move += 1
                else:
                    heading.pop(move)

            elif heading[move] == 2:
                if y - 3 > 0:
                    grid[y][x] = type
                    grid[y - 1][x] = type
                    grid[y - 2][x] = type
                    move += 1
                else:
                    heading.pop(move)
            else:
                if y + 4 < len(grid):
                    grid[y][x] = type
                    grid[y + 1][x] = type
                    grid[y + 2][x] = type
                    move += 1
                else:
                    heading.pop(move)

    for i in range(moves):
        maze_from_here(grid,explored,explored[-i][0],explored[-i][1],1)
    return [grid, explored]


def generate_map(x, y, settings):
    output_map = [[]]
    tmp = []
    explored = []
    type = settings[0]
    for i in range(0, x):
        tmp.append(0)
    output_map[0] = tmp
    for q in range(0, y - 1):
        tmp = []
        for i in range(0, x):
            tmp.append(0)
        output_map.append(tmp)
    tmp = maze_from_here(output_map,explored,0,0,type)
    return tmp[0]


def main():
    # setup pygame
    screen = setup(1000, 700, "C:\\Users\\Delta\\PycharmProjects\\Game Client\\Textures\\Icon.png", "Game client")
    texture_path = "C:\\Users\\Delta\\PycharmProjects\\Game Client\\Textures\\Generate.png"
    textures = unwrap_sprites(texture_path, 1, 2, 8, 8, (255, 255, 255))
    pygame.display.set_caption("Game Client")
    screen = pygame.display.set_mode((1000, 700))
    settings = [1]
    # settings = [0.05, 1, 1, 1, 1]
    game_map = generate_map(64, 64, settings)
    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            screen.blit(textures[game_map[y][x]], (x * 8, y * 8))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            game_map = generate_map(64, 64, settings)
            for y in range(len(game_map)):
                for x in range(len(game_map[y])):
                    screen.blit(textures[game_map[y][x]], (x * 8, y * 8))
            pygame.display.update()


if __name__ == "__main__":
    main()
