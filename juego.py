import tkinter as tk
from tkinter import messagebox
import random

# CONFIGURACIÓN ESTÉTICA
COLOR_FONDO = "#2c3e50"
COLOR_BOTON = "#ecf0f1"
COLOR_TEXTO_X = "#e74c3c"
COLOR_TEXTO_O = "#3498db"

class TicTacToe:
    COMBINACIONES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tic-Tac-Toe Deluxe")
        self.ventana.geometry("400x500")
        self.ventana.configure(bg=COLOR_FONDO)
        
        self.modo_vs_bot = False
        self.esperando_bot = False
        self.tablero = [" " for _ in range(9)]
        self.botones = []
        self.jugador_actual = "X"

        self.crear_menu_superior()
        self.mostrar_pantalla_inicio()

    def crear_menu_superior(self):
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)
        menu_juego = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Opciones", menu=menu_juego)
        menu_juego.add_command(label="Volver al Menú", command=self.mostrar_pantalla_inicio)
        menu_juego.add_command(label="Salir", command=self.ventana.destroy)
        
        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_info)

    def mostrar_info(self):
        messagebox.showinfo("Acerca de", "Tic-Tac-Toe Deluxe\nVersión 2.0\nCreado por Sazeddot")

    def limpiar_ventana(self):
        for widget in self.ventana.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()

    def mostrar_pantalla_inicio(self):
        self.limpiar_ventana()
        self.tablero = [" " for _ in range(9)]
        
        tk.Label(self.ventana, text="TIC-TAC-TOE", font=("Arial", 25, "bold"), 
                 bg=COLOR_FONDO, fg="white", pady=30).pack()

        tk.Button(self.ventana, text="👤 vs 👤 (Amigo)", font=("Arial", 14), width=20,
                  command=lambda: self.iniciar_juego(vs_bot=False)).pack(pady=10)
        
        tk.Button(self.ventana, text="👤 vs 🤖 (Bot)", font=("Arial", 14), width=20,
                  command=lambda: self.iniciar_juego(vs_bot=True)).pack(pady=10)

    def iniciar_juego(self, vs_bot):
        self.modo_vs_bot = vs_bot
        self.limpiar_ventana()
        self.botones = []
        
        contenedor = tk.Frame(self.ventana, bg=COLOR_FONDO)
        contenedor.pack(pady=20)

        for i in range(9):
            btn = tk.Button(contenedor, text=" ", font=('Arial', 20, 'bold'), 
                            width=5, height=2, bg=COLOR_BOTON,
                            command=lambda i=i: self.click_casilla(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.botones.append(btn)

    def click_casilla(self, i):
        if self.tablero[i] == " " and not self.esperando_bot:
            self.realizar_movimiento(i, self.jugador_actual)
            
            if not self.verificar_ganador() and " " in self.tablero:
                if self.modo_vs_bot:
                    self.esperando_bot = True
                    self.ventana.after(600, self.movimiento_bot)
                else:
                    self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def movimiento_bot(self):
        libres = [i for i, x in enumerate(self.tablero) if x == " "]
        if libres:
            eleccion = random.choice(libres)
            self.realizar_movimiento(eleccion, "O")
        self.esperando_bot = False

    def realizar_movimiento(self, i, marca):
        self.tablero[i] = marca
        color = COLOR_TEXTO_X if marca == "X" else COLOR_TEXTO_O
        self.botones[i].config(text=marca, fg=color)
        
        ganador = self.verificar_ganador()
        if ganador:
            messagebox.showinfo("¡Victoria!", f"Ganador: {ganador}")
            self.mostrar_pantalla_inicio()
        elif " " not in self.tablero:
            messagebox.showinfo("Empate", "¡Nadie gana!")
            self.mostrar_pantalla_inicio()

    def verificar_ganador(self):
        for a, b, c in self.COMBINACIONES:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != " ":
                return self.tablero[a]
        return None

if __name__ == "__main__":
    TicTacToe().ventana.mainloop()