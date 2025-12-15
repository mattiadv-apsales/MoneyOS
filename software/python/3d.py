from ursina import *
from math import sin, cos, radians
import random

app = Ursina()

mouse.locked = True
window.fullscreen = True

sc = 1000

# Terreno
ground = Entity(
    model='cube',
    scale=(sc, sc, sc),
    y=-(sc / 2),
    texture='white_cube',
    texture_scale=(sc, sc),
    collider='box'
)

# Player
player = Entity(model='cube', color=color.orange, scale=(1,2,1), y=1, collider='box')

# Timer
timer_text = Text(text='0', position=(-0.85, 0.45), scale=2)
timer = 0

# Lista nemici
enemies = []

camera.parent = player
camera.position = (0, 4, -10)
camera.rotation_x = 15

# Variabili di movimento
speed = 5
vel_y = 0
gravity = 9.8
jump_force = 10
on_ground = True
mouse_sensitive = 40

# Spawn nemici ogni secondo
def spawn_enemy():
    min_dist = 5
    max_dist = 10

    angle = random.uniform(0, 360)
    distance = random.uniform(min_dist, max_dist)

    x = player.x + distance * cos(radians(angle))
    z = player.z + distance * sin(radians(angle))
    enemy_speed = 3  # Velocità casuale, per bilanciare probabilità di vincita/perdita
    enemy = Entity(model='cube', color=color.red, scale=(1,2,1), y=1, x=x, z=z, collider='box')
    enemy.enemy_speed = enemy_speed
    enemies.append(enemy)

# Timer per spawn
spawn_timer = 0

def update():
    global speed, vel_y, jump_force, on_ground, gravity, mouse_sensitive, timer, spawn_timer

    forward = Vec3(sin(radians(player.rotation_y)), 0, cos(radians(player.rotation_y)))
    right = Vec3(cos(radians(player.rotation_y)), 0, -sin(radians(player.rotation_y)))

    # Aggiorna timer
    timer += time.dt
    spawn_timer += time.dt
    seconds = int(timer)
    timer_text.text = f'{seconds}'

    # Spawn nemico ogni secondo
    if spawn_timer >= 1:
        spawn_enemy()
        spawn_timer = 0

    # Movimento player
    move = Vec3(0,0,0)
    if held_keys['w']:
        move += forward
    if held_keys['s']:
        move -= forward
    if held_keys['a']:
        move -= right
    if held_keys['d']:
        move += right
    if move != Vec3(0,0,0):
        player.position += move.normalized() * speed * time.dt
    if held_keys['space'] and on_ground:
        on_ground = False
        vel_y = jump_force

    # Nemici inseguono player
    for enemy in enemies:
        direction = Vec3(player.x - enemy.x, 0, player.z - enemy.z)
        if direction != Vec3(0,0,0):
            enemy.position += direction.normalized() * enemy.enemy_speed * time.dt

        # Collisione
        if player.intersects(enemy).hit:
            print(f"You lose after {seconds}s!")
            application.quit()

    # Gravità
    vel_y -= gravity * time.dt
    player.y += vel_y * time.dt
    if player.y <= 1:
        player.y = 1
        on_ground = True
        vel_y = 0

    # Rotazione camera
    player.rotation_y += mouse.velocity[0] * mouse_sensitive
    camera.rotation_x -= mouse.velocity[1] * mouse_sensitive
    camera.rotation_x = clamp(camera.rotation_x, -45, 45)

    # Vincita dopo 60 secondi
    if seconds >= 60:
        print("YOU WIN THE GAME")
        application.quit()

def input(key):
    if key == "escape":
        application.quit()

app.run()