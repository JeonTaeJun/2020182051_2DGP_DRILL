from pico2d import *
import game_framework
import title_state
import play_state
# fill here
# running=True
import play_state

image =None


def enter():
    global image
    image = load_image('item_select.png')
    # fill here

    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    #play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_state.boy.itam = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    play_state.boy.itam = 'ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    play_state.boy.itam = 'bigball'
                    game_framework.pop_state()





