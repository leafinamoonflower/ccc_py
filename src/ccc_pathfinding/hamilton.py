import time

EMPTY_SPACE_SYMBOLS = '.'
STARTING_POINT_SYMBOLS = 'Ss'
OBSTACLE_SYMBOL = 'X'
DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

class HamiltonSolver:
    """Solver for a Hamilton Path problem."""

    def __init__(self, grid):
        """Initialize the HamiltonSolver instance from a grid, which must be a
        list of strings, one for each row of the grid.

        """
        self.grid = grid
        self.h = h = len(grid)
        self.w = w = len(grid[0])
        if any(len(row) != w for row in grid):
            raise ValueError("Grid is not rectangular")
        self.start = None
        self.legal = set()
        for r, row in enumerate(grid):
            for c, item in enumerate(row):
                if item in STARTING_POINT_SYMBOLS:
                    if self.start is not None:
                        raise ValueError("Multiple starting points")
                    self.start = (r, c)
                elif item in EMPTY_SPACE_SYMBOLS:
                    self.legal.add((r, c))
        if self.start is None:
            raise ValueError("No starting point")

    def format_solution(self, path):
        """Format a path as a string."""
        grid = [[OBSTACLE_SYMBOL] * self.w for _ in range(self.h)]
        prev_r, prev_c = None, None
        formatted_path = ''
        for (r, c) in path:
            if prev_r is not None and prev_c is not None:
                if r > prev_r:
                    direction = 'S'  # Move down
                elif r < prev_r:
                    direction = 'W'  # Move up
                elif c < prev_c:
                    direction = 'A'  # Move left
                elif c > prev_c:
                    direction = 'D'  # Move right
                else:
                    direction = ' '  # No movement
                formatted_path += direction
            prev_r, prev_c = r, c

        # Add 'S' to indicate reaching the destination
        formatted_path += 'S'

        return formatted_path

    def solve(self):
        """Generate solutions as lists of coordinates."""
        target_path_len = len(self.legal) + 1
        paths = [[self.start]]
        start_time = time.time()
        while paths and time.time() - start_time < 1.0:
            path = paths.pop()
            if len(path) == target_path_len:
                yield path
            r, c = path[-1]
            for dr, dc in DIRS:
                new_coord = r + dr, c + dc
                if new_coord in self.legal and new_coord not in path:
                    paths.append(path + [new_coord])