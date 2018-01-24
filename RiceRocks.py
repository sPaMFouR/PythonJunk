# Week 8 Project - RiceRocks

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

# Global Variables

WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
game_started = False
rock_group = set()
missile_group = set()
explosion_group = set()

# Image Information Class

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# Debris Images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png, debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# Nebula Images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# Splash Image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# Ship Image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# Missile Image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_image = [missile_image1, missile_image2, missile_image3]
# Asteroid Images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
asteroid_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
asteroid_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")
asteroid_image = [asteroid_image1, asteroid_image2, asteroid_image3]

# Animated Explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# Sounds
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# Helper Functions

def angle_to_vector(ang):
    """Finds Perpendicular Components Of The Vector"""
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    """Finds Distance Between Two Points"""
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def process_sprite_group(group, canvas):
    """Draws & Updates A Sprite Group"""
    for each_object in group:
        each_object.draw(canvas)
        each_object.update()
        if each_object.update():
            group.remove(each_object)

def group_collide(group, other_object):
    """Checks For Collision Of Objects Within The Group With The Other Object(Rock-Ship Collision)"""
    global explosion_group
    remove_set = set()

    for each_object in set(group):
        if each_object.collide(other_object):
            group.remove(each_object)
            remove_set.add(each_object)
            explosion_group.add(each_object)
            each_object.explosion()
            return True

    if len(remove_set) == 0:
        return False
    else:
        return True

    group.difference_update(remove_set)

def group_group_collide(group1, group2):
    """Checks For Collision Of Objects Within Group1 With The Objects Within Group 2(Rock-Missile Collision)"""
    global score
    for each_object in set(group2):
        if group_collide(group1, each_object):
            score += 10
            group2.remove(each_object)
    return score

def empty_group(group):
    """Deletes All The Entries In A Group(Required For Game Restart)"""
    for each_object in set(group):
        group.remove(each_object)


# SpaceShip Class

class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.accn = [0, 0]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self,canvas):
        if not self.thrust:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image,[self.image_center[0] + 90, self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # Update Angle
        self.angle += self.angle_vel

        # Update Velocity
        if self.thrust:
            self.accn = angle_to_vector(self.angle)
            self.vel[0] += self.accn[0] * 0.4
            self.vel[1] += self.accn[1] * 0.4

        self.vel[0] *= 0.98
        self.vel[1] *= 0.98


        # Update Position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] + self.radius > WIDTH or self.pos[0] - self.radius < 0:
            self.pos[0] %= WIDTH
        if self.pos[1] + self.radius > HEIGHT or self.pos[1] - self.radius < 0:
            self.pos[1] %= HEIGHT

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def increment_angle_vel(self, ang_vel):
        self.angle_vel = ang_vel
        return self.angle_vel

    def decrement_angle_vel(self, ang_vel):
        self.angle_vel = -ang_vel
        return self.angle_vel

    def thrust_status(self, status):
        self.thrust = status
        if status:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
        return self.thrust

    def shoot(self):
        global missile_group
        if game_started:
            if not self.thrust:
                self.accn = angle_to_vector(self.angle)

            missile_pos = [self.pos[0] + self.radius * self.accn[0], self.pos[1] + self.radius * self.accn[1]]
            missile_vel = [self.vel[0] + 8 * self.accn[0], self.vel[1] + 8 * self.accn[1]]

            a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, random.choice(missile_image), missile_info, missile_sound)
            missile_sound.play()
            missile_group.add(a_missile)

# Sprite Class

class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()

    def draw(self, canvas):
        global time1
        if not self.animated:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            time1 += 1
            canvas.draw_image(explosion_image, [explosion_info.get_center()[0] + (2 * time1 % explosion_info.get_lifespan()) * 128, explosion_info.get_center()[1]], explosion_info.get_size(), self.pos, explosion_info.get_size())

            if time % explosion_info.get_lifespan() == 0:
                explosion_group.remove(self)

    def update(self):
        # Update Angle
        self.angle += self.angle_vel

        # Update Position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] + self.radius > WIDTH or self.pos[0] - self.radius < 0:
            self.pos[0] %= WIDTH
        if self.pos[1] + self.radius > HEIGHT or self.pos[1] - self.radius < 0:
            self.pos[1] %= HEIGHT

        # Update Age
        self.age += 1
        if self.age <= self.lifespan:
            return False
        else:
            return True

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) <= (self.radius + other_object.get_radius()) :
            return True
        else:
            return False

    def explosion(self):
        global time1
        explosion_sound.rewind()
        explosion_sound.play()
        self.animated = True
        time1 = 0

# Mouseclick Handler For Starting The Game By Clicking On The Splash Screen

def click(pos):
    global game_started
    splash_center = [WIDTH / 2, HEIGHT / 2]
    splash_size = splash_info.get_size()

    inside_width = (splash_center[0] - splash_size[0] / 2) < pos[0] < (splash_center[0] + splash_size[0] / 2)
    inside_height = (splash_center[1] - splash_size[1] / 2) < pos[1] < (splash_center[1] + splash_size[1] / 2)

    if (not game_started) and inside_width and inside_height:
        game_started = True

# Draw Handler

def draw(canvas):
    global time, lives, score, game_started

    # Animate Background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # Update Score And Lives Left
    canvas.draw_text("Lives", [WIDTH / 10, HEIGHT / 10], 25, "White")
    canvas.draw_text(str(lives), [WIDTH / 10, HEIGHT / 7], 25, "White")
    canvas.draw_text("Score", [8 * WIDTH / 10, HEIGHT / 10], 25, "White")
    canvas.draw_text(str(score), [8 * WIDTH / 10, HEIGHT / 7], 25, "White")

    # Draw & Update Ship And Sprites
    my_ship.draw(canvas)
    my_ship.update()
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)

    # Update Lives When Ship Collides With A Rock
    if group_collide(rock_group, my_ship):
        lives -= 1

    # Update Score When A Missile Hits A Rock
    group_group_collide(rock_group, missile_group)

    # Update Parameters To Restart The Game When No Lives Are Left
    if lives == 0:
        game_started = False
        lives = 3
        score = 0
        empty_group(rock_group)
        empty_group(missile_group)
        empty_group(explosion_group)

    # Draw Splash Screen When The Game Is Not Started
    if not game_started:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(),
                          [WIDTH / 2,  HEIGHT / 2], splash_info.get_size())

# Key Handlers

def keydown(key):
    # Update Thrust Status
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust_status(True)

    # Update Angular Velocity
    if key==simplegui.KEY_MAP["left"]:
        my_ship.decrement_angle_vel(0.1)
    elif key==simplegui.KEY_MAP["right"]:
        my_ship.increment_angle_vel(0.1)

    # Call Ship.Shoot Method For Shooting A Missile
    if key==simplegui.KEY_MAP["space"]:
        my_ship.shoot()

def keyup(key):
    # Update Thrust Status
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust_status(False)

    # Update Anglular Velocity
    if key==simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = 0
    elif key==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0

# Initialize Timer Handler That Spawns A Group Of Rocks

def rock_spawner():
    global rock_group

    # Generate Rocks With Random Components
    if game_started and len(rock_group) < 12:
        rock_pos = [random.randint(asteroid_info.get_radius(), WIDTH - asteroid_info.get_radius()), random.randint(asteroid_info.get_radius(), HEIGHT - asteroid_info.get_radius())]
        rock_vel = ((score + 100) / 100 )*[random.randint(0, 10) * random.choice([1, -1]) / 5, random.randint(0, 10) * random.choice([1, -1]) / 5]
        rock_angvel = random.random() * random.choice([0.1, -0.1])
        a_rock = Sprite(rock_pos, rock_vel, 0, rock_angvel, random.choice(asteroid_image), asteroid_info)

        # Check Whether Randomly Generated Rock Is Spawning Nearby The Ship(If Not - Add To Rock Group)
        if not (my_ship.get_position()[0] - my_ship.get_radius() < rock_pos[0] < my_ship.get_position()[0] + my_ship.get_radius()) and  not (my_ship.get_position()[1] - my_ship.get_radius() < rock_pos[1] < my_ship.get_position()[1] + my_ship.get_radius()):
            rock_group.add(a_rock)

        # Play Game Soundtrack
        soundtrack.rewind()
        soundtrack.play()

# Initialize Frame

frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# Initialize Ship

my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

# Event Handlers

frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Get Things Started

timer.start()
frame.start()


