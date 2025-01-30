import pygame
from sys import exit
from Player import Player
from Render import render

# Changeable
WIDTH, HEIGHT = 1920, 1080
Max_FPS = 60
player = Player((1.5, 1.5), -90)
game_map = [["#", "#", "#", "#", "#"],
            ["#", " ", "#", " ", "#"],
            ["#", " ", "#", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#"]]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS_clock = pygame.time.Clock()
movement_timer = pygame.USEREVENT + 1
pygame.time.set_timer(movement_timer, 15) # Trigger movement every 25 milliseconds
rotation_degree = 0
move_speed = 0
game_loop = True

def apply_key(key, reverse=False):
    global move_speed, rotation_degree
    factor = -1 if reverse else +1
    match event.key:
        case pygame.K_LEFT:
            rotation_degree -= 2 * factor
        case pygame.K_RIGHT:
            rotation_degree += 2 * factor
        case pygame.K_UP:
            move_speed += 0.035 * factor
        case pygame.K_DOWN:
            move_speed -= 0.035 * factor


while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type ==  pygame.KEYDOWN:
            apply_key(event.key)

        if event.type == pygame.KEYUP:
            apply_key(event.key, reverse=True)

        if event.type == movement_timer:
            player.go_forward(move_speed,game_map)
            player.turn_counterclockwise(rotation_degree)

    screen.fill("Black") # clear previous frame
    render(screen, game_map, player)
    
    FPS_clock.tick(Max_FPS)
    pygame.display.update()
