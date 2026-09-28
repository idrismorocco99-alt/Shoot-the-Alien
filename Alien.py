import pgzrun
import random

WIDTH = 600
HEIGHT = 600

TITLE = ("Shoot the Aien!$")
alienIdris=Actor("alien")
message = " "
r,g,b = 17, 68, 214

def draw():
    screen.clear()
    screen.fill((r,g,b ))
    alienIdris.draw()
    screen.draw.text(message,(507,20),color = "gold")

def on_mouse_down(pos):
    global message, r,g,b
    if alienIdris.collidepoint(pos):
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      message = ("Good Shot!")
      move_alien()

    else:
        message = "Get Better"

def move_alien():
    alienIdris.x=random.randint(0,600)
    alienIdris.y=random.randint(0,600)

move_alien()
pgzrun.go()
