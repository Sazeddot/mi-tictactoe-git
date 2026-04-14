# Nuestro tablero de 3x3
tablero = [" " for _ in range(9)]

def dibujar_tablero():
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

print("--- BIENVENIDO AL TIC-TAC-TOE ---")
dibujar_tablero()

def jugar_turno(jugador):
    print(f"\nEs el turno de {jugador}")
    posicion = int(input("Elige una posición (1-9): ")) - 1
    tablero[posicion] = jugador
    dibujar_tablero()

# Probamos un turno
jugar_turno("X")