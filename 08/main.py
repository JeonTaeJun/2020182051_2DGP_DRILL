
from pico2d import *
import os

def handle_events():
    global running
    global move_x
    global move_y
    global direction #0=왼쪽 달리기 1=오른쪽 달리기 2=왼쪽 가만히 3= 오른쪽 가만히

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                move_x += 1
                direction = 1
            elif event.key == SDLK_LEFT:
                move_x -= 1
                direction = 0
            elif event.key == SDLK_UP:
                move_y += 1
                if direction == 3:
                    direction = 1
                elif direction ==2:
                    direction = 0
            elif event.key == SDLK_DOWN:
                move_y -= 1
                if direction == 3:
                    direction = 1
                elif direction == 2:
                    direction = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                move_x -= 1
                direction = 3
            elif event.key == SDLK_LEFT:
                move_x += 1
                direction = 2
            elif event.key == SDLK_UP:
                move_y -= 1
                if direction == 1:
                    direction = 3
                elif direction == 0:
                    direction = 2
            elif event.key == SDLK_DOWN:
                move_y += 1
                if direction == 1:
                    direction = 3
                elif direction == 0:
                    direction = 2

running = True
x = 1280 // 2
y = 1024 // 2
motion=0
frame = 0
move_x = 0
move_y = 0
direction=0


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

pico2d.resize_canvas(1280, 1024)

while running:
    clear_canvas()
    ground.draw(640, 550)
    character.clip_draw(frame * 100, motion, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if x<0:
        x+=5
    elif x>1280:
        x-=5

    if y < 0:
        y += 5
    elif y > 1024:
        y -= 5

    x += move_x * 5
    y += move_y *5
    motion = direction *100
    delay(0.01)

close_canvas()
