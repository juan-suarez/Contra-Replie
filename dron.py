from Utils import image

SPRITES = "imagenes/sprites/" 

class Shoot:
    def __init__(self, bala, x, y):
        self.pos_x = x
        self.pos_y = y
        self.dir = 0
        self.image = image.ImageUtil(SPRITES + bala)
        self.frame = self.image.load()[0]
    def update(self, pantalla, dir):
        if dir == 0:
            self.pos_y += 1
        pantalla.blit(self.frame, [self.pos_x, self.pos_y])


class Dron:
    def __init__(self):
        self.health = 500
        self.pos_x = 200
        self.pos_y = 140
        self.frame = image.ImageUtil(SPRITES + 'FlyingCapsule.png').load()[0]
        self.bala = image.ImageUtil(SPRITES + 'Fire.gif').load()[0]
        self.last_dir = 0
        self.disparos = []

    def update(self, pantalla, billPositionX, billPositionY):
        if billPositionX != self.pos_x:
            if billPositionX < self.pos_x:
                self.pos_x -= 1
            else:
                self.pos_x += 1
        else:
            if len(self.disparos) == 0:
                shoot = Shoot('Fire.gif', self.pos_x, self.pos_y)
                shoot.update(pantalla, 0)
                self.disparos.append(shoot)
        for i in self.disparos:
            i.update(pantalla, 0)
        pantalla.blit(self.frame,[self.pos_x, self.pos_y])

