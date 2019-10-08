import pygame
from pygame.locals import *

def reduce_red(pic):
    pygame.Surface.unlock(pic)
    for x in range (pic.get_size()[0]):
        for y in range(pic.get_size()[1]):
            colour = list(pic.get_at((x,y)))
            print(colour)
            recolour = colour[0]
            colour[0] = colour[2]
            colour[2] = recolour
            colour[2] = colour[2] * 0.5
            pic.set_at((x,y), colour)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Green block moving all over the place.")

    WHITE = (250, 250, 250)
    GREEN = (0, 250, 0)
    BLACK = (0, 0, 0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    red_ball = pygame.image.load("red_ball.jpg")
    red_ball_pos = (1, 1)
    reduce_red(red_ball)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        if pygame.key.get_pressed()[pygame.K_d] and red_ball_pos[0] < screen.get_size()[0]:
            red_ball_pos = ((red_ball_pos[0] + 1), red_ball_pos[1])
        if pygame.key.get_pressed()[pygame.K_a] and red_ball_pos[0] > 0:
            red_ball_pos = ((red_ball_pos[0] - 1), red_ball_pos[1])
        if pygame.key.get_pressed()[pygame.K_w] and red_ball_pos[1] > 0:
            red_ball_pos = (red_ball_pos[0], (red_ball_pos[1] - 1))
        if pygame.key.get_pressed()[pygame.K_s] and red_ball_pos[1] < screen.get_size()[1]:
            red_ball_pos = (red_ball_pos[0], (red_ball_pos[1] + 1))

        screen.blit(background, (0, 0))
        screen.blit(red_ball, (red_ball_pos))
        pygame.display.flip()

main()