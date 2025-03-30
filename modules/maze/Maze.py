import time
import random

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
        window: Window, seed: int = None
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

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_entrance_and_exit(self):
        """
        Break the entrance and exit walls of the maze.
        """
        entrance_exit_cells: list[Cell] = [
            self._cells[0][0],
            self._cells[self._num_cols - 1][self._num_rows - 1]
        ]
        for cell in entrance_exit_cells:
            for wall in cell.walls.values():
                wall["has_wall"] = False
            cell.update_walls()
            cell.draw()
        self._animate()
        
    def _break_walls_r(self, col: int, row: int):
        """
        Break cell walls along the maze grid recursively.
        """
        current_cell: Cell = self._cells[col][row]
        current_cell.visited = True
        break_walls: bool = True
        while break_walls:
            next_index_list: list[tuple[int, int]] = []
            if col > 0 and not self._cells[col - 1][row].visited:
                next_index_list.append((col - 1, row))
            if col < self._num_cols - 1 and not self._cells[col + 1][row].visited:
                next_index_list.append((col + 1, row))
            if row > 0 and not self._cells[col][row - 1].visited:
                next_index_list.append((col, row - 1))
            if row < self._num_rows - 1 and not self._cells[col][row + 1].visited:
                next_index_list.append((col, row + 1))

            if len(next_index_list) == 0:
                self._draw_cell(col, row)
                return
            
            direction_index: int = random.randrange(len(next_index_list))
            next_index: tuple[int, int] = next_index_list[direction_index]

            if next_index[0] == col + 1:
                self._cells[col][row].walls["right"]["has_wall"] = False
                self._cells[next_index[0]][next_index[1]].walls["left"]["has_wall"] = False
            elif next_index[0] == col - 1:
                self._cells[col][row].walls["left"]["has_wall"] = False
                self._cells[next_index[0]][next_index[1]].walls["right"]["has_wall"] = False
            elif next_index[1] == row + 1:
                self._cells[col][row].walls["bottom"]["has_wall"] = False
                self._cells[next_index[0]][next_index[1]].walls["top"]["has_wall"] = False
            elif next_index[1] == row - 1:
                self._cells[col][row].walls["top"]["has_wall"] = False
                self._cells[next_index[0]][next_index[1]].walls["bottom"]["has_wall"] = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        """
        Reset the visited status of all cells in the maze.
        """
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False