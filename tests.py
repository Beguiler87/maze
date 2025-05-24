import unittest

from main import Maze
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.grid),
            num_rows,
        )
        self.assertEqual(
            len(m1.grid[0]),
            num_cols,
        )
    def test_maze_2(self):
        num_cols = 5
        num_rows = 17
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.grid),
            num_rows,
        )
        self.assertEqual(
            len(m1.grid[0]),
            num_cols,
        )
    def test_maze_empty(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.grid),
            num_rows,
            )
        if num_cols > 0 and num_rows > 0:
            self.assertEqual(
                len(m1.grid[0]),
                    num_cols,
                )
        if num_cols == 0 and num_rows == 0:
            print("empty list. no grid")
            return
    def test_start_and_finish(self):
        window_width = 1000
        window_height = 800
        num_rows = 20
        num_cols = 30
        win = None
        cell_size_x = 20
        cell_size_y = 20
        cell_size = int(min(cell_size_x, cell_size_y))
        maze_width = num_cols * cell_size
        maze_height = num_rows * cell_size
        x1 = (window_width - maze_width) // 2
        y1 = (window_height - maze_height) // 2
        maze = Maze(x1, y1, num_rows, num_cols, cell_size, cell_size, win)
        maze._break_entrance_and_exit()
        self.assertEqual(maze.grid[0][0].has_top_wall, False)
        self.assertEqual(maze.grid[maze.num_rows - 1][maze.num_cols - 1].has_bottom_wall, False)
if __name__ == "__main__":
    unittest.main()