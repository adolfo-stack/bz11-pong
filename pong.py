import pygame, sys

"""
- algo de herencia:

- color, ancho , alto.
- hay cosas fijas como el color y el tamaño.

- método moverse: solo hacia arriba y hacia abajo.
- método de chocar: límite para no salirse de la pantalla.

- método para interectuar con la pelota??

"""

class Paleta(pygame.Rect): # Paleta hereda de pygame.Rect, ya que esta definido, color, tamaño, esta ya creado en pygame!!!!
        pass


class Pelota():
    pass

    def __init__(self, pantalla, color, centro, radio):
        self.pantalla = pantalla
        self.color = color
        self.centro = centro
        self.radio = radio
      
class Pong:

    _ANCHO = 1000
    _ALTO = 800
    _MARGEN_LATERAL = 30

    _ANCHO_PALETA = 10
    _ALTO_PALETA = 60

    _RADIO_PELOTA = 10




    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.jugador1 = Paleta(self._MARGEN_LATERAL, (self._ALTO-self._ALTO_PALETA)/2, self._ANCHO_PALETA, self._ALTO_PALETA)
        self.jugador2 = Paleta(self._ANCHO-self._MARGEN_LATERAL-self._ANCHO_PALETA, (self._ALTO-self._ALTO_PALETA)/2, self._ANCHO_PALETA, self._ALTO_PALETA)

        self.pelota = Pelota(self.pantalla, (255, 255, 255), (200, 200), self._RADIO_PELOTA)

    
        pygame.draw.line(self.pantalla, (255, 255, 255), (500, 0), (500, 800), width=6) # SE DIBUJA LA RED, NO ES DISCONTINUA, DEBE SER CON UN BUCLE.

    """pygame.draw.line(self.pantalla, (255, 255, 255), (500, 0), (500, 100), width=6)
    pygame.draw.line(self.pantalla, (255, 255, 255), (500, 110), (500, 200), width=6)
    pygame.draw.line(self.pantalla, (255, 255, 255), (500, 210), (500, 300), width=6)
    pygame.draw.line(self.pantalla, (255, 255, 255), (500, 310), (500, 400), width=6)
    pygame.draw.line(self.pantalla, (255, 255, 255), (500, 410), (500, 500), width=6)
    """  
            

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        while True:
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador1 )
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador2 )
            pygame.draw.circle(self.pantalla, (255, 255, 255), (100, 100), self._RADIO_PELOTA)
            
            pygame.display.flip() # Siempre deberá haber un flip para mostrar lo dibujado o lo que ha cambiado en la pantalla.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        

if __name__=="__main__":
    juego = Pong()
    juego.bucle_principal()