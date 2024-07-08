from peon import Peon


def mainn():
    tablero = [["♜","♞","♝","♛","♚","♝","♞","♜"],
               ["♟","♟","♟","♟","♟","♟","♟","♟"],
               ["  ","  ","  ","  ","  ","  ","  ","  "],
               ["  ","  ","  ","  ","  ","  ","  ","  "],
               ["  ","  ","  ","  ","  ","  ","  ","  "],
               ["  ","  ","  ","  ","  ","  ","  ","  "],
               ["♙","♙","♙","♙","♙","♙","♙","♙"],
               ["♖","♘","♗","♕","♔","♗","♘","♖"]]
    
    tablero_actu(tablero)  
  
    while True:
        fila_peon = input("Fila del peón a mover ")
        columna_peon = input("Columna del peón a mover ")
        fila_destino = input("Fila de destino del peón")
        columna_destino = input("Columna de destino del peón")
        
        if fila_peon.isdigit() and columna_peon.isdigit() and fila_destino.isdigit() and columna_destino.isdigit():
            fila_peon = int(fila_peon)
            columna_peon = int(columna_peon)
            fila_destino = int(fila_destino)
            columna_destino = int(columna_destino)
            
            if 0 <= fila_peon < 8 and 0 <= columna_peon < 8 and 0 <= fila_destino < 8 and 0 <= columna_destino < 8:
                if movimiento_peon(tablero, (fila_peon, columna_peon), (fila_destino, columna_destino)):
                    tablero_actu(tablero)
                else:
                    print("Movimiento inválido")


def movimiento_peon(tablero, ubicacion_del_peon, destino_del_peon):
    fila_del_peon, columna_del_peon = ubicacion_del_peon
    fila_destino_peon, columna_destino_peon = destino_del_peon
    
    if not (0 <= fila_del_peon < 8 and 0 <= columna_del_peon < 8 and
            0 <= fila_destino_peon < 8 and 0 <= columna_destino_peon < 8):
        print("Ubicación fuera del tablero")
        return False
    
    if tablero[fila_del_peon][columna_del_peon] != "♙":
        print("No hay un peón blanco en esta casilla")
        return False
    
    if fila_destino_peon == fila_del_peon - 1 and columna_destino_peon == columna_del_peon:
        
        if tablero[fila_destino_peon][columna_destino_peon] == "  ":
            tablero[fila_destino_peon][columna_destino_peon] = tablero[fila_del_peon][columna_del_peon]
            tablero[fila_del_peon][columna_del_peon] = "  "
            return tablero 
            
        print("Casilla de destino no disponible")
        return False

def tablero_actu(tablero):
    for fila in tablero:
        for casilla in fila:
            print(casilla, final=' ')
        print()

if __name__ == "__main__":
    mainn()
