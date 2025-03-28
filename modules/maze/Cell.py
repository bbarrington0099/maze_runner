from modules.display.Window import Window
from modules.indicators.Line import Line
from modules.indicators.Point import Point

class Cell:
    """
    A cell in a grid.
    """
    def __init__(self, 
                 top_left_x: int, top_left_y: int, 
                 bottom_right_x: int, bottom_right_y: int, 
                 window: Window, 
                 has_top_wall: bool = True, 
                 has_right_wall: bool = True, 
                 has_bottom_wall: bool = True, 
                 has_left_wall: bool = True
    ):
        """
        Create a cell.
        """
        self.__top_left_x: int = top_left_x
        self.__top_left_y: int = top_left_y
        self.__bottom_right_x: int = bottom_right_x
        self.__bottom_right_y: int = bottom_right_y
        self.__center: Point = Point(
            (top_left_x + bottom_right_x) // 2, 
            (top_left_y + bottom_right_y) // 2
        )
        self.__window: Window = window
        self.walls: dict = {
            "top": {
                "has_wall": has_top_wall,
                "line": Line(
                    Point(top_left_x, top_left_y),
                    Point(bottom_right_x, top_left_y)
                )
            },
            "right": {
                "has_wall": has_right_wall,
                "line": Line(
                    Point(bottom_right_x, top_left_y),
                    Point(bottom_right_x, bottom_right_y)
                )
            },
            "bottom": {
                "has_wall": has_bottom_wall,
                "line": Line(
                    Point(bottom_right_x, bottom_right_y),
                    Point(top_left_x, bottom_right_y)
                )
            },
            "left": {
                "has_wall": has_left_wall,
                "line": Line(
                    Point(top_left_x, bottom_right_y),
                    Point(top_left_x, top_left_y)
                )
            }
        }

    def draw(self, fill_color: str = "black"):
        """
        Draw the cell on the window.
        """
        for wall in self.walls:
            if self.walls[wall]["has_wall"]:
                self.__window.draw_line(
                    self.walls[wall]["line"], 
                    fill_color
                )

    def draw_to(self, target_cell: 'Cell', undo: bool = False, 
                first_draw_fill_color: str = "red", undo_draw_fill_color: str = "gray"
    ):
        """
        Draw a line from the center of this cell to the center of another cell.
        """
        fill_color = first_draw_fill_color if not undo else undo_draw_fill_color
        line = Line(self.__center, target_cell.__center)
        self.__window.draw_line(line, fill_color)
        
