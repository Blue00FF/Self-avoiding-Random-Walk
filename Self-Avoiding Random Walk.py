import numpy as np
import matplotlib.pyplot as plt
import random

GRID_DIMENSION = 5


def check_possible_direction(current_pos):
    x = current_pos[0]
    y = current_pos[1]
    if y - 1 < 0 or grid[x][y - 1].visited == True:
        grid[x][y].options.update({"up": False})
    if y + 1 >= GRID_DIMENSION or grid[x][y + 1].visited == True:
        grid[x][y].options.update({"down": False})
    if x - 1 < 0 or grid[x - 1][y].visited == True:
        grid[x][y].options.update({"left": False})
    if x + 1 >= GRID_DIMENSION or grid[x + 1][y].visited == True:
        grid[x][y].options.update({"right": False})


class Spot:
    def __init__(self):
        self.options = {"up": True, "down": True, "left": True, "right": True}
        self.allowed = []
        self.visited = False
    
    def generate_allowed(self):
        self.allowed = []
        for (key, value) in self.options.items():
            if value:
                self.allowed.append(key)


grid = []
for i in range(GRID_DIMENSION):
    grid.append([])
    for j in range(GRID_DIMENSION):
        grid[i].append(Spot())

grid = np.array(grid)
current_position = np.array([0, 0])
history = []

while True:
    history.append(current_position.copy())
    current_grid_pos = grid[current_position[0]][current_position[1]]
    current_grid_pos.visited = True
    check_possible_direction(current_position)
    current_grid_pos.generate_allowed()
    if len(current_grid_pos.allowed) > 0:
        match random.choice(current_grid_pos.allowed):
            case "up":
                current_position += np.array([0, -1])
            case "down":
                current_position += np.array([0, 1])
            case "left":
                current_position += np.array([-1, 0])
            case "right":
                current_position += np.array([1, 0])
    else:
        print("Stuck!")
        break
        
history = np.array(history)

x = history[:, 0]
y = history[:, 1]

plt.plot(x, y)
plt.plot(x, y, "bo")
plt.plot(x[0], y[0], "go")
plt.plot(x[-1], y[-1], "ro")
plt.show()

