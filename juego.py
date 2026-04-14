tablero = [" " for _ in range(9)]

def dibujar_tablero():
    print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}\n")

def verificar_ganador():
    combinaciones = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] != " ":
            return tablero[a]
    return None

def jugar():
    jugador_actual = "X"
    for turno in range(9):
        dibujar_tablero()
        while True:
            try:
                pos = int(input(f"Turno de {jugador_actual}. Elige (1-9): ")) - 1
                if 0 <= pos < 9 and tablero[pos] == " ":
                    tablero[pos] = jugador_actual
                    break
                print("Movimiento no válido.")
            except ValueError:
                print("Escribe un número.")
        
        ganador = verificar_ganador()
        if ganador:
            dibujar_tablero()
            print(f"¡El jugador {ganador} ha ganado!")
            return
        
        jugador_actual = "O" if jugador_actual == "X" else "X"
    
    dibujar_tablero()
    print("¡Empate!")

jugar()