import pygame
from common_methods import get_relative_coords

# Beerline surface will be blitted on BeerDepict surface
# The position of the beerline surface will by default be relative to the BeerDepict surface
class BeerLine:
    # The capital arguments suggest that the value remain constant during execution
    # Line coordinates are given as a list in which both relative start_pos and relative_pos are specified as seperate tuples 
    def __init__( self, SIZE: tuple, POS: tuple, COLOR: tuple, line_coords: list, line_color, line_width, \
        sad_dot_colors, sad_dot_radius, happy_dot_colors, happy_dot_radius, \
             popsickle_color, popsickle_width, , sad_smiley_pos, happy_smiley_pos, smiley_address ):
        
        self._surface = None
        self._rect = None
        
        # Attributes for the surface 
        self._SIZE = SIZE
        self._POS = POS
        self._COLOR = COLOR

        # Attributes for the line
        self._line_start_pos = line_coords[0]
        self._line_end_pos  = line_coords[1]
        self._line_color = line_color
        self._line_width = line_width

        # Attributes for the dots
        self._sad_dot_colors = sad_dot_colors
        self._sad_dot_radius = sad_dot_radius
        self._happy_dot_colors = happy_dot_colors
        self._happy_dot_radius = happy_dot_radius

        # Attributes for the popsickle
        self._popsickle_color = popsickle_color
        self._