from piezas import Pieza

class Caballo(Pieza):
    
    def __init__(self,nombre,color,movimiento_en_L,mata_en_L):
        super().__init__(nombre,color)
        self.movimiento_en_L = movimiento_en_L
        self.mata_en_L = mata_en_L