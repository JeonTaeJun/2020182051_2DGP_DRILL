from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

x = 0
while ( x < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+10
    delay(0.01)

y=90
while ( y<589):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(799,y)
    y=y+10
    delay(0.01)

x = 799
while ( x > 0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,588)
    x=x-10
    delay(0.01)
y=588
while ( y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(10,y)
    y=y-10
    delay(0.01)

x = 0
while ( x < 400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+10
    delay(0.01)


x=0;
while(x < 360):
     clear_canvas_now()
     grass.draw_now(400,30)
     character.draw_now(math.cos(x)*300+400,math.sin(x)*300+300)
     x=x+1
     delay(0.01)










    
close_canvas()
