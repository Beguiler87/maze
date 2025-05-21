from tkinter import Tk, BOTH, Canvas

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
def main():
    win = Window(800, 600)
    win.wait_for_close()
if __name__ == "__main__":
    main()