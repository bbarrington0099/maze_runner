from tkinter import Canvas
from modules.indicators.Point import Point

class Line:
    """
    A line in 2D space.
    """
    def __init__(self, start: Point, end: Point):
        """
        Create a line from start to end.
        """
        self.start: Point = start
        self.end: Point = end

    def draw(self, canvas: Canvas, fill_color: str):
        """
        Draw the line on the canvas.
        """
        canvas.create_line(
            self.start.x, self.start.y, 
            self.end.x, self.end.y, 
            fill=fill_color, width=2
        )