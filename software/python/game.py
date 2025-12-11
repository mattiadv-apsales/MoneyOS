import tkinter as tk
import random

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

    def __str__(self):
        return f"Posizione attuale: {self.x} : {self.y}"

citta = city(15,15)
x_player = citta.width // 2
y_player = citta.height // 2
giocatore = player(x_player, y_player, "@")

for w in range(citta.width):
    for h in range(citta.height):
        scelta = random.randint(1, 2)
        if scelta == 1:
            circle = tk.Button(text="O", width=1, height=1, bg="white")
            circle.grid(row=h, column=w)
            circle.original_text = "O"
            citta.grid_buttons[h][w] = circle
        else:
            circle = tk.Button(text="-", width=1, height=1, bg="white")
            circle.grid(row=h, column=w)
            circle.original_text = "-"
            citta.grid_buttons[h][w] = circle

citta.grid_buttons[giocatore.y][giocatore.x].config(text=giocatore.symbol, bg="lightgreen", fg="white")

def move(event):
    prev_x, prev_y = giocatore.x, giocatore.y
    citta.grid_buttons[prev_y][prev_x].config(text=citta.grid_buttons[prev_y][prev_x].original_text, bg="white", fg="black")
    if event.keysym == "w" and giocatore.y > 0:
        giocatore.y -= 1
    if event.keysym == "s" and giocatore.y < citta.height - 1:
        giocatore.y += 1
    if event.keysym == "a" and giocatore.x > 0:
        giocatore.x -= 1
    if event.keysym == "d" and giocatore.x < citta.width - 1:
        giocatore.x += 1

    citta.grid_buttons[giocatore.y][giocatore.x].config(text=giocatore.symbol, bg="lightgreen", fg="white")
    print(giocatore)

window.bind("<Key>", move)

if __name__ == "__main__":
    window.mainloop()