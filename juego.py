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
    while True:
        try:
            # Usamos len(tablero) para que sea más profesional
            posicion = int(input(f"\nEs el turno de {jugador}. Elige posición (1-{len(tablero)}): ")) - 1
            if 0 <= posicion < len(tablero) and tablero[posicion] == " ":
                tablero[posicion] = jugador
                break
            else:
                print("Esa posición no es válida o ya está ocupada. Prueba otra.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    dibujar_tablero()

# Probamos un turno
jugar_turno("X")