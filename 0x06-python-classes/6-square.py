#!/usr/bin/python3
"""
This is a module that defines a class Square
by: (5-square.py)
"""


class Square:
    """
    This is a class that defines a Square

    Attributes:
        size (int): Length of one side of the square.
        position (tuple): Tuple with coordinates of the sqare.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method initializes attributes whenever an object is instantiated.

        Args:
            size (int): Length of one side of the square.
            position (tuple): Tuple with coordinates of the sqare.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Private instance attribute: size
        """
       if (not isinstance(position, tuple) or len(position) != 2
            or not isinstance(position[0], int) or
            not isinstance(position[1], int) or position[0] < 0
                or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        """
        Private instance attribute: position
        """

    @property
    def size(self):
        """
        Getter method that returns the size.

        Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method that sets the size of the square.
        
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method that returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method that sets the position of the square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not
            isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            Area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Function that prints a square made of #
        """
        if self.__size == 0:
            print("")
        else:
            string_to_print = ""
            for i in range(self.position[1]):
                string_to_print += "\n"
            for x in range(self.size):
                for y in range(self.position[0]):
                    string_to_print += " "
                for z in range(self.size):
                    string_to_print += "#"
                string_to_print += "\n"
            print("{}".format(string_to_print), end='')
