from pico2d import *
import game_framework
import title_state
import play_state
# fill here
# running=True
image =None
logo_time=0.0


def enter():
    global image
    image = load_image('tuk_credit.png')
    # fill here

    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    # logo time을 계산하고, 그결과에 따라 1초가 넘으면 런닝을 false로 변경
    global logo_time, running
    delay(0.01)
    if logo_time >= 1.0:
        logo_time = 0.0
        game_framework.change_state(title_state)
    logo_time += 0.01
    # fill here

    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()





