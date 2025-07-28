import time
from MiniGameEngine import GameObject
from Bullet import Bullet


class SpaceShip(GameObject):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/SpaceShip.png", "SpaceShip")
        self.lastBullet = time.time()

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.isPressed("Left"):
            x = x - 4
            if x - w / 2 < 0:
                x = w / 2
        elif self.isPressed("Right"):
            x = x + 4
            if x > ww - w / 2:
                x = ww - w / 2
        self.setPosition(x, y)

        # movimiento vertical
        if self.isPressed("Up"): # movimiento hacia arriba al presionar "Up"
            y = y - 4 
            if y - w / 2 < 0:
                y = w / 2
        elif self.isPressed("Down"): # movimiento hacia abajo al presionar "Down"
            y = y + 4
            if y > ww - w / 2:
                y = ww - w / 2
        self.setPosition(x, y) # actualizamos la posición de la nave

        # disparamos una bala
        if self.isPressed("space"):
            if time.time() - self.lastBullet > 0.3:
                Bullet(x, y - 30)
                self.lastBullet = time.time()
