from MiniGameEngine import GameObject

class Alien(GameObject):
    def __init__(self, x, y, movimiento_ancho=100):  # Puedes pasar opcionalmente el ancho de movimiento
        super().__init__(x, y, "Recursos/Alien.png", "Alien")
        self.speed = 1
        self.direction = 1

        # Definir el rango de movimiento horizontal limitado
        self.initial_x = x
        self.min_x = x - movimiento_ancho / 2
        self.max_x = x + movimiento_ancho / 2

    def onUpdate(self, dt):
        x = self.getX()
        y = self.getY()

        # Mover al alien
        x += self.speed * self.direction

        # Cambiar de dirección si llega a los límites definidos
        if x > self.max_x:
            x = self.max_x
            self.direction = -1
        elif x < self.min_x:
            x = self.min_x
            self.direction = 1

        self.setPosition(x, y)

    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Bullet":
            self.destroy()
            print("Alien: me dieron")
