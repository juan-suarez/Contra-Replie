import pygame
import random

screen_size = 1200 , 300

NEGRO=[0,0,0]

def cargar_mapa(pantalla,pos_x=0,pos_y=0):
  fondo = pygame.image.load('imagenes/mapa/mapa2.png')
  player = pygame.image.load('imagenes/sprites/Bill.png')
  pantalla.blit(fondo,[pos_x,pos_y])
  pantalla.blit(player,[50,510])


def main():
  run = True
  pos_x = 0
  pygame.init()
  pantalla=pygame.display.set_mode(screen_size)
  pygame.display.set_caption('Contra')
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT : run = False
    cargar_mapa(pantalla,pos_x,0)
    pygame.display.flip()
    pos_x-=20
    pygame.time.delay(1)
  pygame.quit()

main()