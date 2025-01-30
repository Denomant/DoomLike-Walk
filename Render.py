import pygame
from Player import Player, is_valid_point, move_point_in_angle
from math import ceil


class Ray:
    def __init__(self, pos: tuple[float], angle):
        self.x = pos[0]
        self.y = pos[1]
        self.angle = angle

    def calculate_length(self, game_map, view_distance):
        current_point = (self.x, self.y)
        step_size = 0.01 # how preciece we want the distance
        distance = 0
        while is_valid_point(current_point, game_map) and distance <= view_distance:
            distance += step_size
            current_point = move_point_in_angle(current_point, self.angle, step_size)

        self.length = distance

    def calculate_height(self, screen_height):
        screen_distance = 0.1
        wall_actual_size = screen_height
        # when player is at (0, 0) looking at 0 degrees, a wall at distance 0.1 will take the whole screen

        if self.length <= 0:
            self.visible_height = screen_height # if wall too close - draw it on the whole bloc
        else:
            self.visible_height = (screen_distance / self.length) * wall_actual_size

    def convert_distance_to_shadow(self, view_distance):
        # distance / view_distance = x / 255
        # x = (distance * 255) / view_distance
        self.shadow = 255 - int((self.length * 255) / view_distance)

    def get_polygon_points(self, screen_height, current_bloc_x, bloc_width):
        middle_height = screen_height / 2
        half_of_visible_height = self.visible_height / 2

        top_left = (current_bloc_x, middle_height - half_of_visible_height)
        bottom_left = (current_bloc_x, middle_height + half_of_visible_height)
        top_right = (current_bloc_x + bloc_width, middle_height - half_of_visible_height)
        bottom_right = (current_bloc_x + bloc_width, middle_height + half_of_visible_height)

        return (top_left, bottom_left, bottom_right, top_right)

def draw_bloc(screen, shadow, *points):
    shadow = (shadow, shadow, shadow)
    pygame.draw.polygon(screen, shadow, points)
        

def render(screen, game_map, player: Player):
    screen_sizes = screen.get_size()
    view_distance = 5
    FOV = 120 # Field of view, how far to sides the player can see in degrees
    ray_angle_diffrence = 1
    last_ray_angle = (player.current_angle + (0.5 * FOV))
    current_ray_angle = (player.current_angle - (0.5 * FOV))
    # Angle normalization should be done only right before drawing to avoid infinite / too short loops
    
    total_draw_blocs = ceil((last_ray_angle - current_ray_angle) / ray_angle_diffrence)
    bloc_width = (screen_sizes[0] / total_draw_blocs)
    current_bloc_x = 0

    while current_ray_angle <= last_ray_angle:
        ray = Ray(player.get_pos(), current_ray_angle % 360)
        ray.calculate_length(game_map, view_distance)
        ray.calculate_height(screen_sizes[1])
        ray.convert_distance_to_shadow(view_distance)
        points = ray.get_polygon_points(screen_sizes[1], current_bloc_x, bloc_width)

        draw_bloc(screen, ray.shadow, *points)

        current_ray_angle += ray_angle_diffrence
        current_bloc_x += bloc_width