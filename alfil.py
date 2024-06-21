from piezas import Pieza

class Alfil(Pieza):
    def __init__(self,nombre,color,movimiento_en_diagonal,mata_en_diagonal):
        super().__init__(nombre,color)
        self.movimiento_en_diagonal = movimiento_en_diagonal
        self.mata_en_diagonal = mata_en_diagonal
        