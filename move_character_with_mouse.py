from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
r = 10

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    # global x, y
    events = get_events()
    for event in events:
        if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
    pass

def creat_hand():
    global hand_coord, character_coord, angle, value
    hand_coord = (random.randint(0, TUK_WIDTH - 50), random.randint(0, TUK_HEIGHT - 52))
    angle = math.atan2(hand_coord[1] - character_coord[1], hand_coord[0] - character_coord[0])
    value = (math.cos(angle) * r, math.sin(angle) * r)

running = True
character_coord, hand_coord, value = (TUK_WIDTH // 2, TUK_HEIGHT // 2), (0, 0), (0, 0)
frame, angle = 0, 0
hide_cursor()
creat_hand()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(hand_coord[0] + 25, hand_coord[1] - 26)
    if (value[0] >= 0):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, character_coord[0], character_coord[1])
    else:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', character_coord[0], character_coord[1], 100, 100)
    frame = (frame + 1) % 8

    character_coord = (character_coord[0] + value[0], character_coord[1] + value[1])
    if value[0] > 0 and value[1] > 0 and character_coord[0] >= hand_coord[0] and character_coord[1] >= hand_coord[1]:
        creat_hand()
    elif value[0] <= 0 and value[1] > 0 and character_coord[0] <= hand_coord[0] and character_coord[1] >= hand_coord[1]:
        creat_hand()
    elif value[0] <= 0 and value[1] <= 0 and character_coord[0] <= hand_coord[0] and character_coord[1] <= hand_coord[1]:
        creat_hand()
    elif value[0] > 0 and value[1] <= 0 and character_coord[0] >= hand_coord[0] and character_coord[1] <= hand_coord[1]:
        creat_hand()

    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()





