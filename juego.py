import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    # Movimos las combinaciones aquí arriba (Constante de clase)
    COMBINACIONES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tic-Tac-Toe Pro")
        self.jugador_actual = "X"
        self.tablero = [" " for _ in range(9)]
        self.botones = []
        self.crear_interfaz()

    def crear_interfaz(self):
        for i in range(9):
            boton = tk.Button(self.ventana, text=" ", font=('Arial', 20, 'bold'), 
                              width=5, height=2,
                              command=lambda i=i: self.presionar_boton(i))
            boton.grid(row=i//3, column=i%3)
            self.botones.append(boton)

    def presionar_boton(self, i):
        # Quitamos el verificar_ganador de aquí para no repetir
        if self.tablero[i] == " ":
            self.tablero[i] = self.jugador_actual
            self.botones[i].config(text=self.jugador_actual)
            
            ganador = self.verificar_ganador()
            if ganador:
                messagebox.showinfo("Fin del juego", f"¡El jugador {ganador} ha ganado!")
                self.reiniciar_juego()
            elif " " not in self.tablero:
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.reiniciar_juego()
            else:
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def verificar_ganador(self):
        # Ahora usa la constante de la clase self.COMBINACIONES
        for a, b, c in self.COMBINACIONES:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != " ":
                return self.tablero[a]
        return None

    def reiniciar_juego(self):
        self.tablero = [" " for _ in range(9)]
        for boton in self.botones:
            boton.config(text=" ")
        self.jugador_actual = "X"

if __name__ == "__main__":
    juego = TicTacToe()
    juego.ventana.mainloop()