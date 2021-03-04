from arcade import *
import random
import time
open_window(600, 400, 'rainbow')

set_background_color(color.WHITE)


for i in range(6):
    start_render()
    for i in range(6):
        r = random.randint(0, 255)
        g = random.randint(0, 225)
        b = random.randint(0, 255)
        draw_circle_filled(300, 0, 300-i*10, (r, g, b))
    draw_circle_filled(300, 0, 240, color.WHITE)
    finish_render()
    time.sleep(0.5)
#run()




