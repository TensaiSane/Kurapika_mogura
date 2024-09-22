import tkinter as tk
import random
import time

class KurapikaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("クラピカたたきゲーム")
        self.master.geometry("1000x1000")

        self.canvas = tk.Canvas(self.master, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        self.label = tk.Label(self.master, text="クラピカたたきゲーム")
        self.label.place(x=350, y=0)
        self.label.config(font=("normal", 30))

        self.canvas.create_rectangle(1, 60, 1000, 61, fill="black")

        self.button = tk.Button(self.master, text="開始/停止", command=self.toggle_game)
        self.button.place(x=100, y=100)
        self.button.config(font=("normal", 30))

        self.running = False
        self.img = None

    def toggle_game(self):
        self.running = not self.running
        if self.running:
            self.button.config(text="停止")
            self.master.after(0, self.game_loop)
        else:
            self.button.config(text="開始")
            self.canvas.delete("kurapika")

    def show_image(self):
        x = random.randint(0, 900)
        y = random.randint(100, 900)
        self.img = tk.PhotoImage(file="main_kurapika.gif")
        self.canvas.create_image(x, y, image=self.img, tag="kurapika")
        self.canvas.tag_bind("kurapika", "<Button-1>", self.img_click)
        print(f"画像を表示: ({x}, {y})")

    def img_click(self, event):
        self.canvas.delete("kurapika")
        print("画像がクリックされました")

    def game_loop(self):
        if self.running:
            self.show_image()
            self.master.after(2000, self.game_loop)

def main():
    root = tk.Tk()
    game = KurapikaGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()