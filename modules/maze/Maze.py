import time

from modules.display.Window import Window
from modules.maze.Cell import Cell

class Maze:
    """
    A class representing a maze grid.
    """
    def __init__(self, 
        top_left_x: int, top_left_y: int, 
        num_rows: int, num_cols: int, 
        cell_width: int, cell_height: int,
        window: Window,
    ):
        """
        Create a maze grid with the given parameters.
        """
        self._top_left_x: int = top_left_x
        self._top_left_y: int = top_left_y
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_width: int = cell_width
        self._cell_height: int = cell_height
        self._window: Window = window
        self._cells: list[list[Cell]] = []

        self._create_cells()

    def _create_cells(self):
        """
        Create cells for the maze grid.
        """
        for col in range(self._num_cols):
            col_cells: list[Cell] = []
            for row in range(self._num_rows):
                col_cells.append(Cell(self._window))
            self._cells.append(col_cells)
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col: int, row: int):
        """
        Draw a cell of the maze grid.
        """
        top_left_x: int = self._top_left_x + col * self._cell_width
        top_left_y: int = self._top_left_y + row * self._cell_height
        bottom_right_x: int = top_left_x + self._cell_width
        bottom_right_y: int = top_left_y + self._cell_height

        cell: Cell = self._cells[col][row]
        cell.draw(
            top_left_x = top_left_x, top_left_y = top_left_y, 
            bottom_right_x = bottom_right_x, bottom_right_y = bottom_right_y,
        )
        self._animate()

    def _animate(self):
        """
        Update the display window to show the drawn cells.
        """
        self._window.redraw()
        time.sleep(0.05)