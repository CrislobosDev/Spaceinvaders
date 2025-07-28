

from MiniGameEngine import GameWorld
from SpaceShip import SpaceShip
from Alien import Alien


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Actividad 01", bgpic="Recursos/Fondo.png")

        # agregamos a los actores
        SpaceShip(400, 540)
        Alien(100, 50)
        Alien(200, 50)
        Alien(300, 50)
        Alien(400, 50)
        Alien(500, 50)
        Alien(600, 50)
        Alien(700, 50)

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        # print(fps)
        if self.isPressed("Escape"):
            self.exitGame()

    def colision(self, spaceShip, alien):
        if spaceShip.getTipo() == "SpaceShip" and alien.getTipo() == "Alien":
            print("Colisión detectada entre la nave espacial y el alien.")
            # Aquí puedes agregar lógica adicional para manejar la colisión
    
game = Game()
game.gameLoop(60)
