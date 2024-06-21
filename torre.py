from piezas import Pieza

class Torre(Pieza):
    def __init__(self,nombre,color,movimiento_Horizontal_y_Vertical,mata_en_Horizontal_Vertical):
        super().__init__(nombre,color)
        self.movimiento_Horizontal_y_Vertical = movimiento_Horizontal_y_Vertical
        self.mata_en_Horizontal_y_Vertical = mata_en_Horizontal_Vertical