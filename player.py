from math import sin, cos, radians


def move_point_in_angle(point: tuple, angle, distance):
    delta_x = distance * cos(radians(angle))
    delta_y = distance * -sin(radians(angle))
    return point[0] + delta_x, point[1] + delta_y

def is_valid_point(point, game_map):
    x = point[0]
    y = point[1] 
    if (0 <= x < len(game_map[0])) and (0 <= y < len(game_map)): # if new point is in the bounderies
        return game_map[int(y)][int(x)] != "#"                   # and is not a wall
    return False


class Player:
    def __init__(self, starting_pos: tuple[float], starting_angle: float):
        self.y, self.x = starting_pos
        self.current_angle = starting_angle % 360

    def turn_counterclockwise(self, degrees):
        self.current_angle = (self.current_angle + degrees) % 360

    def go_forward(self, units, game_map):
        new_x, new_y = move_point_in_angle(self.get_pos(), self.current_angle, units)

        if is_valid_point((new_x, new_y), game_map):
            self.x = new_x
            self.y = new_y

    def get_pos(self):
        return self.x, self.y

