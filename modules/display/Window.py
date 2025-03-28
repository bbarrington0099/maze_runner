from tkinter import Tk, BOTH, Canvas
from modules.indicators.Line import Line

class Window:
    """
    A window with a canvas to draw on.
    """
    def __init__(self, width: int, height: int):
        """
        Create the window.
        """   
        self.__widget = Tk()
        self.__widget.title("Maze Runner")
        self.__widget.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__widget, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.is_running = False

    def redraw(self):
        """
        Redraw the window by completing all pending drawing tasks.
        """
        self.__widget.update_idletasks()
        self.__widget.update()

    def wait_for_close(self):
        """
        Draws the window until it is closed.
        """
        print("Window opened.")
        self.is_running = True
        while self.is_running:
            self.redraw()
        print("Window closed.")
    
    def close(self):
        """
        Close the window.
        """
        print("Closing window...")
        self.is_running = False

    def draw_line(self, line: Line, fill_color: str):
        """
        Draw a line on the window's canvas.
        """
        line.draw(self.__canvas, fill_color)