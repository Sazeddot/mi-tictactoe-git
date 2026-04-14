import tkinter as tk
from tkinter import messagebox
import random  # <--- Nuevo: para que el bot elija

TITULO_APP = "Tic-Tac-Toe vs Bot"
AUTOR = "Sazeddot"
AÑO = "2026"
INFO_ADICIONAL = f"{TITULO_APP}\nCreado por {AUTOR}\n{AÑO}"

class TicTacToe:
    COMBINACIONES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title(TITULO_APP)
        self.jugador_actual = "X" # Tú siempre eres X
        self.tablero = [" " for _ in range(9)]
        self.botones = []
        
        self.crear_menu()
        self.crear_interfaz()

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)
        menu_juego = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Juego", menu=menu_juego)
        menu_juego.add_command(label="Nuevo Juego", command=self.reiniciar_juego)
        menu_juego.add_separator()
        menu_juego.add_command(label="Salir", command=self.ventana.destroy)

    def crear_interfaz(self):
        for i in range(9):
            boton = tk.Button(self.ventana, text=" ", font=('Arial', 20, 'bold'), 
                              width=5, height=2,
                              command=lambda i=i: self.movimiento_jugador(i))
            boton.grid(row=i//3, column=i%3)
            self.botones.append(boton)

    def movimiento_jugador(self, i):
        if self.tablero[i] == " " and self.jugador_actual == "X":
            self.realizar_movimiento(i, "X")
            
            # Si no has ganado tú y hay sitio, juega el bot
            if not self.verificar_ganador() and " " in self.tablero:
                self.ventana.after(500, self.movimiento_bot) # El bot espera 0.5s para no ser instantáneo

    def movimiento_bot(self):
        # El bot busca posiciones vacías y elige una al azar
        posiciones_libres = [i for i, x in enumerate(self.tablero) if x == " "]
        if posiciones_libres:
            eleccion = random.choice(posiciones_libres)
            self.realizar_movimiento(eleccion, "O")

    def realizar_movimiento(self, i, marca):
        self.tablero[i] = marca
        color = "red" if marca == "X" else "blue"
        self.botones[i].config(text=marca, fg=color)
        
        ganador = self.verificar_ganador()
        if ganador:
            messagebox.showinfo("Fin", f"¡El jugador {ganador} ha ganado!")
            self.reiniciar_juego()
        elif " " not in self.tablero:
            messagebox.showinfo("Fin", "¡Empate!")
            self.reiniciar_juego()

    def verificar_ganador(self):
        for a, b, c in self.COMBINACIONES:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != " ":
                return self.tablero[a]
        return None

    def reiniciar_juego(self):
        self.tablero = [" " for _ in range(9)]
        for boton in self.botones:
            boton.config(text=" ", fg="black")
        self.jugador_actual = "X"

if __name__ == "__main__":
    juego = TicTacToe()
    juego.ventana.mainloop()