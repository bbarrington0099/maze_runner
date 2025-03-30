from modules.display.Window import Window
from modules.maze.Maze import Maze

def main():
    window = Window(800, 600)
    maze = Maze(
        top_left_x=10, top_left_y=10,
        num_rows=16, num_cols=16,
        cell_width=10, cell_height=10,
        window=window
    )
    window.wait_for_close()

if __name__ == "__main__":
    main()