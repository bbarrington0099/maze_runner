from modules.display.Window import Window
from modules.indicators.Line import Line
from modules.indicators.Point import Point

class Cell:
    """
    A cell in a grid.
    """
    def __init__(self, 
                 window: Window, 
                 top_left_x: int = None, top_left_y: int = None, 
                 bottom_right_x: int = None, bottom_right_y: int = None, 
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
        if self.__top_left_x is not None and \
            self.__bottom_right_x is not None and \
            self.__top_left_y is not None and \
            self.__bottom_right_y is not None:
            self.__center: Point = Point(
                (top_left_x + bottom_right_x) // 2, 
                (top_left_y + bottom_right_y) // 2
            )
        self.visited: bool = False
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

    def draw(self, fill_color: str = "black", top_left_x: int = None, top_left_y: int = None, 
                 bottom_right_x: int = None, bottom_right_y: int = None):
        """
        Draw the cell on the window.
        """
        if top_left_x is not None and \
            bottom_right_x is not None and \
            top_left_y is not None and \
            bottom_right_y is not None:
            self.update_coordinates(
                top_left_x, top_left_y,
                bottom_right_x, bottom_right_y
            )
            self.update_walls()

        for wall in self.walls:
            if self.walls[wall]["has_wall"]:
                self.__window.draw_line(
                    self.walls[wall]["line"], 
                    fill_color
                )
            else:
                self.__window.draw_line(
                    self.walls[wall]["line"], 
                    "white"
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
        
    def update_coordinates(self, top_left_x: int, top_left_y: int, 
                        bottom_right_x: int, bottom_right_y: int):
        """
        Update the coordinates of the cell.
        """
        self.__top_left_x = top_left_x
        self.__top_left_y = top_left_y
        self.__bottom_right_x = bottom_right_x
        self.__bottom_right_y = bottom_right_y
        self.__center = Point(
            (top_left_x + bottom_right_x) // 2, 
            (top_left_y + bottom_right_y) // 2
        )

    def update_walls(self):
        self.walls = {
            "top": {
                "has_wall": self.walls["top"]["has_wall"],
                "line": Line(
                    Point(self.__top_left_x, self.__top_left_y),
                    Point(self.__bottom_right_x, self.__top_left_y)
                )
            },
            "right": {
                "has_wall": self.walls["right"]["has_wall"],
                "line": Line(
                    Point(self.__bottom_right_x, self.__top_left_y),
                    Point(self.__bottom_right_x, self.__bottom_right_y)
                )
            },
            "bottom": {
                "has_wall": self.walls["bottom"]["has_wall"],
                "line": Line(
                    Point(self.__bottom_right_x, self.__bottom_right_y),
                    Point(self.__top_left_x, self.__bottom_right_y)
                )
            },
            "left": {
                "has_wall": self.walls["left"]["has_wall"],
                "line": Line(
                    Point(self.__top_left_x, self.__bottom_right_y),
                    Point(self.__top_left_x, self.__top_left_y)
                )
            }
        }