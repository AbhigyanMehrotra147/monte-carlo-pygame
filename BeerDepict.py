
from tracemalloc import start
import pygame
from common_methods import get_relative_coords

class DepictBox:

    # The capitalized arguments represent constant values only to assigned once
    # blit screen is the screen on which we will blit our surface
    # Line coordinates are always relative to the surface
    def __init__( self, SIZE: tuple, POS: tuple, BORDER_RADIUS: float, color: tuple, blit_screen: pygame.Surface, h_line_color: tuple, h_line_coords: list, v_line_color: tuple, v_line_coords: list, h_line_width: float, v_line_width: float ):
        
        self._SIZE = SIZE
        self._POS = POS
        self._BORDER_RADIUS = BORDER_RADIUS
        self._color = color
        self._rect = None
        self._surface = None
        self._blit_screen = blit_screen
        
        # Attributes of the horizontal division
        self._h_line_start = h_line_coords[0]
        self._h_line_end = h_line_coords[1]
        self._h_line_width = h_line_width
        self._h_line_color = h_line_color

        # Attributes of the vertical division
        self._v_line_start = v_line_coords[0]
        self._v_line_end = v_line_coords[1]
        self._v_line_width = v_line_width
        self._v_line_color = v_line_color
    def inititalize( self ):
        self._create_self()
        pass

    def _create_self( self ):
        # Setting color key so that it gets removed. 
        self._surface = pygame.Surface( size= self._SIZE )
        self._surface.set_colorkey (self._color)
        self._rect = pygame.Rect( self._POS, self._SIZE )

        # Getting position of lines to be drawn
        self._h_line_start = get_relative_coords( relative_surface = self._surface, relative_coords = self._h_line_start )
        self._h_line_end = get_relative_coords( relative_surface = self._surface, relative_coords = self._h_line_end )
        self._v_line_start = get_relative_coords( relative_surface = self._surface, relative_coords = self._v_line_start )
        self._v_line_end = get_relative_coords( relative_surface = self._surface, relative_coords = self._v_line_end )
    
    def _update( self ):
        pass

    def _render_lines( self ):
        pygame.draw.line( surface= self._surface, color= self._h_line_color, start_pos= self._h_line_start, end_pos= self._h_line_end, width=self._h_line_width )
        pygame.draw.line( surface= self._surface, color= self._v_line_color, start_pos= self._v_line_start, end_pos= self._v_line_end, width= self._v_line_width )
    
    def _render_self( self ):
        self._surface.fill( color=self._color )
        self._render_lines()
        self._blit_screen.blit( source = self._surface, dest = self._rect ) 
    
    # Function will call all renders, including self, BeerLine, Formula and Zi's
    def render( self ):
        self._render_self()
