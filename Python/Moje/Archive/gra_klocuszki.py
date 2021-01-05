import pygame
import sys
import random

#initialize
pygame.init()

#clock & score
clock = pygame.time.Clock()
score = 0
#myfont = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 35)

#colours
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

#creating a screen
height = 600
width = 800
screen = pygame.display.set_mode((width, height))

#player
player_size = 50
player_position = [width/2, height - 2*player_size]

#enemy
enemy_size = 50
enemy_position = [random.randint(0,width - enemy_size), 0]
speed = 10
enemy_list = [enemy_position]

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (p_x <= e_x and p_x > (e_x + player_size)) or (p_x >= e_x and p_x < (e_x + player_size)):
        if (p_y <= e_y and p_x > (e_y + player_size)) or (p_y >= e_y and p_y < (e_y + player_size)):
            return True
    return False

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay > 0.8:
        enemy_position = [random.randint(0, width - enemy_size), 0]
        enemy_list.append(enemy_position)

def draw_enemies(enemy_list):
    for enemy_position in enemy_list:
        pygame.draw.rect(screen, blue, (enemy_position[0], enemy_position[1], player_size, player_size))

def update_enemy_positions(enemy_list, speed):
    for idx, enemy_position in enumerate(enemy_list):
        if enemy_position[1] >= 0 and enemy_position[1] < height:
            enemy_position[1] += speed
        else:
            enemy_list.pop(idx)
            return True

def collision_check(enemy_list, player_position):
    for enemy_position in enemy_list:
        if detect_collision(player_position, enemy_position):
            return True


gameover = False
while not gameover:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event)

            x = player_position [0]
            y = player_position [1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_position = [x,y]
            pygame.display.update()


    screen.fill (black)
    if collision_check(enemy_list, player_position):
        gameover = True
        break

    if update_enemy_positions(enemy_list, speed):
        score += 1

    speed = score/5 + 5

    text = "Score" + str(score)
    label = myfont.render(text, 1, white)
    screen.blit(label, (width - 200, height - 40))

    drop_enemies(enemy_list)
    draw_enemies(enemy_list)
    pygame.draw.rect(screen, red, (player_position[0],player_position[1], player_size, player_size) )
    #surface, colour, rect (left pos, top pos, width, height), optional outline
    clock.tick(30)
    pygame.display.update()

