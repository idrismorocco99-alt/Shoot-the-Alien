import pgzrun
import random

WIDTH = 600
HEIGHT = 600
TITLE = ("Shoot the Aien!$")
alienIdris=Actor("alien")

def draw():
    alienIdris.draw()

def move_alien():
    alienIdris.x=random.randint(0,600)
    alienIdris.y=random.randint(0,600)

move_alien()
pgzrun.go()
