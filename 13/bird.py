import random

from pico2d import *
import game_world
import game_framework


from pico2d import *
import game_world
import game_framework

# bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # km / Hour 새의 움직이는 속도를 지정합니다.
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = ( RUN_SPEED_MPM / 60.0 )
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5



class bird:
    image = None

    def __init__(self):
        if bird.image == None:
            bird.image = load_image('bird_animation.png')
        self.x=random.randint(300,800)
        self.y=random.randint(400,500)
        self.velocity = RUN_SPEED_PPS

        #self.y = random.randint(400,500)

        self.count =0
        self.frame = 0
        self.frame2=0
        self.dir = 0


        self.Width = 183
        self.Height = 169

        if random.randint(1,2) == 1:
            self.velocity *= -1




    def draw(self):
        # 오른쪽
        if self.velocity >= 1:
            self.image.clip_draw(int(self.frame) * 183, 169*2, self.Width, self.Height, self.x, self.y)
        # 왼쪽
        else:
            self.image.clip_composite_draw(int(self.frame) * 183 ,169*2, self.Width, self.Height, 0.0, 'h', self.x, self.y,self.Width,self.Height)

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if self.x < 50 or self.x > 1600 - 50:
            self.velocity *= -1

        self.dir = clamp(-1, self.velocity, 1)