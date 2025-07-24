from MiniGameEngine import GameObject # Importa la clase GameObject del módulo MiniGameEngine


class Alien(GameObject): # Define la clase Alien que hereda de GameObject
    # inicializamos el Alien
    def __init__(self, x, y): # Constructor de la clase Alien, toma coordenadas x e y
        super().__init__(x, y, "Recursos/Alien.png", "Alien") # Llama al constructor de la clase padre (GameObject) para inicializar el alien con su posición, imagen y tipo "Alien"
        self.speed = 2 # Atributo para la velocidad horizontal del alien (2 unidades por frame)
        self.direction = 1 # Atributo para la dirección de movimiento (1: derecha, -1: izquierda)

    # movimiento del Alien
    def onUpdate(self, dt): # Método llamado en cada frame para actualizar el estado del alien, recibe el tiempo delta (dt)
        x = self.getX() # Obtiene la coordenada x actual del alien
        y = self.getY() # Obtiene la coordenada y actual del alien
        world_width = self.getWorldWidth() # Obtiene el ancho del mundo del juego
        alien_width = self.getWidth() # Obtiene el ancho del alien

        # Calcula la nueva posición x
        x += self.speed * self.direction # Mueve el alien horizontalmente sumando (o restando) la velocidad según la dirección

        # Cambia de dirección si llega a los bordes
        if x + alien_width / 2 > world_width: # Comprueba si el alien ha alcanzado o superado el borde derecho de la pantalla
            x = world_width - alien_width / 2 # Ajusta la posición del alien para que no se salga del borde derecho
            self.direction = -1 # Cambia la dirección a izquierda (-1)
        elif x - alien_width / 2 < 0: # Comprueba si el alien ha alcanzado o superado el borde izquierdo de la pantalla
            x = alien_width / 2 # Ajusta la posición del alien para que no se salga del borde izquierdo
            self.direction = 1 # Cambia la dirección a derecha (1)

        self.setPosition(x, y) # Actualiza la posición del alien en el juego

    # manejamos las colisiones
    def onCollision(self, dt, gobj): # Método llamado cuando el alien colisiona con otro objeto (gobj), recibe el tiempo delta (dt) y el objeto con el que colisiona
        if gobj.getTipo() == "Bullet": # Comprueba si el objeto con el que colisionó es de tipo "Bullet"
            self.destroy() # Si colisiona con una bala, destruye el alien
            print("Alien:me dieron") # Imprime un mensaje en la consola