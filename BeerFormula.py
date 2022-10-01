import pygame
from sympy import re
import common_methods as cm

class BeerFormula:

    def __init__( self, blit_surface: pygame.Surface, SIZE: tuple, POS: tuple, COLOR: tuple ):
        
        # Surface to be blitted on
        self._blit_surface = blit_surface

        # own rect and surface
        self._surface = None
        self._rect = None

        # Relative size and position
        self._POS = POS
        self._SIZE = SIZE
        self._COLOR = COLOR


    def _create_self( self ):
        
        self._POS = cm.get_relative_coords( relative_surface= self._blit_surface, relative_coords= self._POS )
        self._SIZE = cm.get_relative_size( relative_surface= self._blit_surface, relative_size= self._SIZE )
        self._surface = pygame.Surface( size= self._SIZE )
        self._surface.set_colorkey( self._COLOR )
        self._rect = pygame.Rect( self._POS, self._SIZE )


    def create( self ):
        self._create_self()

    def _update( self ):
        pass

    def _render_self( self ):
        self._surface.fill( self._COLOR )
        self._blit_surface.blit( source = self._surface, dest= self._POS )

    def render( self ):
        self._render_self()
        pass
