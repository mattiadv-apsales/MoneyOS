import pygame
import random

pygame.init()

class player:
    def __init__(self, color):
        self.x = 0
        self.y = 480
        self.height = 20
        self.width = 20
        self.color = color
        self.vel_y = 0
        self.gravity = 0.5
        self.jump_force = -10
        self.on_ground = True
        self.morti = 0
        self.punti = 0

speedss = 5

class object:
    def __init__(self, width, height, color, y):
        self.width = width
        self.height = height
        self.color = color
        self.speed = speedss
        self.x = 500
        self.y = y

class air_object:
    def __init__(self, width, height, color, y):
        self.width = width
        self.height = height
        self.color = color
        self.speed = speedss
        self.x = 500
        self.y = y

p1 = player((0, 0, 255))
p2 = player((255, 0, 0))
ob = object(50, 50, (0, 255, 0), 450)
vl = air_object(50, 100, (0, 200, 0), 380)
current_obstacle = None
game_over = False
tot_death = p1.morti + p2.morti
tot_point = p1.punti + p2.punti

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GG THE GAME")
GROUND_Y = 480
STAND_H = 20
CROUCH_H = 10

font = pygame.font.SysFont(None, 30)

bg = (255, 255, 255)

running = True
clock = pygame.time.Clock()

def reset_game():
    global tot_point, tot_death, current_obstacle, game_over, ob, vl, speedss
    tot_point = 0
    tot_death = 0
    p1.morti = 0
    p2.morti = 0
    p1.punti = 0
    p2.punti = 0
    speedss = 5
    p1.x, p1.y = 0, 480
    p2.x, p2.y = 0, 480
    p1.height = STAND_H
    p2.height = STAND_H
    p1.vel_y = 0
    p2.vel_y = 0
    p1.on_ground = True
    p2.on_ground = True
    current_obstacle = None
    ob = object(50, 50, (0, 255, 0), 450)
    vl = air_object(50, 100, (0, 200, 0), 380)
    game_over = False

def spawn_obstacle():
    choice = random.choice(['ground', 'air'])
    w = random.randint(30, 50)
    if choice == 'ground':
        y = GROUND_Y - w / 2 + 1
        return object(w, w, (0, 255, 0), y)
    else:
        h = random.randint(100, 180)
        y = GROUND_Y - h + 5
        return air_object(w, h, (0, 200, 0), y)

while running:
    screen.fill(bg)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_rect.collidepoint(event.pos):
                reset_game()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and p1.on_ground:
                p1.vel_y = p1.jump_force
                p1.on_ground = False
            
            if event.key == pygame.K_UP and p2.on_ground:
                p2.vel_y = p2.jump_force
                p2.on_ground = False
    if game_over == False:
        keys = pygame.key.get_pressed()

        p1.vel_y += p1.gravity
        p1.y += p1.vel_y

        p2.vel_y += p2.gravity
        p2.y += p2.vel_y

        if p2.y >= 480:
            p2.y = 480
            p2.vel_y = 0
            p2.on_ground = True

        if p1.y >= 480:
            p1.y = 480
            p1.vel_y = 0
            p1.on_ground = True

        if keys[pygame.K_d] and p1.x < 480:
            p1.x += 5
        if keys[pygame.K_a] and p1.x > 0:
            p1.x -= 5
        
        if keys[pygame.K_s] and p1.on_ground:
            p1.height = CROUCH_H
            p1.y = GROUND_Y + (STAND_H - CROUCH_H)
        else:
            if p1.on_ground:
                p1.height = STAND_H
                p1.y = GROUND_Y

        if keys[pygame.K_DOWN] and p2.on_ground:
            p2.height = CROUCH_H
            p2.y = GROUND_Y + (STAND_H - CROUCH_H)
        else:
            if p2.on_ground:
                p2.height = STAND_H
                p2.y = GROUND_Y

        if keys[pygame.K_RIGHT] and p2.x < 480:
            p2.x += 5
        if keys[pygame.K_LEFT] and p2.x > 0:
            p2.x -= 5

        if ob.x >= -(ob.width):
            ob.x -= ob.speed
        else:
            ob.x = 500

        if vl.x >= -(vl.width):
            vl.x -= vl.speed
        else:
            vl.x = 500

        if current_obstacle is None:
            current_obstacle = spawn_obstacle()

        current_obstacle.x -= current_obstacle.speed

        if current_obstacle.x < -current_obstacle.width:
            current_obstacle = None

        if current_obstacle:
            cc = pygame.draw.rect(screen, current_obstacle.color, 
                        (current_obstacle.x, current_obstacle.y, current_obstacle.width, current_obstacle.height))


        p1_rect = pygame.draw.rect(screen, p1.color, (p1.x, p1.y, p1.width, p1.height))
        p2_rect = pygame.draw.rect(screen, p2.color, (p2.x, p2.y, p2.width, p2.height))
        death_count = font.render(f"morti - P1: {p1.morti} - P2: {p2.morti}", True, (0, 0, 0))
        screen.blit(death_count, (10, 10))
        total_death = font.render(f"Morti totali: {tot_death}", True, (0, 0, 0))
        screen.blit(total_death, (10, 50))
        total_points = font.render(f"Punti totali: {tot_point}", True, (0, 0, 0))
        screen.blit(total_points, (10, 70))

        if tot_death >= 30 or tot_point >= 100:
            game_over = True

    tot_death = p1.morti + p2.morti
    tot_point = p1.punti + p2.punti

    if game_over:
        txt = ""
        if tot_death >= 30:
            txt = "Avete perso!"
        if tot_point >= 100:
            txt = "Avete vinto!"

        screen.fill(bg)
        
        # Testo principale
        lose = font.render(txt, True, (0, 0, 0))
        lose_rect = lose.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        screen.blit(lose, lose_rect)
        
        # Punti totali
        total_points = font.render(f"Punti totali: {tot_point}", True, (0, 0, 0))
        points_rect = total_points.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        screen.blit(total_points, points_rect)
        
        # Morti totali
        deaths_total = font.render(f"Morti totali: {tot_death}", True, (0, 0, 0))
        deaths_total_rect = deaths_total.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(deaths_total, deaths_total_rect)
        
        # Morti dei singoli giocatori
        deaths_p1 = font.render(f"Morti P1: {p1.morti}", True, (0, 0, 0))
        deaths_p1_rect = deaths_p1.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        screen.blit(deaths_p1, deaths_p1_rect)
        
        deaths_p2 = font.render(f"Morti P2: {p2.morti}", True, (0, 0, 0))
        deaths_p2_rect = deaths_p2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(deaths_p2, deaths_p2_rect)

        # Pulsante reset
        button_text = font.render("Reset", True, (255, 255, 255))
        button_width, button_height = 150, 50
        button_x = WIDTH // 2 - button_width // 2
        button_y = HEIGHT // 2 + 140
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, (0, 0, 255), button_rect)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        # Controllo click
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] and button_rect.collidepoint(mouse_pos):
            reset_game()

    if p1_rect.colliderect(cc):
        current_obstacle = None
        p1.morti += 1
    elif p2_rect.colliderect(cc):
        current_obstacle = None
        p2.morti += 1
    elif current_obstacle == None:
        p1.punti += 1

    if (p1.punti >= 10 or p1.morti >= 10) and (p1.punti <= 20 or p1.morti <= 20):
        speedss = 6

    if (p1.punti >= 21 or p1.morti >= 21) and (p1.punti <= 30 or p1.morti <= 30):
        speedss = 7

    if (p1.punti >= 31 or p1.morti >= 31) and (p1.punti <= 40 or p1.morti <= 40):
        speedss = 8

    if (p1.punti >= 41 or p1.morti >= 41) and (p1.punti <= 50 or p1.morti <= 50):
        speedss = 9

    if p1.punti >= 51 or p1.morti >= 51:
        speedss = 10
    
    pygame.display.flip()

pygame.quit()