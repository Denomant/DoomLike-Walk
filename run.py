import pygame
from sys import exit
from Player import Player
from Render import render

pygame.init()
INFO = pygame.display.Info()

# Changeable
WIDTH, HEIGHT = INFO.current_w, INFO.current_h
Max_FPS = 60
player = Player((5.5, 1.5), 0)
game_map = [["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", " ", " ", "#", " ", " ", "#"],
            ["#", " ", " ", " ", "#", "#", " ", "#"],
            ["#", " ", " ", " ", "#", " ", " ", "#"],
            ["#", "#", " ", "#", "#", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", "#"],
            ["#", "#", " ", "#", " ", "#", " ", "#"],
            ["#", "#", " ", "#", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"]]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS_clock = pygame.time.Clock()
movement_timer = pygame.USEREVENT + 1
pygame.time.set_timer(movement_timer, 15) # Trigger movement every 25 milliseconds
rotation_degree = 0
move_speed = 0
game_loop = True

# Exit button
exit_rect = pygame.Rect(WIDTH - 50, 10, 40, 40)

def apply_key(key, reverse=False):
    global move_speed, rotation_degree
    factor = -1 if reverse else +1
    match event.key:
        case pygame.K_LEFT:
            rotation_degree += 2 * factor
        case pygame.K_RIGHT:
            rotation_degree -= 2 * factor
        case pygame.K_UP:
            move_speed += 0.035 * factor
        case pygame.K_DOWN:
            move_speed -= 0.035 * factor


while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # exit button handeling
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(event.pos):
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
    
    # Draw exit "X" button
    pygame.draw.line(screen, "White", exit_rect.topleft, exit_rect.bottomright, 2)
    pygame.draw.line(screen, "White", exit_rect.topright, exit_rect.bottomleft, 2)

    FPS_clock.tick(Max_FPS)
    pygame.display.update()
