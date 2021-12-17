import pygame
from PIL import Image, ImageSequence

class ImageUtil:
    gframes = []

    def __init__(self, filename):
        self.image = Image.open(filename)
        self.loadGIF()

    def loadGIF(self):
        frames = []
        for frame in ImageSequence.Iterator(self.image):
            pygameImage = self.__pilImageToSurface(frame.convert('RGBA'))
            frames.append(pygameImage)
        self.gframes = frames
        return frames

    def __pilImageToSurface(self, pilImage):
        mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
        return pygame.image.fromstring(data, size, mode).convert_alpha()

    def rotation(self, angle):
        rotated_images = []
        for frame in self.gframes:
            image = pygame.transform.rotate(frame, angle)
            rotated_images.append(image)
        self.gframes = rotated_images
        return rotated_images

    def flip(self):
        flip_images = []
        for frame in self.gframes:
            image = pygame.transform.flip(frame, False, True)
            flip_images.append(image)
        self.gframes = flip_images 
        return flip_images

    def flip_and_rotate(self):
        self.flip()
        self.rotation(180)
        return self.gframes

 

### EXAMPLE ###
'''
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


image = ImageUtil("my_gif.gif")
gifFrameList = image.flip_and_rotate()
currentFrame = 0

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill([0, 0, 0])
    rect = gifFrameList[currentFrame].get_rect(center = (250, 250))
    window.blit(gifFrameList[currentFrame], rect)
    currentFrame = (currentFrame + 1) % len(gifFrameList)
    
    pygame.display.flip()
'''
