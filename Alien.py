import pgzrun
import random

WIDTH = 600
HEIGHT = 600

TITLE = ("Shoot the Aien!$")
alienIdris=Actor("alien")
message = " "

def draw():
    screen.clear()
    screen.fill("silver")
    alienIdris.draw()
    screen.draw.text(message,(507,20),color = "gold")

def on_mouse_down(pos):
    global message
    if alienIdris.collidepoint(pos):
      message = ("Good Shot!")
      move_alien()

    else:
        message = "Get Better"

def move_alien():
    alienIdris.x=random.randint(0,600)
    alienIdris.y=random.randint(0,600)

move_alien()
pgzrun.go()
