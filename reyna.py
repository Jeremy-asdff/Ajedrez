from piezas import Pieza

class Reyna(Pieza):
    def __init__(self,nombre,color,movimiento_Horizontal_Vertical_Diagonal,mata_en_Horizontal_Vertical_Diagonal):
        super().__init__(nombre,color)
        self.movimiento_Horizontal_Vertical_Diagonal = movimiento_Horizontal_Vertical_Diagonal
        self.mata_en_Horizontal_Vertical_Diagonal = mata_en_Horizontal_Vertical_Diagonal
    
    