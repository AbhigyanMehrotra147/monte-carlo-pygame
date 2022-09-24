
import sys
import pygame
file = open( "temp.txt" , 'r')

string = ""
for line in file:
    string += line

lis = list(string.split( " " ))

print(lis[1])

import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Text Tryout")

font = pygame.font.Font("freesansbold.ttf", 34)
text = font.render("hello world",True, (10,10,23),(255,255,255))
# print(pygame.font.get_fonts())

text_rect = text.get_rect()
text_rect.center = (200,200)

while True:

    screen.fill((255,255,255))
    screen.blit(source=text,dest=text_rect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update

