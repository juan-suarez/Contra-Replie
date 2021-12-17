import pygame
from PIL import Image, ImageSequence

class ImageUtil:
    def __init__(self, filename):
        self.filename = filename

    def loadGIF(self):
        pilImage = Image.open(self.filename)
        frames = []
        for frame in ImageSequence.Iterator(pilImage):
            pygameImage = self.__pilImageToSurface(frame.convert('RGBA'))
            frames.append(pygameImage)
        return frames

    def __pilImageToSurface(self, pilImage):
        mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
        return pygame.image.fromstring(data, size, mode).convert_alpha()
 

### EXAMPLE ###
'''
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


gifFrameList = ImageUtil("my_gif.gif").loadGIF()
currentFrame = 0

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect = gifFrameList[currentFrame].get_rect(center = (250, 250))
    window.blit(gifFrameList[currentFrame], rect)
    currentFrame = (currentFrame + 1) % len(gifFrameList)
    
    pygame.display.flip()
'''
