from typing import overload

import pygame

class CoordinateConvertor():
    """
    Class that contains methods for converting coordinates from the Pygame coordinate system to the centralised coordinate system and back.
        By Pygame coordinate system I mean coordinate system which has 0,0 at the upper-left corner of the screen and y-axis directed down.
        By centralised coordinate system I mean coordinate system which has 0,0 at the center of the screen and y-axis directed up.
    """
    def __init__(self, width : int, height : int):
        """
        Args:
            width: Screen width in pixels.
            height: Screen height in pixels.
        """
        if not (
                (isinstance(width, int) and not isinstance(width, (bool,tuple)))
                and
                (isinstance(height, int) and not isinstance(height, (bool,tuple)))
            ):
            raise TypeError(f"expected two integers, got {type(width).__name__} and {type(height).__name__}")
        if not (width > 0 and height > 0):
            raise ValueError("Screen width and height can't be negative or zero")
        
        self.width = width
        self.height = height


    @overload
    def convertToCenter(self, x : int|float, y : int|float) -> tuple[int|float, int|float]: ...

    @overload
    def convertToCenter(self, coordinates : pygame.typing.Point) -> tuple[int|float, int|float]: ...
    
    def convertToCenter(
            self,
            value1 : int | float | pygame.typing.Point,
            value2 : int | float | None = None
            ) -> tuple[int|float, int|float]:
        """
        Converts coordinates from the Pygame coordinate system to the centralised coordinate system.
        
        Args:
            value1: Horizontal coordinate, or a point (sequence of two numbers).
            value2: Vertical coordinate. Omit when value1 is a sequence.
        
        Returns:
            Tuple of converted coordinates.
        """
        if value2 is None:
            if (
                not isinstance(value1, (tuple, list, pygame.Vector2))
                or
                len(value1) != 2
                or
                not all((isinstance(c, (int, float)) and not isinstance(c, bool)) for c in value1)
            ):
                raise TypeError(f"expected a point (sequence of two numbers), got {repr(value1)}")

            x, y = value1
        else:
            if not (
                (isinstance(value1, (int, float)) and not isinstance(value1, bool))
                and
                (isinstance(value2, (int, float)) and not isinstance(value2, bool))
            ):
                raise TypeError(f"expected two numbers, got {type(value1).__name__} and {type(value2).__name__}")
            
            x, y = value1, value2

        return (x - self.width//2, -(y - self.height//2))
    

    @overload
    def convertFromCenter(self, x : int|float, y : int|float) -> tuple[int|float, int|float]: ...

    @overload
    def convertFromCenter(self, coordinates : pygame.typing.Point) -> tuple[int|float, int|float]: ...
    
    def convertFromCenter(
            self,
            value1 : int | float | pygame.typing.Point,
            value2 : int | float | None = None
            ) -> tuple[int|float, int|float]:
        """
        Converts coordinates from the centralised coordinate system to the Pygame coordinate system.
        
        Args:
            value1: Horizontal coordinate, or a point (sequence of two numbers).
            value2: Vertical coordinate. Omit when value1 is a sequence.
        
        Returns:
            Tuple of converted coordinates.
        """
        if value2 is None:
            if (
                not isinstance(value1, (tuple, list, pygame.Vector2))
                or
                len(value1) != 2
                or
                not all((isinstance(c, (int, float)) and not isinstance(c, bool)) for c in value1)
            ):
                raise TypeError(f"expected a point (sequence of two numbers), got {repr(value1)}")

            x, y = value1
        else:
            if not (
                (isinstance(value1, (int, float)) and not isinstance(value1, bool))
                and
                (isinstance(value2, (int, float)) and not isinstance(value2, bool))
            ):
                raise TypeError(f"expected two numbers, got {type(value1).__name__} and {type(value2).__name__}")
            
            x, y = value1, value2

        return (x + self.width//2, -(y - self.height//2))