import tkinter as tk
import winsound

window = tk.Tk()
window.geometry("500x500")
window.title("Escape from the comunist!")

class players:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.punti = 0
        self.morti = 0
        self.velocita = 10

fascio = players(0, 30, "X")
comuni = players(100, 100, "O")
timer = 0

def winner_fascio():
    winsound.PlaySound("winner_player.wav", winsound.SND_ASYNC)

def winner_comuni():
    winsound.PlaySound("winner_enemy.wav", winsound.SND_ASYNC)

def incrementa_timer(label):
    global timer
    timer += 1
    label.config(text=f"tempo passato: {timer}")
    if timer >= 60:
        for widget in window.winfo_children():
            widget.destroy()
        fascio.punti += 1
        comuni.morti += 1
        label_sconfitta = tk.Label(text=f"FASCISM WIN!\n\nPoints:\nFascio: {fascio.punti}\nComuni: {comuni.punti}\n\nDeaths:\nFascio: {fascio.morti}\nComuni: {comuni.morti}\n\nTime past: {timer}")
        label_sconfitta.place(relx=0.5, rely=0.5, anchor="center")
        button_restart = tk.Button(text=f"Restart the game", command=init_game)
        button_restart.place(relx=0.5, rely=0.7, anchor="center")
    else:
        window.after(1000, lambda: incrementa_timer(label))

def init_game():
    global timer

    for widget in window.winfo_children():
        widget.destroy()

    timer = 0
    fascio.x = 0
    fascio.y = 30
    comuni.x = 100
    comuni.y = 100

    fascio_label = tk.Label(text=fascio.symbol, bg="black", fg="white")
    fascio_label.place(x=fascio.x, y=fascio.y)

    comuni_label = tk.Label(text=comuni.symbol, bg="red", fg="white")
    comuni_label.place(x=comuni.x, y=comuni.y)

    timer_label = tk.Label(text=f"tempo passato: {timer}", bg="black", fg="white")
    timer_label.place(x=0, y=0)

    window.after(1000, lambda: incrementa_timer(timer_label))

    def move(ev):
        if ev.keysym == "w" or ev.keysym == "a" or ev.keysym == "d" or ev.keysym == "s":
            if ev.keysym == "w" and comuni.y > 0:
                comuni.y -= comuni.velocita

            if ev.keysym == "a" and comuni.x > 0:
                comuni.x -= comuni.velocita

            if ev.keysym == "d" and comuni.x < 485:
                comuni.x += comuni.velocita

            if ev.keysym == "s" and comuni.y < 480:
                comuni.y += comuni.velocita
            
            comuni_label.place(x=comuni.x, y=comuni.y)

        
        if ev.keysym == "Up" or ev.keysym == "Down" or ev.keysym == "Left" or ev.keysym == "Right":
            if ev.keysym == "Up" and fascio.y > 0:
                fascio.y -= fascio.velocita

            if ev.keysym == "Left" and fascio.x > 0:
                fascio.x -= fascio.velocita

            if ev.keysym == "Right" and fascio.x < 485:
                fascio.x += fascio.velocita

            if ev.keysym == "Down" and fascio.y < 480:
                fascio.y += fascio.velocita
            
            fascio_label.place(x=fascio.x, y=fascio.y)

        if abs(comuni.x - fascio.x) <= 10 and abs(comuni.y - fascio.y) <= 10:
            for widget in window.winfo_children():
                widget.destroy()
            comuni.punti += 1
            fascio.morti += 1
            label_sconfitta = tk.Label(text=f"You've been trapped by comunism!\n\nPoints:\nFascio: {fascio.punti}\nComuni: {comuni.punti}\n\nDeaths:\nFascio: {fascio.morti}\nComuni: {comuni.morti}\n\nTime past: {timer}")
            label_sconfitta.place(relx=0.5, rely=0.5, anchor="center")
            button_restart = tk.Button(text=f"Restart the game", command=init_game)
            button_restart.place(relx=0.5, rely=0.7, anchor="center")

    window.bind("<Key>", move)

init_game()

if __name__ == "__main__":
    window.mainloop()