from typing import Collection, Dict, List

import numpy as np
import matplotlib.pyplot as plt
import random

# Side dimension of the grid we are going to perform our self-avoiding walk.
from numpy.typing import ArrayLike

GRID_DIMENSION: int = 5


def check_possible_direction(current_pos: Collection[int]) -> None:
    """
    Function Taking the numpy array expressing the current position as input
    and modifying the corresponding Spot object on the grid to reflect the
    possible directions we can proceed on.
    """
    x: int = current_pos[0]
    y: int = current_pos[1]
    # Disallow the up direction if we are on the upper edge of the grid or
    # the square above the current one has already been visited.
    if y - 1 < 0 or grid[x][y - 1].visited == True:
        grid[x][y].options.update({"up": False})
    # Disallow the down direction if we are on the lower edge of the grid or
    # the square below the current one has already been visited.
    if y + 1 >= GRID_DIMENSION or grid[x][y + 1].visited == True:
        grid[x][y].options.update({"down": False})
    # Disallow the left direction if we are on the leftmost edge of the grid
    # or the square to the left of the current one has already been visited.
    if x - 1 < 0 or grid[x - 1][y].visited == True:
        grid[x][y].options.update({"left": False})
    # Disallow the right direction if we are on the rightmost edge of the grid
    # or the square to the right of the current one has already been visited.
    if x + 1 >= GRID_DIMENSION or grid[x + 1][y].visited == True:
        grid[x][y].options.update({"right": False})


class Spot:
    """
    Class made to contain the data we need about any point on the grid:
    - Which directions we are allowed to move towards and which we aren't.
    - Which directions we can choose for our next move.
    - If the point has been visited or not.
    """
    
    def __init__(self):
        self.options: Dict = {"up": True, "down": True, "left": True,
                              "right": True}
        self.allowed: List = []
        self.visited: bool = False
    
    def generate_allowed(self) -> None:
        """
        From the self.options dictionary, filters the directions which
        are not false (i.e. disallowed) and puts them into the self.allowed
        list.
        """
        self.allowed = []
        for (key, value) in self.options.items():
            if value:
                self.allowed.append(key)


def main():
    # Create the grid as a list and convert it to a numpy array.
    grid: Collection[Collection[int]] = []
    for i in range(GRID_DIMENSION):
        grid.append([])
        for j in range(GRID_DIMENSION):
            grid[i].append(Spot())
    grid = np.array(grid)
    
    # Initialise the current position as the upper left corner of the grid and
    # the history, i.e. the list which is going to contain the positions taken
    # in our random walk.
    current_position: Collection[int] = np.array([0, 0])
    history = []
    
    while True:
        # Add the current position to the history.
        history.append(current_position.copy())
        # Get a variable pointing at the corresponding grid position for
        # convenience.
        current_grid_pos = grid[current_position[0]][current_position[1]]
        # Set the current position as visited on the grid.
        current_grid_pos.visited = True
        # Update the possible directions in the object describing the current
        # position on the grid.
        check_possible_direction(current_position)
        current_grid_pos.generate_allowed()
        # Choose a new direction to go at random (if there is one), else exit
        # the loop. If the walk has gone across the whole grid it will print
        # "success", else it will print "stuck".
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
        elif len(history) == 25:
            print("Success!")
            break
        else:
            print("Stuck!")
            break
    
    # Convert the history list into an array for convenience.
    history = np.array(history)
    
    # Split the array into the x coordinates and the y coordinates.
    x: Collection[int] = history[:, 0]
    y: Collection[int] = history[:, 1]
    
    # Flip the y-axis in order to maintain the correspondence between the grid,
    # where (0,0) is the upper left corner, and the plot graph.
    y = abs(y - 5)
    
    # Plot the random walk result on a graph, marking the starting position
    # with a
    # green dot, the ending position with a red dot and the intermediate
    # ones with
    # blue dots.
    plt.plot(x, y)
    plt.plot(x, y, "bo")
    plt.plot(x[0], y[0], "go")
    plt.plot(x[-1], y[-1], "ro")
    plt.show()


if __name__ == "__main__":
    main()
