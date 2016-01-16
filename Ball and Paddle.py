# Iridescence - a bouncing ball game about colors, perfection and imperfection
# Submitted by Joyce Yang, Fleetwood Park Secondary
# April 30, 2015
# Special thanks to Ms. Stusiak, without whom you would probably never see
# this game functioning properly :)

import simplegui
import random
import math

# colors and sounds
DEFAULT_COLOR = "#e6e6fa" # very light purple
COLOR1 = "#8a0303"  # blood red
COLOR2 = "#cd3a3e"  # ruby red
COLOR3 = "#9b3752"  # rose pink
COLOR4 = "#ff7171"  # dark peach
COLOR5 = "#f69a9a"  # peach
COLOR6 = "#ffde8d"  # peachy orange
COLOR7 = "#f1e94b"  # lemon yellow
COLOR8 = "#fefe00"  # bright yellow
COLOR9 = "#bfeebe"  # mint green
COLOR10 = "#b6d877" # pale green
COLOR11 = "#aef357" # lime green
COLOR12 = "#4dae4e" # emerald green
COLOR13 = "#6c8d71" # ink green
COLOR14 = "#54862e" # grass green
COLOR15 = "#afc4db" # pale blue
COLOR16 = "#b8f4e7" # mint blue
COLOR17 = "#6699cc" # blue
COLOR18 = "#6564bf" # bluish indigo
COLOR19 = "#27224d" # indigo
COLOR20 = "#d5b8d8" # lavendar
COLOR21 = "#634163" # plum
COLOR22 = "#8850f6" # purple
COLOR23 = "#ee82ee" # violet
COLOR24 = "#aeaeae" # grey
COLOR_LIST = [COLOR1, COLOR2, COLOR3, COLOR4, COLOR5,
              COLOR6, COLOR7, COLOR8, COLOR9, COLOR10,
              COLOR11, COLOR12, COLOR13, COLOR14, COLOR15,
              COLOR16, COLOR17, COLOR18, COLOR19, COLOR20,
              COLOR21, COLOR22, COLOR23, COLOR24]
PREFIX = 'https://docs.google.com/uc?export=download&id='
BEETHOVEN_MOONLIGHT_SONATA = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1R3d3Q3Y1OVhmSEk")
CHOPIN_NOCTURNE_OP9No2 = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1d1ZuTXV6NTREdnM")
TCHAIKOVSKY_BOAT_SONG = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1aW84ZzlGZ0xYaUU")
MOZART_TURKISH_MARCH = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1OFlYOVNnSFVPQWs")
BACH_AIR_ON_G_STRING = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1S1B4ZnZ5V0tEVkk")
MUSIC_DICT = {1: CHOPIN_NOCTURNE_OP9No2, 2: TCHAIKOVSKY_BOAT_SONG,
             3: BEETHOVEN_MOONLIGHT_SONATA, 0: MOZART_TURKISH_MARCH,
             "title_bkgd": BACH_AIR_ON_G_STRING}
PIANO_KEY_A = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1SHQ2eGVSWkUwaG8")
PIANO_KEY_Ab = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1WGtjcEZPT2k2LTg")
PIANO_KEY_B = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1Vk5FVXplSVAtUVU")
PIANO_KEY_Bb = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1cnFEdlp1YkVIRzA")
PIANO_KEY_C = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1V2Vjc0F3SjJrNmc")
PIANO_KEY_D = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1VjUydVpQZFRkUDg")
PIANO_KEY_Db = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1V2MyeUZ1VW5MeTA")
PIANO_KEY_E = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1cWhlV3RvYXB2M1E")
PIANO_KEY_Eb = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1VlFqdm1Vd1BXSVE")
PIANO_KEY_F = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1ZGhLQW91VGktUWM")
PIANO_KEY_G = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1c3I1WG1yWnJRQ28")
PIANO_KEY_Gb = simplegui.load_sound(PREFIX + "0B2YMlW0M79d1bGxIQ3ZPc1FjWGM")
PIANO_KEY_DICT = {COLOR18: PIANO_KEY_C, COLOR19: PIANO_KEY_C,
                  COLOR1: PIANO_KEY_D, COLOR22: PIANO_KEY_D,
                  COLOR2: PIANO_KEY_Db, COLOR23: PIANO_KEY_Db,
                  COLOR13: PIANO_KEY_E, COLOR14: PIANO_KEY_E,
                  COLOR4: PIANO_KEY_Eb, COLOR21: PIANO_KEY_Eb,
                  COLOR12: PIANO_KEY_F, COLOR20: PIANO_KEY_F,
                  COLOR3: PIANO_KEY_G, COLOR5: PIANO_KEY_G,
                  COLOR6: PIANO_KEY_Gb, COLOR17: PIANO_KEY_Gb,
                  COLOR8: PIANO_KEY_A, COLOR11: PIANO_KEY_A,
                  COLOR7: PIANO_KEY_Ab, COLOR16: PIANO_KEY_Ab,
                  COLOR9: PIANO_KEY_B, COLOR15: PIANO_KEY_B,
                  COLOR10: PIANO_KEY_Bb, COLOR24: PIANO_KEY_Bb}

# Images
left_arrow_img = simplegui.load_image("http://www.wpclipart.com/signs_symbol/BW/direction_arrows/left_arrow_sign.png")
right_arrow_img = simplegui.load_image("http://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Aiga_rightarrow_inv.svg/500px-Aiga_rightarrow_inv.svg.png")
up_arrow_img = simplegui.load_image("https://cdn4.iconfinder.com/data/icons/dot/256/arrow_up_1.png")
down_arrow_img = simplegui.load_image("http://i229.photobucket.com/albums/ee166/shepheard79/down_arrow_inv1245951673.png")
pointer_img = simplegui.load_image("http://alecjacobson.com/weblog/media/mac-cursor.png")
IMG_DICT = {"left_arrow": (255, 256), 
            "right_arrow": (500, 500), 
            "up_arrow": (256, 256), 
            "down_arrow": (400, 401),
            "pointer": (286, 429)}

# Constant initialization
BALL_RAD = 50.0
BALL_VEL_INIT = [3.0, 3.0]
BALL_COLOR_INIT = DEFAULT_COLOR
TREASURE_RAD = 10.0
FRAME_WIDTH = 950.0
FRAME_HEIGHT = 700.0
PADDLE_WIDTH = 150.0
PADDLE_HEIGHT = 100.0
PADDLE_VEL = [5.0, 5.0]
PADDLE_POS = [FRAME_WIDTH / 2, FRAME_HEIGHT - PADDLE_HEIGHT / 2]
PADDLE_COLOR = "#ffa500" # orange
PROGRESS_BAR_WIDTH = FRAME_WIDTH * 0.2
PROGRESS_BAR_HEIGHT = FRAME_HEIGHT * 0.03
PROGRESS_BAR_POS = [FRAME_WIDTH * 0.88, FRAME_HEIGHT * 0.112]
KEYBOARD_POS = [FRAME_WIDTH / 2, FRAME_HEIGHT * 0.6]
KEYBOARD_WIDTH = FRAME_WIDTH * 0.9
KEYBOARD_HEIGHT = FRAME_HEIGHT * 0.3

# Variable initialization
level_num = 1
treasure_num = 0
mouse_pos = [0,0]
time_count = 0
ball_list = []
paddle_list = []
progress_bar_color_list = []
rec_corner = {}
# text colors in the title page
font_color_list = [COLOR2, COLOR18, COLOR7, COLOR17, COLOR16, COLOR10, COLOR4,
                   COLOR3, COLOR12, COLOR20, COLOR8]
# colors of the sample keyboard in the helper page
helper_keyboard_color_list = progress_bar_color_list = [COLOR10, COLOR19, COLOR3, COLOR2, COLOR8, 
                                                        COLOR23, COLOR16, COLOR10, COLOR23, COLOR13]
# Initialize hitting_sound
hitting_sound = PIANO_KEY_C
title_page_display = True
helper_page_display = False
game_over = False
treasure_present = False
# moving_up/down/left/right indicate which the key-board controlled spring will move
moving_up = False
moving_down = False
moving_left = False
moving_right = False
# bouncing_left(right)(down) indicate which way (relative to the paddle) the ball collides
bouncing_left = False
bouncing_right = False
bouncing_down = False
# not continue_moving: the involuntary stop of the ball
# ex: when the ball stops moving, when game is over or when the player reaches the next level
# continue_moving = True when the player hits space to continue
continue_moving = False
# pause controls the active start and stop of the ball controlled by the player when "P" is hit
pause = False
# bkgd_music_playing and level_inc control the start and stop
# of the different bkgd music played in each level
bkgd_music_playing = False
level_inc = False
# piano_display controls the display of the keyboard at the end of each level
piano_display = False
# new_sound controls the new sound in keyboard playing
new_sound = False

# Initiate title page and thus the entire game
def start_game():
    global ball_list, paddle_list, timer, sound
    
    sound = MUSIC_DICT['title_bkgd']
    sound.play()
    
    # Add the ball and paddle in the title page into lists
    ball_vel = [FRAME_WIDTH / 100, (FRAME_HEIGHT - PADDLE_HEIGHT - 5) / 100]
    ball = Ball(BALL_COLOR_INIT, BALL_RAD, [FRAME_WIDTH / 2, BALL_RAD], ball_vel)
    ball_list.append(ball)
    paddle = Paddle(PADDLE_COLOR, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_POS, [0,0])
    paddle_list.append(paddle)
    
    # Start the timer that changes the font color every 500 millisec
    timer.start()
     
# Start a New Game/Level with level_num
def new_game():
    global ball_list, paddle_list, progress_bar_color_list, treasure_present
    global treasure_num, time_count, continue_moving, pause
        
    ball_list = []
    paddle_list = []
    progress_bar_color_list = []
    continue_moving = False
    pause = False
    treasure_num = 0
    treasure_present = False
    time_count = 0
    
    # Add the ball and paddle into lists
    # Starting position of a ball in a new level is randomly generated
    new_pos = [random.randrange(BALL_RAD, FRAME_WIDTH - BALL_RAD), 
               random.randrange(BALL_RAD, FRAME_HEIGHT / 4)]
    # The velocity of the ball and paddle will be twice as fast as the velocity in the previous level
    new_vel = [BALL_VEL_INIT[0] * level_num, BALL_VEL_INIT[1] * level_num]
    ball = Ball(BALL_COLOR_INIT, BALL_RAD, new_pos, new_vel)
    ball_list.append(ball)
    new_vel = [PADDLE_VEL[0] * level_num, PADDLE_VEL[1] * level_num]
    paddle = Paddle(PADDLE_COLOR, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_POS, new_vel)
    paddle_list.append(paddle)

# Add treasure if treasure is not present
# New level if the player scores 10 treasures
def add_treasure():
    global treasure_num, treasure_present, ball_list
    if treasure_num == 10:
        # The next splash screen will start after the ball idly bounces for 2 seconds
        timer.start()
    else:
        treasure_num += 1
        treasure_present = True
        new_pos = [random.randrange(TREASURE_RAD, FRAME_WIDTH - TREASURE_RAD),
                   random.randrange(TREASURE_RAD, FRAME_HEIGHT - PADDLE_HEIGHT - 8 * TREASURE_RAD)]
        # color of the new treasure is randomly generated out of the COLOR_LIST
        new_color = random.choice(COLOR_LIST)
        # The new color cannot be the same as the current ball color
        while new_color == ball_list[0].get_color():
            new_color = random.choice(COLOR_LIST)
        treasure = Ball(new_color, TREASURE_RAD, new_pos, [0,0])
        ball_list.append(treasure)
        
# Helper function calculating the distance between two points
def calc_distance(pos1, pos2):
    dis_x = pos1[0] - pos2[0]
    dis_y = pos1[1] - pos2[1]
    return math.sqrt(dis_x ** 2 + dis_y ** 2)

# Helper function calculating the center_source of an image given its width and height
def calc_center(width_height_tuple):
    return (width_height_tuple[0] / 2, width_height_tuple[1] / 2)

# Helper function finding out the coordinates of the four corners of a rectangle 
# given its center position, width and height
def rec_coordinate(pos, width, height):
    global rec_corner
    rec_corner = {"leftup": (pos[0] - width / 2, pos[1] - height / 2), 
                     "leftdown": (pos[0] - width / 2, pos[1] + height / 2), 
                     "rightdown": (pos[0] + width / 2, pos[1] + height / 2), 
                     "rightup": (pos[0] + width / 2, pos[1] - height / 2)}
    
# Helper function deciding which way the ball (pos1) bounces into the paddle (pos2)
def bouncing_direction(pos1, radius, pos2, width, height):
    global bouncing_left, bouncing_right, bouncing_down
    bouncing_left = False
    bouncing_right = False
    bouncing_down = False
    # Calc the positions of four corners and edges of the paddle
    rec_coordinate(pos2, width, height)
    left_edge = rec_corner["leftup"][0]
    right_edge = rec_corner["rightup"][0]
    up_edge = rec_corner["leftup"][1]
    down_edge = rec_corner["leftdown"][1]
    # Calc the distance between the center of the ball and the corners/edges of the paddle
    dis_leftup = calc_distance(rec_corner["leftup"], pos1)
    dis_rightup = calc_distance(rec_corner["rightup"], pos1)
    dis_leftdown = calc_distance(rec_corner["leftdown"], pos1)
    dis_rightdown = calc_distance(rec_corner["rightdown"], pos1)
    dis_leftedge = left_edge - pos1[0]
    dis_rightedge = pos1[0] - right_edge
    dis_upedge = up_edge - pos1[1]
    dis_downedge = pos1[1] - down_edge
       
    # The right side of the ball bounces into the left side of the paddle
    # cond1 and cond2: the ball just bounces against the left side of the paddle (corners excluded)
    cond1 = dis_leftedge > 0 and dis_leftedge <= radius
    cond2 = dis_upedge <= 0 and dis_downedge <= 0
    # cond3: the ball bounces into the top left corner of the paddle
    cond3 = dis_upedge > 0 and dis_leftedge > 0 and dis_leftup <= radius
    # cond4: the ball bounces into the bottom left corner of the paddle
    cond4 = dis_downedge > 0 and dis_leftedge > 0 and dis_leftdown <= radius
    if  cond1 and cond2 or cond3 or cond4:
        bouncing_left = True
    # The left side of the ball bounces into the right side of the paddle
    # cond1 and cond2: the ball just bounces against the right side of the paddle (corners excluded)
    cond1 = dis_rightedge > 0 and dis_rightedge <= radius
    cond2 = dis_upedge <= 0 and dis_downedge <= 0
    # cond3: the ball bounces into the top right corner of the paddle
    cond3 = dis_upedge > 0 and dis_rightedge > 0 and dis_rightup <= radius
    # cond4: the ball bounces into the bottom right corner of the paddle
    cond4 = dis_downedge > 0 and dis_rightedge > 0 and dis_rightdown <= radius
    if cond1 and cond2 or cond3 or cond4:
        bouncing_right = True
    # The down side of the ball bounces into the up side of the paddle
    # cond1 and cond2: the ball just bounces against the up side of the paddle (corners excluded)
    cond1 = dis_upedge > 0 and dis_upedge <= radius
    cond2 = dis_leftedge <= 0 and dis_rightedge <=0
    # cond3: the ball bounces into the top left corner of the paddle
    cond3 = dis_upedge > 0 and dis_leftedge > 0 and dis_leftup <= radius
    # cond4: the ball bounces into the top right corner of the paddle
    cond4 = dis_upedge > 0 and dis_rightedge > 0 and dis_rightup <= radius
    if cond1 and cond2 or cond3 or cond4:
        bouncing_down = True

class Ball:
    def __init__(self, color, radius, position, velocity):
        self.color = color
        self.radius = radius
        self.pos = position
        self.vel = velocity
    
    def __str__(self):
        pass
    
    # Draw the ball on the canvas
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 0.1, "black", self.color)
        
    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i]
            
        # Bouncing against the left/right boundary of the screen
        if self.pos[0] <= self.radius:
            if self.vel[0] < 0:
                self.vel[0] *= -1
        if self.pos[0] >= FRAME_WIDTH - self.radius:
            if self.vel[0] > 0:
                self.vel[0] *= -1
            
        # Bouncing against the up boundary of the screen
        if self.pos[1] <= self.radius:
            if self.vel[1] < 0:
                self.vel[1] *= -1
    
    def get_color(self):
        return self.color
    
    def get_radius(self):
        return self.radius
    
    def get_pos(self):
        return self.pos
    
    # Change the color of the ball (into the color of the treasure it collides with)
    def change_color(self, new_color):
        self.color = new_color
            
    def bouncing(self, paddle):
        bouncing_direction(self.pos, self.radius, paddle.get_pos(), paddle.get_width(), paddle.get_height())
        # Reverse the horizontal moving direction if the ball traveling from the right
        # bouncing against the right side of the paddle
        if bouncing_right:
            if self.vel[0] < 0:
                self.vel[0] *= -1
        # Reverse the horizontal moving direction if the ball travelling from the left
        # bouncing against the left side of the paddle
        if bouncing_left:
            if self.vel[0] > 0:
                self.vel[0] *= -1
        # Reverse the vertical moving direction if the ball travelling from the top
        # bouncing against the up side of the paddle
        if bouncing_down:
            if self.vel[1] > 0:
                self.vel[1] *= -1
    
    def collecting_treasure(self, treasure):
        global treasure_present, ball_list, progress_bar_color_list
        # Ball-treasure collision
        if calc_distance(self.pos, treasure.get_pos()) <= self.radius + treasure.get_radius():
            self.change_color(treasure.get_color())
            progress_bar_color_list.append(treasure.get_color())
            ball_list.remove(treasure)
            treasure_present = False

class Paddle:
    def __init__(self, color, width, height, position, velocity):
        self.color = color
        self.width = width
        self.height = height
        self.pos = position
        self.vel = velocity
    
    def __str__(self):
        pass
    
    # Draw the paddle on the canvas
    def draw(self, canvas):
        rec_coordinate(self.pos, self.width, self.height)
        canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                            rec_corner["rightdown"], rec_corner["rightup"]],
                            2, self.color, self.color)
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    # The paddle is able to move left/right/up/down as long as the buttons are pressed
    # and it does not hit the walls of the frame
    def update(self):
        if moving_left:
            if self.pos[0] - self.vel[0] >= self.width / 2:
                self.pos[0] -= self.vel[0]
            else:
                self.pos[0] = self.width / 2
        if moving_right:
            if self.pos[0] + self.vel[0] <= FRAME_WIDTH - self.width / 2:
                self.pos[0] += self.vel[0]
            else:
                self.pos[0] = FRAME_WIDTH - self.width / 2
        if moving_up:
            if self.pos[1] - self.vel[1] >= self.height / 2:
                self.pos[1] -= self.vel[1]
            else:
                self.pos[1] = self.height / 2
        if moving_down:
            if self.pos[1] + self.vel[1] <= FRAME_HEIGHT - self.height / 2:
                self.pos[1] += self.vel[1]
            else:
                self.pos[1] = FRAME_HEIGHT - self.height / 2

def key_start_handler(key):
    global moving_left, moving_right, moving_up, moving_down
    global continue_moving, piano_display, pause, sound, helper_page_display
    global level_inc, treasure_num, level_num
    
    # Key left, right, up and down control the moving direction of the paddle
    if key == simplegui.KEY_MAP['left']:
        moving_left = True
    if key == simplegui.KEY_MAP['right']:
        moving_right = True
    if key == simplegui.KEY_MAP['up']:
        moving_up = True
    if key == simplegui.KEY_MAP['down']:
        moving_down = True
        
    # When space is hit in the main game: new level/game
    if key == simplegui.KEY_MAP['space'] and not title_page_display and not helper_page_display:
        continue_moving = True
    # When space is hit in the helper page: the game starts
    if key == simplegui.KEY_MAP['space'] and helper_page_display:
        sound.pause()
        helper_page_display = False
        new_game()
        
    # When "C" is hit in the piano page: new level
    if key == simplegui.KEY_MAP['C'] and piano_display:
        piano_display = False
        level_inc = True
        treasure_num = 0
        level_num += 1
        progress_bar_color_list = []
        new_game()
        
    # When "P" is hit when game is on: pause
    if not piano_display and not title_page_display and not helper_page_display:
        if key == simplegui.KEY_MAP['P']:
            pause = not pause
            if not pause:
                sound.play()
        
def key_stop_handler(key):
    global moving_left
    global moving_right
    global moving_up
    global moving_down
    if key == simplegui.KEY_MAP['left']:
        moving_left = False
    if key == simplegui.KEY_MAP['right']:
        moving_right = False
    if key == simplegui.KEY_MAP['up']:
        moving_up = False
    if key == simplegui.KEY_MAP['down']:
        moving_down = False

def mouse_handler(position):
    global mouse_pos, new_sound, title_page_display, helper_page_display, timer, ball_list, paddle_list
    
    # When mouse is clicked in the title page: the screen moves to helper page
    if title_page_display:
        timer.stop()
        title_page_display = False
        helper_page_display = True
        ball_list = []
        paddle_list = []
        paddle_pos = [FRAME_WIDTH * 0.35, FRAME_HEIGHT * 0.235]
        new_paddle = Paddle(PADDLE_COLOR, PADDLE_WIDTH * 0.6, PADDLE_HEIGHT * 0.6, paddle_pos, [0,0])
        paddle_list.append(new_paddle)
        ball = Ball(BALL_COLOR_INIT, BALL_RAD * 0.6, [FRAME_WIDTH * 0.38, FRAME_HEIGHT * 0.38], [0, 0])
        ball_list.append(ball)
        treasure = Ball(COLOR21, TREASURE_RAD, [FRAME_WIDTH * 0.83, FRAME_HEIGHT * 0.385], [0, 0])
        ball_list.append(treasure)
        ball2 = Ball(BALL_COLOR_INIT, BALL_RAD * 0.6, [FRAME_WIDTH * 0.54, FRAME_HEIGHT * 0.93], [0, 0])
        ball_list.append(ball2)
    else:
        mouse_pos = position
        new_sound = True        
        
def draw_handler(canvas):
    global game_over, level_num, continue_moving, bkgd_music_playing, level_inc, sound, hitting_sound, piano_display, new_sound
    
    # piano/keyboard page
    if piano_display:
        canvas.draw_text('COMPOSE YOUR OWN MUSIC!!', (FRAME_WIDTH * 0.2, FRAME_HEIGHT * 0.25), 40, DEFAULT_COLOR)
        canvas.draw_text('PRESS "C" TO NEXT LEVEL', (FRAME_WIDTH * 0.29, FRAME_HEIGHT * 0.35), 30, DEFAULT_COLOR)
        rec_coordinate(KEYBOARD_POS, KEYBOARD_WIDTH, KEYBOARD_HEIGHT)
        keyboard_left = rec_corner["leftup"][0]
        canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                             rec_corner["rightdown"], rec_corner["rightup"]], 3, DEFAULT_COLOR)
        # index indicates the number of each color section
        index = 0
        for color in progress_bar_color_list:
            rec_coordinate([keyboard_left + index * KEYBOARD_WIDTH / 10 + KEYBOARD_WIDTH / 20,
                            KEYBOARD_POS[1]],
                            KEYBOARD_WIDTH / 10 - 1, KEYBOARD_HEIGHT - 1.5)
            canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                                 rec_corner["rightdown"], rec_corner["rightup"]], 0.5, DEFAULT_COLOR, color)
            cond1 = mouse_pos[0] > rec_corner["leftup"][0]
            cond2 = mouse_pos[0] < rec_corner["rightup"][0]
            cond3 = mouse_pos[1] > rec_corner["leftup"][1]
            cond4 = mouse_pos[1] < rec_corner["leftdown"][1]
            # cond1 and cond2 and cond3 and cond4 and new_sound: mouse just clicks on the key
            if cond1 and cond2 and cond3 and cond4 and new_sound:
                hitting_sound.pause()
                hitting_sound.rewind()
                new_sound = False
                hitting_sound = PIANO_KEY_DICT[color]
                hitting_sound.play()
            index += 1
    else:
        # When game is over and space is hit to continue: new game starting from level 1
        if continue_moving and game_over:
            game_over = False
            bkgd_music_playing = False
            level_inc = False
            level_num = 1
            new_game()
        
        # When the main game is on...
        if not title_page_display and not helper_page_display:
            # New background music matching the new level
            if not bkgd_music_playing and not level_inc:
                sound = MUSIC_DICT[level_num % 4]
                sound.set_volume(0.7)
                sound.play()
                bkgd_music_playing = True
            # Pause the old background music
            if bkgd_music_playing and level_inc:
                sound.pause()
                sound.rewind()
                level_inc = False
                bkgd_music_playing = False
    
            # Display the "level #" at the top right corner along with the colored progress bar
            if continue_moving:
                canvas.draw_text('Level ' + str(level_num), (FRAME_WIDTH * 0.82, FRAME_HEIGHT * 0.08), 30, DEFAULT_COLOR, 'monospace')
                rec_coordinate(PROGRESS_BAR_POS, PROGRESS_BAR_WIDTH, PROGRESS_BAR_HEIGHT)
                # progress_bar_left stores the position (x-cordinate) of the progress bar's left edge to calc
                # the position of each color section of the progress bar in the future
                progress_bar_left = rec_corner["leftup"][0]
                canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                                     rec_corner["rightdown"], rec_corner["rightup"]], 
                                    3, DEFAULT_COLOR)
                # index indicates the number of each color section
                index = 0
                for color in progress_bar_color_list:
                    rec_coordinate([progress_bar_left + index * PROGRESS_BAR_WIDTH / 10 + PROGRESS_BAR_WIDTH / 20,
                                    PROGRESS_BAR_POS[1]], PROGRESS_BAR_WIDTH / 10 - 0.5, PROGRESS_BAR_HEIGHT - 0.7)
                    canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                                         rec_corner["rightdown"], rec_corner["rightup"]], 
                                        0.03, DEFAULT_COLOR, color)
                    index += 1
    
            # Add a new treasure once the old one is consumed
            if not treasure_present:
                add_treasure() 
                
            # Collect treasure with the ball
            for treasure in ball_list:
                if treasure != ball_list[0]:
                    ball_list[0].collecting_treasure(treasure)
    
        for ball in ball_list:
            # Draw the objects (bouncing ball and treasure) in the ball_list
            ball.draw(canvas)
            # The ball is only moving in the title page or when game is on
            if title_page_display or continue_moving and not pause:
                ball.update()

        for paddle in paddle_list:
            # Draw the moving paddle in the paddle_list
            paddle.draw(canvas)
            # The paddle is only moving in the tile page or when game is on
            if title_page_display or continue_moving and not pause:
                paddle.update()
                ball_list[0].bouncing(paddle)
        
        # Display the text of the title page
        if title_page_display:
            canvas.draw_text('I', (FRAME_WIDTH * 0.12, FRAME_HEIGHT * 0.4), 100, font_color_list[0])
            canvas.draw_text('R', (FRAME_WIDTH * 0.17, FRAME_HEIGHT * 0.4), 100, font_color_list[1])
            canvas.draw_text('I', (FRAME_WIDTH * 0.25, FRAME_HEIGHT * 0.4), 100, font_color_list[2])
            canvas.draw_text('D', (FRAME_WIDTH * 0.3, FRAME_HEIGHT * 0.4), 100, font_color_list[3])
            canvas.draw_text('E', (FRAME_WIDTH * 0.385, FRAME_HEIGHT * 0.4), 100, font_color_list[4])
            canvas.draw_text('S', (FRAME_WIDTH * 0.46, FRAME_HEIGHT * 0.4), 100, font_color_list[5])
            canvas.draw_text('C', (FRAME_WIDTH * 0.52, FRAME_HEIGHT * 0.4), 100, font_color_list[6])
            canvas.draw_text('E', (FRAME_WIDTH * 0.6, FRAME_HEIGHT * 0.4), 100, font_color_list[7])
            canvas.draw_text('N', (FRAME_WIDTH * 0.67, FRAME_HEIGHT * 0.4), 100, font_color_list[8])
            canvas.draw_text('C', (FRAME_WIDTH * 0.75, FRAME_HEIGHT * 0.4), 100, font_color_list[9])
            canvas.draw_text('E', (FRAME_WIDTH * 0.83, FRAME_HEIGHT * 0.4), 100, font_color_list[10])
            canvas.draw_text('click to start', (FRAME_WIDTH * 0.33, FRAME_HEIGHT * 0.56), 40, DEFAULT_COLOR, "monospace")
        
        if helper_page_display:
            canvas.draw_text('How to Play', (FRAME_WIDTH * 0.05, FRAME_HEIGHT * 0.1), 50, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('Move the', (FRAME_WIDTH * 0.1, FRAME_HEIGHT * 0.25), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('with', (FRAME_WIDTH * 0.415, FRAME_HEIGHT * 0.25), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_image(left_arrow_img, calc_center(IMG_DICT['left_arrow']), 
                              IMG_DICT['left_arrow'], (FRAME_WIDTH * 0.57, FRAME_HEIGHT * 0.235),
                              (80, 80))
            canvas.draw_image(down_arrow_img, calc_center(IMG_DICT['down_arrow']),
                              IMG_DICT['down_arrow'], (FRAME_WIDTH * 0.66, FRAME_HEIGHT * 0.235),
                              (80, 80))
            rec_coordinate([FRAME_WIDTH * 0.75, FRAME_HEIGHT * 0.235], 80, 80)
            canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                                 rec_corner["rightdown"], rec_corner["rightup"]], 
                                0.03, 'White', 'White')
            canvas.draw_image(right_arrow_img, calc_center(IMG_DICT['right_arrow']),
                              IMG_DICT['right_arrow'], (FRAME_WIDTH * 0.75, FRAME_HEIGHT * 0.2345),
                              (77, 76))
            canvas.draw_image(up_arrow_img, calc_center(IMG_DICT['up_arrow']),
                              IMG_DICT['up_arrow'], (FRAME_WIDTH * 0.66, FRAME_HEIGHT * 0.11),
                              (100, 100))
            canvas.draw_text('to', (FRAME_WIDTH * 0.81, FRAME_HEIGHT * 0.25), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('Bounce the', (FRAME_WIDTH * 0.1, FRAME_HEIGHT * 0.4), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('and collect the', (FRAME_WIDTH * 0.43, FRAME_HEIGHT * 0.4), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('At the end of each level, you will', (FRAME_WIDTH * 0.1, FRAME_HEIGHT * 0.5), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('See a', (FRAME_WIDTH * 0.1, FRAME_HEIGHT * 0.62), 40, DEFAULT_COLOR, 'monospace')
            rec_coordinate([FRAME_WIDTH * 0.4, FRAME_HEIGHT * 0.61], KEYBOARD_WIDTH / 3, KEYBOARD_HEIGHT / 3)
            sample_keyboard_left = rec_corner["leftup"][0]
            canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                                 rec_corner["rightdown"], rec_corner["rightup"]], 
                                1.5, DEFAULT_COLOR)
            index = 0
            for color in helper_keyboard_color_list:
                rec_coordinate([sample_keyboard_left + index * KEYBOARD_WIDTH / 30 + KEYBOARD_WIDTH / 60,
                                FRAME_HEIGHT * 0.61], KEYBOARD_WIDTH / 30 - 0.33, KEYBOARD_HEIGHT / 3 - 0.5)
                canvas.draw_polygon([rec_corner["leftup"], rec_corner["leftdown"],
                                     rec_corner["rightdown"], rec_corner["rightup"]], 
                                    0.03, DEFAULT_COLOR, color)
                index += 1
            canvas.draw_text('Play it by', (FRAME_WIDTH * 0.57, FRAME_HEIGHT * 0.62), 40, DEFAULT_COLOR,'monospace')
            canvas.draw_image(pointer_img, calc_center(IMG_DICT['pointer']),
                              IMG_DICT['pointer'], (FRAME_WIDTH * 0.85, FRAME_HEIGHT * 0.6),
                              (286 / 8, 429 / 8))
            canvas.draw_text('On each key  1 color = 1 piano note', (FRAME_WIDTH * 0.1, FRAME_HEIGHT * 0.74), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('"P" = Pause the game Game is OVER', (FRAME_WIDTH * 0.1, FRAME_HEIGHT * 0.85), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('When you drop the', (FRAME_WIDTH * 0.1, FRAME_HEIGHT * 0.95), 40, DEFAULT_COLOR, 'monospace')
            canvas.draw_text('Press space to start', (FRAME_WIDTH * 0.62, FRAME_HEIGHT * 0.98), 30, DEFAULT_COLOR, 'monospace')
            
        if not title_page_display and not helper_page_display:
            # Display "Pause" at the center of the screen when the player pauses the game    
            if pause:
                canvas.draw_text('Pause', (FRAME_WIDTH * 0.4, FRAME_HEIGHT * 0.5), 80, DEFAULT_COLOR) 
                sound.pause()
                
            # Display the next level# at the center of the spring when a level is finished
            if not game_over and not continue_moving:
                canvas.draw_text('LEVEL ' + str(level_num), (FRAME_WIDTH / 3, FRAME_HEIGHT / 2.5), 80, DEFAULT_COLOR) 
                canvas.draw_text('PRESS SPACE TO CONTINUE', (FRAME_WIDTH / 4.5, FRAME_HEIGHT / 1.8), 40, DEFAULT_COLOR)
          
            # Check if game is over    
            ball_pos = ball_list[0].get_pos()
            ball_rad = ball_list[0].get_radius()
            if ball_pos[1] - ball_rad >= FRAME_HEIGHT: # game is over
                game_over = True
                level_inc = True
                canvas.draw_text("GAME OVER", (FRAME_WIDTH * 0.27, FRAME_HEIGHT / 2.33), 80, DEFAULT_COLOR)
                canvas.draw_text('PRESS SPACE TO START A NEW GAME', (FRAME_WIDTH / 7.0, FRAME_HEIGHT / 1.8), 40, DEFAULT_COLOR)
                continue_moving = False

def timer_handler():
    global time_count, font_color_list
    global treasure_num, level_num, progress_bar_color_list, level_inc, piano_display, sound, new_sound
    
    # Change the text color in the title page
    if title_page_display:
        time_count += 1
        if time_count > 1:
            time_count = 0
            font_color_list.insert(0, font_color_list[-1])
            font_color_list.pop(-1)
    # Let the ball bounce idly for two seconds after each level is finished
    else:
        time_count += 1
        if time_count > 4:
            timer.stop()
            sound.pause()
            new_sound = False
            piano_display = True
        
frame = simplegui.create_frame('Iridescence', FRAME_WIDTH, FRAME_HEIGHT)
frame.set_keydown_handler(key_start_handler)
frame.set_keyup_handler(key_stop_handler)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)

timer = simplegui.create_timer(500, timer_handler)

# Initiate the title page
start_game()

# Start the frame
frame.start()