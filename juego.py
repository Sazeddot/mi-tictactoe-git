import tkinter as tk
from tkinter import messagebox
import random
import pygame
import time

# CONFIGURACIÓN ESTÉTICA
COLOR_FONDO = "#2c3e50"
COLOR_BOTON = "#ecf0f1"
COLOR_TEXTO_X = "#e74c3c"
COLOR_TEXTO_O = "#3498db"
COLOR_GANADOR = "#2ecc71"

class TicTacToe:
    COMBINACIONES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    def __init__(self):
        pygame.mixer.init()
        try:
            self.sonido_click = pygame.mixer.Sound("click.wav")
        except:
            self.sonido_click = None

        self.ventana = tk.Tk()
        self.ventana.title("Tic-Tac-Toe Deluxe")
        self.ventana.geometry("400x550")
        self.ventana.configure(bg=COLOR_FONDO)
        
        # Estado inicial
        self.reiniciar_estado()
        self.crear_menu_superior()
        self.mostrar_pantalla_inicio()

    def reiniciar_estado(self):
        self.modo_vs_bot = False
        self.esperando_bot = False
        self.tablero = [" " for _ in range(9)]
        self.botones = []
        self.jugador_actual = "X" # X siempre empieza

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
        messagebox.showinfo("Acerca de", "Tic-Tac-Toe Deluxe v3.0\nBy Sazeddot")

    def limpiar_ventana(self):
        for widget in self.ventana.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()

    def mostrar_pantalla_inicio(self):
        self.reiniciar_estado()
        self.limpiar_ventana()
        
        tk.Label(self.ventana, text="TIC-TAC-TOE", font=("Arial", 25, "bold"), 
                 bg=COLOR_FONDO, fg="white", pady=30).pack()

        tk.Button(self.ventana, text="👤 vs 👤 (Amigo)", font=("Arial", 14), width=20,
                  command=lambda: self.iniciar_juego(vs_bot=False)).pack(pady=10)
        
        tk.Button(self.ventana, text="👤 vs 🤖 (Bot)", font=("Arial", 14), width=20,
                  command=lambda: self.iniciar_juego(vs_bot=True)).pack(pady=10)

    def iniciar_juego(self, vs_bot):
        self.modo_vs_bot = vs_bot
        self.limpiar_ventana()
        
        contenedor = tk.Frame(self.ventana, bg=COLOR_FONDO)
        contenedor.pack(pady=20)

        for i in range(9):
            btn = tk.Button(contenedor, text=" ", font=('Arial', 20, 'bold'), 
                            width=5, height=2, bg=COLOR_BOTON,
                            command=lambda i=i: self.click_casilla(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.botones.append(btn)

    def click_casilla(self, i):
        # Solo permite click si la casilla está vacía y no es el turno del bot
        if self.tablero[i] == " " and not self.esperando_bot:
            self.ejecutar_turno(i)

    def ejecutar_turno(self, i):
        if self.sonido_click: self.sonido_click.play()
        
        # Poner marca
        marca = self.jugador_actual
        self.tablero[i] = marca
        color = COLOR_TEXTO_X if marca == "X" else COLOR_TEXTO_O
        self.botones[i].config(text=marca, fg=color)
        
        # Verificar si hay ganador
        ganador, indices = self.verificar_ganador()
        
        if ganador:
            self.efecto_parpadeo(indices)
            messagebox.showinfo("¡Victoria!", f"Ganador: {ganador}")
            self.mostrar_pantalla_inicio()
            return
        
        if " " not in self.tablero:
            messagebox.showinfo("Empate", "¡Tablero lleno!")
            self.mostrar_pantalla_inicio()
            return

        # Cambiar turno
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
        
        # Si ahora le toca al Bot
        if self.modo_vs_bot and self.jugador_actual == "O":
            self.esperando_bot = True
            self.ventana.after(600, self.movimiento_bot)

    def movimiento_bot(self):
        libres = [i for i, x in enumerate(self.tablero) if x == " "]
        if libres:
            eleccion = random.choice(libres)
            self.esperando_bot = False # Liberar antes de ejecutar para evitar bloqueos
            self.ejecutar_turno(eleccion)

    def efecto_parpadeo(self, indices):
        for _ in range(3):
            for i in indices: self.botones[i].config(bg=COLOR_GANADOR)
            self.ventana.update()
            time.sleep(0.1)
            for i in indices: self.botones[i].config(bg=COLOR_BOTON)
            self.ventana.update()
            time.sleep(0.1)
        for i in indices: self.botones[i].config(bg=COLOR_GANADOR)

    def verificar_ganador(self):
        for a, b, c in self.COMBINACIONES:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != " ":
                return self.tablero[a], (a, b, c)
        return None, None

if __name__ == "__main__":
    TicTacToe().ventana.mainloop()