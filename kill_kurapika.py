import sys
import tkinter
import random
import time

#global
check = None
job = None

#root
root = tkinter.Tk()
root.title("クラピカたたきゲーム")
root.geometry("1000x1000")

#canvas
canvas = tkinter.Canvas(root, width=1000, height=1000)
canvas.place(x=0, y=0)

#label
label = tkinter.Label(text="クラピカたたきゲーム")
label.place(x=350, y=0)
label.config(font=("normal", 30))

#border
canvas.create_rectangle(1, 60, 1000, 61, fill="black")

#button関連
def Button_click_start():
    button["text"] = "停止"
    button["command"] = Button_click_stop
    canvas.delete("kurapika")
    image_show()

def Button_click_stop():
    global job
    canvas.delete("kurapika")
    button["text"] = "開始"
    button["command"] = Button_click_start
    root.after_cancel(job)

#image表示
def image_show():
    global img
    global job
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    print(x, y)
    img = tkinter.PhotoImage(file="main_kurapika.gif")
    canvas.create_image(x, y, image=img, tag="kurapika")
    canvas.tag_bind("kurapika", "<Button-1>", img_click)
    job = root.after(1000, image_show)

def img_click(event):
    canvas.delete("kurapika")


#button
button = tkinter.Button()
button.config(command=Button_click_start, text="開始")
button.place(x=100, y=100)
button.config(font=("normal", 30))



#ウィンドウ終了
root.mainloop()