from piezas import Pieza

class Rey(Pieza):
    def __init__(self,nombre,color,movimiento_en_horizontal_vertical_diagonal,mata_en_horizontal_vertical_diagonal):
        super().__init__(nombre,color)
        self.movimiento_en_horizontal_vertical_diagonal = movimiento_en_horizontal_vertical_diagonal
        self.mata_en_horizontal_vertical_diagonal = mata_en_horizontal_vertical_diagonal
        