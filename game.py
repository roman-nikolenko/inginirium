from random import *
from tkinter import *

label = Label

def move_by_keys(event):
    info_coords = canvas.coords(player)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x) + ' ' + str(y))
    if event.keysym == 'Up':
        canvas.move(player, 0, -20)
    elif event.keysym == 'Down':
        canvas.move(player, 0, 20)
    elif event.keysym == 'Left':
        canvas.move(player, -20, 0)
    elif event.keysym == 'Right':
        canvas.move(player, 20, 0)

num = randint(1,4)
print(num)

def following_enemy_numbers():
    if num == 1:
                canvas.move(enemy, 0, -20)
    elif num == 2:
                canvas.move(enemy, 0, 20)
    elif num == 3:
                canvas.move(enemy, -20, 0)
    elif num == 4:
                canvas.move(enemy, 20, 0)

num2 = following_enemy_numbers

def following_enemy(event):
    if event.keysym == 'Up':
        following_enemy_numbers
    elif event.keysym == 'Down':
        following_enemy_numbers
    elif event.keysym == 'Left':
        following_enemy_numbers
    elif event.keysym == 'Right':
        following_enemy_numbers



root = Tk()

root.title('BrawlStars')
root.geometry('400x400')
root.resizable(width=False, height=False)
label = Label(root, text='HomeWork')
label.pack()

canvas = Canvas(root, width=400, height=400, bg='white')
player = canvas.create_oval(100, 50, 50, 100, fill='green', outline='green')
enemy = canvas.create_oval(100, 100, 150, 150, fill='red', outline='red')

root.bind('<KeyPress>', move_by_keys)
root.bind('<KeyPress>', following_enemy)


canvas.pack()

root.mainloop()