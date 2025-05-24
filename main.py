from tkinter import Tk, BOTH, Canvas
import time
# defines the window display
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # parent widget creating an instance of Tk
        self.__root = Tk()
        # assigns title attribute
        self.__root.title("Maze Solver")
        # parent widget creatin an instance of Canvas
        self.__canvas = Canvas(self.__root, width=width, height=height)
        # makes the 'canvas' visible in the window
        self.__canvas.pack()
        # indicator that the window is running
        self.__running = False
        # hooks the system to the "close" options in the window and tells it to trigger the shutoff
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    # methods for keeping the window running and functional until the "close" trigger is given
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    # method to close the window on given input. cancels the redraw and wait_for_close methods, tells tkinter to erase the window and free up the resources
    def close(self):
        self.__running = False
        self.__root.destroy()
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    def draw_move(self, to_cell, from_cell, undo=False):
        to_point = Point(*to_cell.get_center())
        from_point = Point(*from_cell.get_center())
        fill_color = "gray" if undo else "red"
        new_line = Line(from_point, to_point)
        self.draw_line(new_line, fill_color)
# used to define x and y axis points within the window
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# used to define lines
class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
    def draw(self, canvas, fill_color):
        canvas.create_line(
        self.start_point.x, self.start_point.y,
        self.end_point.x, self.end_point.y,
        fill=fill_color, width=2
        )
# defines which lines should be drawn upon refresh
class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win == None:
            return
        fill_color = "black" if self.has_left_wall else "white"
        left_line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.__win.draw_line(left_line, fill_color)
        fill_color = "black" if self.has_right_wall else "white"
        right_line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        self.__win.draw_line(right_line, fill_color)
        fill_color = "black" if self.has_top_wall else "white"
        top_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.__win.draw_line(top_line, fill_color)
        fill_color = "black" if self.has_bottom_wall else "white"
        bottom_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.__win.draw_line(bottom_line, fill_color)
    def get_center(self):
        center_x = (self.__x1 + self.__x2) /2
        center_y = (self.__y1 + self.__y2) /2
        return (center_x, center_y)
# defines the maze itself
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.grid = []
        self.__create_cells()
    # creates the cells that make up the maze
    def __create_cells(self):
        for row in range(self.num_rows):
            cells_in_row = []
            for col in range(self.num_cols):
                cell = Cell(self.win)
                cells_in_row.append(cell)
            self.grid.append(cells_in_row)
        print("num_rows:", self.num_rows)
        print("num_cols:", self.num_cols)
        print("grid shape:", len(self.grid), "rows,", len(self.grid[0]) if self.grid else 0, "cols per row")
        print("total cells:", sum(len(row) for row in self.grid))
        if self.win == None:
            return
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.__draw_cell(row, col)
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)
    def __draw_cell(self, i, j):
        cell = self.grid[i][j]
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = self.x1 + (j + 1) * self.cell_size_x
        y2 = self.y1 + (i + 1) * self.cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()
    # creates the start and end points for the maze
    def _break_entrance_and_exit(self):
        self.grid[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.grid[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.num_rows - 1, self.num_cols - 1)
# primary function
def main():
    # defines window size
    window_width = 1000
    window_height = 800
    num_rows = 3
    num_cols = 5
    win = Window(window_width, window_height)
    cell_size_x = 20
    cell_size_y = 20
    cell_size = int(min(cell_size_x, cell_size_y))
    maze_width = num_cols * cell_size
    maze_height = num_rows * cell_size
    x1 = (window_width - maze_width) // 2
    y1 = (window_height - maze_height) // 2
    maze = Maze(x1, y1, num_rows, num_cols, cell_size, cell_size, win)
    maze._break_entrance_and_exit()
    # Wait for user to close the window
    win.wait_for_close()
if __name__ == "__main__":
    main()