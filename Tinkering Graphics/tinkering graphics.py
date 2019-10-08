import pygame, sys
from pygame.locals import *

def reduce_red(pic):
    pygame.Surface.unlock(pic)
    for x in range (pic.get_size()[0]):
        for y in range(pic.get_size()[1]):
            colour = list(pic.get_at((x,y)))
            recolour = colour[0]
            colour[0] = colour[2]
            colour[2] = recolour
            colour[2] = colour[2] * 0.5
            pic.set_at((x,y), colour)

class Pic:
    def __init__(self):
        self.pic = pygame.image.load(picture_addr)
        self.pos = (1, 1)

class Block:

    def __init__(self):
        self.speed = 2
        self.box_x = 300
        self.box_y = 200
        self.box_dir = 3
        self.box_colour = (100, 0, 255)
        self.size = 30

    def draw(self, surface):
        pygame.draw.rect(surface, self.box_colour, (self.box_x, self.box_y, self.size, self.size))


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Moving Block.")

    WHITE = (250, 250, 250)
    GREEN = (0, 250, 0)
    BLACK = (0, 0, 0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    clock = pygame.time.Clock()

    box = Block()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return
        screen.fill(BLACK)
        box.draw(screen)
        if pygame.key.get_pressed()[pygame.K_d] and (box.box_x + box.size) < screen.get_size()[0]:
            box.box_x += box.speed
        if pygame.key.get_pressed()[pygame.K_a] and box.box_x > 0:
            box.box_x -= box.speed
        if pygame.key.get_pressed()[pygame.K_w] and box.box_y > 0:
            box.box_y -= box.speed
        if pygame.key.get_pressed()[pygame.K_s] and (box.box_y + box.size) < screen.get_size()[1]:
            box.box_y += box.speed

        """
        red_ball_pos = (1, 1)
        reduce_red(red_ball)
        screen.blit(background, (0, 0))
        screen.blit(red_ball, (red_ball_pos))"""
        pygame.display.flip()

main()