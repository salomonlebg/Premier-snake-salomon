import tkinter
import time
from tkinter import messagebox
canvasWidth = 600
canvasHeight = 600
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="darkblue")
canvas.pack()
serp1 = canvas.create_rectangle(0, 0, 50, 50, fill="red")

windowOpen= True
def main_loop():
    while windowOpen == True:
        move_serp1()
        window.update()
        time.sleep(0.02)
        if windowOpen == True:
            check_game_over()

leftPressed = 0
rightPressed = 0
upPressed = 0
downPressed = 0

def on_key_press(event):
    global leftPressed, rightPressed, upPressed, downPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1
    elif event.keysym == "Up":
        upPressed = 1
    elif even.keysym == "Down":
        downPressed = 1

def on_key_release(event):
    global leftPressed, rightPressed, upPressed, downPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0
    elif event.keysym == "Up":
        upPressed = 0
    elif even.keysym == "Down":
        downPressed = 0

serp1MoveX = 4
serp1MoveY = -4

def move_serp1():
    global serp1MoveX, serp1MoveY
    (serp1Left, serp1Top, serp1Right, serp1Bottom) = canvas.coords(serp1)

  
    canvas.move(serp1, serp1MoveX, serp1MoveY)


def check_game_over():
    (serp1Left, serp1Top, serp1Right, serp1Bottom) = canvas.coords(serp1)
    if serp1Bottom > canvasHeight:
        close()
    elif serp1Top < 0:
        close()
    elif serp1Left < 0:
        close()
    elif serp1Right > canvasWidth:
        close()
def close():
    global windowOpen
    windowOpen = False
    window.destroy()
     
    
window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)











    

