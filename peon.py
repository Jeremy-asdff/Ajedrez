from piezas import Pieza


class Peon(Pieza):
    def __init__(self,nombre,color,movimiento_hacia_adelante,mata_solamente_diagonal):
        super().__init__(nombre,color)
        self.movimiento_hacia_adelante = movimiento_hacia_adelante
        self.mata_solamente_diagonal = mata_solamente_diagonal



