from pico2d import *
import game_framework
import title_state
import play_state
# fill here
# running=True
import play_state
import play_state
image =None

num = 0
def enter():
    global image
    image = load_image('add_delete_boy.png')
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
                case pico2d.SDLK_z:
                    play_state.num += 1
                    play_state.boy.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_k:
                    play_state.num -= 1
                    del play_state.boy[play_state.num]
                    game_framework.pop_state()





