import pygame
import winsound

pygame.init()

class player:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        self.point = 0
        self.morti = 0
        self.speed = 0.1
        self.base_speed = 0.1
        self.win = 0

class area:
    def __init__(self, width, height, dimin, x, y, color):
        self.width = width
        self.height = height
        self.dimin = dimin
        self.x = x
        self.y = y
        self.color = color

fascio = player(0, 100, "X")
comuni = player(250, 250, "O")

fascio_zone = area(200, 200, "comuni", 0, 300, "black")
comuni_zone = area(200, 200, "fascio", 300, 0, "red")

player1_color = [0, 0, 100]
player2_color = [100, 0, 0]
max_value = 255
increment = 30

pop_count = 0
timer = 0
clock = pygame.time.Clock()
seconds = 0

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape from the comunism!")
background_color = (255, 255, 255)
text_color = (0, 0, 0)

game_over = False
running = True
sound_player = False
win_assigned = False
sound_step = False
start_sound = False
fascio_in_zone = False

speed_flags = {10: False, 20: False, 30: False, 40: False, 50: False}
speed_values = {10:0.2, 20:0.3, 30:0.5, 40:0.7, 50:1.0}

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 40)
winner_text = "Complimenti fascio, sei scappato!"
winning_stat = font.render(f"Fascio win: {fascio.win}, Comuni win: {comuni.win}", True, text_color)
text_timer = font.render(f"Timer: {seconds}", True, text_color)
text_point = font.render(f"Fascio: 0/3, Comuni: 0/3", True, text_color)
button_color = (0, 200, 0)

def winner_fascio():
    winsound.PlaySound("winner_player.wav", winsound.SND_ASYNC)

def winner_comuni():
    winsound.PlaySound("winner_enemy.wav", winsound.SND_ASYNC)

def in_the_zone():
    winsound.PlaySound("dentro.wav", winsound.SND_ASYNC)

def increment_speed_sound():
    winsound.PlaySound("pop.wav", winsound.SND_ASYNC)
    player1_color[2] = min(player1_color[2] + increment, max_value)  
    player2_color[0] = min(player2_color[0] + increment, max_value) 

def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, button_color, (x, y, w, h))
    txt = font.render(text, True, (255, 255, 255))
    screen.blit(txt, (x + 10, y + 5))
    return pygame.Rect(x, y, w, h)

def reset_game_complete():
    global seconds, fascio, comuni, game_over, sound_player, text_point, win_assigned, player1_color, player2_color, speed_flags, speed_values
    seconds = 0
    fascio.x, fascio.y = 0, 100
    comuni.x, comuni.y = 250, 250
    game_over = False
    sound_player = False
    fascio.point = 0
    comuni.point = 0
    player1_color = [0, 0, 100]
    player2_color = [100, 0, 0]
    speed_flags = {10: False, 20: False, 30: False, 40: False, 50: False}
    speed_values = {10:0.2, 20:0.3, 30:0.5, 40:0.7, 50:1.0}
    fascio.morti = 0
    comuni.morti = 0
    comuni.speed = 0.1
    fascio.speed = 0.1
    fascio.base_speed = 0.1
    comuni.base_speed = 0.1
    win_assigned = False
    text_point = font.render(f"Fascio: 0/3, Comuni: 0/3", True, text_color)
    winsound.PlaySound(None, winsound.SND_PURGE)

def reset_game():
    global seconds, fascio, comuni, game_over, sound_player, win_assigned, player1_color, player2_color, speed_flags, speed_values
    seconds = 0
    player1_color = [0, 0, 100]
    player2_color = [100, 0, 0]
    fascio.x, fascio.y = 0, 100
    comuni.x, comuni.y = 250, 250
    speed_flags = {10: False, 20: False, 30: False, 40: False, 50: False}
    speed_values = {10:0.2, 20:0.3, 30:0.5, 40:0.7, 50:1.0}
    game_over = False
    sound_player = False
    comuni.speed = 0.1
    fascio.speed = 0.1
    fascio.base_speed = 0.1
    comuni.base_speed = 0.1
    win_assigned = False
    winsound.PlaySound(None, winsound.SND_PURGE)

area1 = pygame.image.load("area1.png").convert_alpha()
area1 = pygame.transform.scale(area1, (fascio_zone.width, fascio_zone.height))

area2 = pygame.image.load("area2.png").convert_alpha()
area2 = pygame.transform.scale(area2, (comuni_zone.width, comuni_zone.height))

background_img = pygame.image.load("back.jpg").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

player1 = pygame.image.load("player1.png").convert_alpha()
player1 = pygame.transform.scale(player1, (40, 40))

player2 = pygame.image.load("player2.png").convert_alpha()
player2 = pygame.transform.scale(player2, (40, 40))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    screen.fill(background_color)
    screen.blit(background_img, (0, 0))

    if game_over == False:
        comuni_space = screen.blit(area2, (comuni_zone.x, comuni_zone.y))
        fascio_space = screen.blit(area1, (fascio_zone.x, fascio_zone.y))
        comuni_rect = screen.blit(player2, (comuni.x, comuni.y))
        fascio_rect = screen.blit(player1, (fascio.x, fascio.y))
        screen.blit(text_timer, (10, 10))
        screen.blit(text_point, (10, 30))
        screen.blit(winning_stat, (10, 50))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and fascio.y > 0:
            fascio.y -= fascio.speed
        if keys[pygame.K_s] and fascio.y < 460:
            fascio.y += fascio.speed
        if keys[pygame.K_a] and fascio.x > 0:
            fascio.x -= fascio.speed
        if keys[pygame.K_d] and fascio.x < 460:
            fascio.x += fascio.speed

        if keys[pygame.K_UP] and comuni.y > 0:
            comuni.y -= comuni.speed
        if keys[pygame.K_DOWN] and comuni.y < 460:
            comuni.y += comuni.speed
        if keys[pygame.K_LEFT] and comuni.x > 0:
            comuni.x -= comuni.speed
        if keys[pygame.K_RIGHT] and comuni.x < 460:
            comuni.x += comuni.speed

        if fascio_rect.colliderect(comuni_rect):
            comuni.point += 1
            fascio.morti += 1
            seconds = 0
            fascio.x = 0
            fascio.y = 100
            comuni.x = 250
            comuni.y = 250
            text_point = font.render(f"Fascio: {fascio.point}/3, Comuni: {comuni.point}/3", True, text_color)
            winner_text = "Comunism win..."
            game_over = True
            screen.blit(text_point, (10, 30))

        current_time = pygame.time.get_ticks()
        fascio.speed = fascio.base_speed
        comuni.speed = comuni.base_speed

        if fascio_rect.colliderect(comuni_space):
            fascio.speed = 0.1
            if fascio_in_zone == False:
                in_the_zone()
                fascio_in_zone = True

        if comuni_rect.colliderect(fascio_space):
            comuni.speed = 0.1
            if start_sound == False:
                in_the_zone()
                start_sound = True

        if not comuni_rect.colliderect(fascio_space):
            start_sound = False

        if not fascio_rect.colliderect(comuni_space):
            fascio_in_zone = False

        if seconds >= 60:
            fascio.point += 1
            comuni.morti += 1
            seconds = 0
            fascio.x = 0
            fascio.y = 100
            comuni.x = 250
            comuni.y = 250
            text_point = font.render(f"Fascio: {fascio.point}/3, Comuni: {comuni.point}/3", True, text_color)
            winner_text = "Fascio WIN!!!!"
            game_over = True
            screen.blit(text_point, (10, 30))
        elif current_time - timer >= 1000:
            timer = current_time
            seconds += 1
            for sec in speed_flags:
                if seconds >= sec and not speed_flags[sec]:
                    fascio.base_speed = speed_values[sec]
                    comuni.base_speed = speed_values[sec]
                    try:
                        increment_speed_sound()
                    except RuntimeError:
                        pass
                    speed_flags[sec] = True
            text_timer = font.render(f"Timer: {seconds}", True, text_color)
            screen.blit(text_timer, (10, 10))
            winning_stat = font.render(f"Fascio win: {fascio.win}, Comuni win: {comuni.win}", True, text_color)
            screen.blit(winning_stat, (10, 50))

    else:
        if sound_player == False:
            if winner_text == "Comunism win...":
                winner_comuni()
            else:
                winner_fascio()
            sound_player = True
        if (comuni.point >= 3 or fascio.point >= 3) and win_assigned == False:
            if comuni.point >= 3:
                comuni.win += 1
                winner_text = "Peccato, ha vinto il comunismo..."
            if fascio.point >= 3:
                fascio.win += 1
                winner_text = "FASCIO WIN THE GAME!!!!!!"

            win_assigned = True

        text_winner = big_font.render(winner_text, True, (0, 0, 0))
        screen.blit(text_winner, (WIDTH//2 - text_winner.get_width()//2, HEIGHT//2 - 50))
        button_rect = draw_button("Restart Game", WIDTH//2 - 75, HEIGHT//2 + 20, 150, 50)

        if mouse_click[0] and button_rect.collidepoint(mouse_pos):
            if comuni.point >= 3 or fascio.point >= 3:
                reset_game_complete()
            else:
                reset_game()

    pygame.display.flip()

pygame.quit()