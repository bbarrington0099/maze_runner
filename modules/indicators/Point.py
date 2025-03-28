class Point:
    """
    A point in 2D space.
    """
    def __init__(self, x: int, y: int):
        """
        Create a point. Point(0, 0) is the top left corner.\n
        x increases to the right, y increases downwards.
        """
        self.x = x
        self.y = y