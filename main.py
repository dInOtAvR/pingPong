from pygame import *


back=(200,200,200)
win_width=600
win_height=500
window=display.set_mode((win_width,win_height))
window.fill(back)
display.set_caption('pingPong')

game=True
clock= time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type== QUIT:
            game=False
    display.update()
    clock.tick(FPS)
