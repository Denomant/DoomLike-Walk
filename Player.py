from math import sin, cos, radians


class Player:
    def __init__(self, starting_pos: tuple[float], starting_angle: float):
        self.y, self.x = starting_pos
        self.current_angle = starting_angle % 360

    def turn_counterclockwise(self, degrees):
        self.current_angle = (self.current_angle + degrees) % 360

    def go_forward(self, units, game_map):
        delta_x = units * cos(radians(self.current_angle))
        delta_y = units * -sin(radians(self.current_angle))

        new_x = self.x + delta_x # optimization so I dont have to calculate it 8 times
        new_y = self.y + delta_y 

        if (0 <= new_y < len(game_map)) and (0 <= new_x< len(game_map[0])): # if new point is in the bounderies
            if game_map[int(new_y)][int(new_x)] != "#":                     # and is not a wall, then move
                self.x = new_x
                self.y = new_y