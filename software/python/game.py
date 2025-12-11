import tkinter as tk
import random
import time
import winsound

window = tk.Tk()
window.title("La città perduta")
window.geometry("500x500")

class city:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid_buttons = [[None for _ in range(width)] for _ in range(height)]

class player:
    def __init__(self, x, y, symbol):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.punti = 0

    def __str__(self):
        return f"Posizione attuale: {self.x} : {self.y}"
    
class mosse_player:
    def __init__(self):
        self.mosse = 0

class enemy:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.mosse = 0
        self.punti = 0

citta = city(15,15)
x_player = citta.width // 2
y_player = citta.height // 2
giocatore = player(x_player, y_player, "🧍")
mosse = mosse_player()
comunista = enemy(0, 0, "🟥")
timer = 0

def incrementa_time(label):
    global timer
    timer = timer + 1
    label.config(text=f"Tempo trascorso: {timer}s")
    window.after(1000, lambda: incrementa_time(label))

def player_win():
    winsound.PlaySound("winner_player.wav", winsound.SND_ASYNC)

def enemy_win():
    winsound.PlaySound("winner_enemy.wav", winsound.SND_ASYNC)

def player_sound():
    winsound.PlaySound("player.wav", winsound.SND_ASYNC)

def comunista_sound():
    winsound.PlaySound("enemy.wav", winsound.SND_ASYNC)

def init_game():
    global giocatore, comunista, mosse, timer

    for widget in window.winfo_children():
        widget.destroy()

    mosse.mosse = 0
    giocatore.x = citta.width // 2
    giocatore.y = citta.height // 2
    comunista.x = 0
    comunista.y = 0
    timer = 0

    for w in range(citta.width):
        for h in range(citta.height):
            scelta = random.randint(1, 2)
            if scelta == 1:
                circle = tk.Button(text="⬜", width=2, height=2, bg="white")
                circle.grid(row=h, column=w)
                circle.original_text = "⬜"
                circle.original_bg = "white"
                circle.original_fg = "black"
                citta.grid_buttons[h][w] = circle
            else:
                circle = tk.Button(text="🌳", width=2, height=2, bg="white")
                circle.grid(row=h, column=w)
                circle.original_text = "🌳"
                circle.original_bg = "white"
                circle.original_fg = "black"
                citta.grid_buttons[h][w] = circle

    label_mosse = tk.Label(text=f"Mosse player: {mosse.mosse}", fg="black")
    label_mosse.grid(row=citta.height + 3, column=citta.width + 1)

    label_mosse_avversario = tk.Label(text=f"Mosse Comunista: {comunista.mosse}", fg="black")
    label_mosse_avversario.grid(row=citta.height + 4, column=citta.width + 1)

    label_timer = tk.Label(text=f"Tempo trascorso: {timer}s")
    label_timer.grid(row=citta.height + 5, column=citta.width + 1)
    window.after(1000, lambda: incrementa_time(label_timer))

    citta.grid_buttons[giocatore.y][giocatore.x].config(text=giocatore.symbol, bg="lightgreen", fg="white")
    citta.grid_buttons[comunista.y][comunista.x].config(text=comunista.symbol, bg="red", fg="white")

    def move(event):
        if event.keysym == "w" or event.keysym == "s" or event.keysym == "a" or event.keysym == "d":
            prev_x, prev_y = giocatore.x, giocatore.y
            citta.grid_buttons[prev_y][prev_x].config(text=citta.grid_buttons[prev_y][prev_x].original_text, bg=citta.grid_buttons[prev_y][prev_x].original_bg, fg=citta.grid_buttons[prev_y][prev_x].original_fg)
            if event.keysym == "w" and giocatore.y > 0:
                giocatore.y -= 1
                mosse.mosse += 1
                player_sound()
            if event.keysym == "s" and giocatore.y < citta.height - 1:
                giocatore.y += 1
                mosse.mosse += 1
                player_sound()
            if event.keysym == "a" and giocatore.x > 0:
                giocatore.x -= 1
                mosse.mosse += 1
                player_sound()
            if event.keysym == "d" and giocatore.x < citta.width - 1:
                giocatore.x += 1
                mosse.mosse += 1
                player_sound()

            citta.grid_buttons[giocatore.y][giocatore.x].config(text=giocatore.symbol, bg="lightgreen", fg="white")
        else:
            prev_x, prev_y = comunista.x, comunista.y
            citta.grid_buttons[prev_y][prev_x].config(text=citta.grid_buttons[prev_y][prev_x].original_text, bg=citta.grid_buttons[prev_y][prev_x].original_bg, fg=citta.grid_buttons[prev_y][prev_x].original_fg)
            if event.keysym == "Up" and comunista.y > 0:
                comunista.y -= 1
                comunista.mosse += 1
                comunista_sound()
            if event.keysym == "Down" and comunista.y < citta.height - 1:
                comunista.y += 1
                comunista.mosse += 1
                comunista_sound()
            if event.keysym == "Left" and comunista.x > 0:
                comunista.x -= 1
                comunista.mosse += 1
                comunista_sound()
            if event.keysym == "Right" and comunista.x < citta.width - 1:
                comunista.x += 1
                comunista.mosse += 1
                comunista_sound()

            citta.grid_buttons[comunista.y][comunista.x].config(text=comunista.symbol, bg="red", fg="white")

        if comunista.x == giocatore.x and comunista.y == giocatore.y:
            comunista.punti += 1
            print("Sei stato infettato dal comunista! HAI PERSO!")
            for widget in window.winfo_children():
                widget.destroy()
            label_sconfitta = tk.Label(text=f"Giocatore, hai perso!\nSei stato infettato dal comunismo!\n\nPunti generali\nPlayer: {giocatore.punti}\nComunista: {comunista.punti}\n\nTempo totale: {timer}s", fg="black")
            label_sconfitta.place(relx=0.5, rely=0.5, anchor="center")
            button_restart = tk.Button(text="Ricomincia", command=init_game)
            button_restart.place(relx=0.5, rely=0.7, anchor="center")
            enemy_win()

        if mosse.mosse >= 20:
            giocatore.punti += 1
            print("Il comunista non ha più fiato! COMPLIEMNTI PLAYER HAI VINTO")
            for widget in window.winfo_children():
                widget.destroy()
            label_sconfitta = tk.Label(text=f"Il comunista non ha più fiato!\nCOMPLIEMNTI PLAYER HAI VINTO\n\nPunti generali\nPlayer: {giocatore.punti}\nComunista: {comunista.punti}\n\nTempo totale: {timer}s", fg="black")
            label_sconfitta.place(relx=0.5, rely=0.5, anchor="center")
            button_restart = tk.Button(text="Ricomincia", command=init_game)
            button_restart.place(relx=0.5, rely=0.7, anchor="center")
            player_win()

        label_mosse.config(text=f"Mosse player: {mosse.mosse}")
        label_mosse_avversario.config(text=f"Mosse Comunista: {comunista.mosse}")

    window.bind("<Key>", move)

init_game()

if __name__ == "__main__":
    window.mainloop()