import pygame
import random
#import leerjson
from Utils import image

screen_size = 1200 , 300

NEGRO=[0,0,0]

def cargar_mapa(pantalla,pos_x=0,pos_y=0):
  fondo = pygame.image.load('imagenes/mapa/mapa2.png')
  pantalla.blit(fondo,[pos_x,pos_y])


SPRITES = "imagenes/sprites/" 
Billimages = [ 'LanceJumpingR.gif' , 'LanceLayingDownR.png',  'LanceStandingR.png' , 'LanceWalkingR.gif']

class Bill():
  def __init__(self,image):
    self.health = 500
    self.pos_x = 50
    self.pos_y = 240
    self.image = image.ImageUtil(SPRITES+'LanceStandingR.png')
    self.frames = self.image.load()
    self.currentFrame = 0
    self.vel_x = 0
    self.vel_y = 0
    self.last_dir = 0
  def update(self,pantalla,action,left):
    self.image = image.ImageUtil(SPRITES + Billimages[action])
    self.frames = self.image.load()
    self.currentFrame = (self.currentFrame + 1) % len(self.frames)
    des_y = 0
    if action == 1:
      des_y = 20
      if self.last_dir == -1:
        self.frames = self.image.flip_and_rotate()
    if left:
      self.frames = self.image.flip_and_rotate()
      self.last_dir = -1
    if action  == 0:
      des_y = -50
      self.currentFrame = (self.currentFrame + 5) % len(self.frames)
    pantalla.blit(self.frames[self.currentFrame],[50,des_y+ 240])
  

def main():
  currentFrame = 0
  run = True
  pos_x = 0
  pygame.init()
  pantalla=pygame.display.set_mode(screen_size)
  pygame.display.set_caption('Contra')
  bill = Bill(image)
  action,left = 2,0
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT : run = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          action = 3
          left = 0
          bill.last_dir = 1
        if event.key == pygame.K_LEFT:
          action = 3
          left = 1
        if event.key == pygame.K_DOWN:
          action = 1
          left = 0
        if event.key == pygame.K_UP:
          action = 0
          left = 0 
      else:
          action = 2
    cargar_mapa(pantalla,pos_x,0)
    bill.update(pantalla,action,left)
    pygame.display.flip()
    pygame.time.delay(1)
  pygame.quit()

main()