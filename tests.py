import unittest
import random

from modules.display.Window import Window
from modules.maze.Maze import Maze

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        """
        Test the creation of cells in the maze.
        """
        window: Window = Window(800, 600)
        num_cols: int = 12
        num_rows: int = 10
        m1: Maze = Maze(10, 10, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        """
        Test the creation of cells in the maze with larger dimensions.
        """
        window: Window = Window(800, 600)
        num_cols: int = 16
        num_rows: int = 12
        m1: Maze = Maze(10, 10, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_with_seed(self):
        """
        Test the maze generation with a specific seed. Compare two mazes with the same seed.
        """
        window1: Window = Window(800, 600)
        window2: Window = Window(800, 600)
        num_cols: int = 12
        num_rows: int = 10
        seed: int = random.randint(0, 100)
        m1: Maze = Maze(10, 10, num_rows, num_cols, 10, 10, window1, seed=seed)
        m2: Maze = Maze(10, 10, num_rows, num_cols, 10, 10, window2, seed=seed)
        
        for test_row in range(num_rows):
            for test_col in range(num_cols):
                self.assertEqual(
                    m1._cells[test_col][test_row].walls["top"]["has_wall"],
                    m2._cells[test_col][test_row].walls["top"]["has_wall"],
                )
                self.assertEqual(
                    m1._cells[test_col][test_row].walls["right"]["has_wall"],
                    m2._cells[test_col][test_row].walls["right"]["has_wall"],
                )
                self.assertEqual(
                    m1._cells[test_col][test_row].walls["bottom"]["has_wall"],
                    m2._cells[test_col][test_row].walls["bottom"]["has_wall"],
                )
                self.assertEqual(
                    m1._cells[test_col][test_row].walls["left"]["has_wall"],
                    m2._cells[test_col][test_row].walls["left"]["has_wall"],
                )

    def test_maze_visited_cell_reset(self):
        """
        Confirm that the visited attribute of cells is reset correctly to False.
        """
        window: Window = Window(800, 600)
        num_cols: int = 12
        num_rows: int = 10
        m1: Maze = Maze(10, 10, num_rows, num_cols, 10, 10, window)
        
        for test_row in range(num_rows):
            for test_col in range(num_cols):
                self.assertFalse(
                    m1._cells[test_col][test_row].visited,
                )
            

if __name__ == "__main__":
    unittest.main()