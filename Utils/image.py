import pygame
from PIL import Image, ImageSequence

class ImageUtil:
    frames = []

    def __init__(self, filename):
        self.image = Image.open(filename)
        self.load()

    def load(self):
        frames = []
        if self.image.format == 'GIF':
            for frame in ImageSequence.Iterator(self.image):
                pygameImage = self.__pilImageToSurface(frame.convert('RGBA'))
                frames.append(pygameImage)
        else:
            frames.append(self.__pilImageToSurface(self.image.convert('RGBA')))
        self.frames = frames
        return frames

    def __pilImageToSurface(self, pilImage):
        mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
        return pygame.image.fromstring(data, size, mode).convert_alpha()

    def rotation(self, angle):
        rotated_images = []
        for frame in self.frames:
            image = pygame.transform.rotate(frame, angle)
            rotated_images.append(image)
        self.frames = rotated_images
        return rotated_images

    def flip(self):
        flip_images = []
        for frame in self.frames:
            image = pygame.transform.flip(frame, False, True)
            flip_images.append(image)
        self.frames = flip_images 
        return flip_images

    def flip_and_rotate(self):
        self.flip()
        return self.rotation(180)

 

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