
import pygame
from sympy import re
import common_methods as cm
import matplotlib.pyplot as plt

class BeerFormula:

    def __init__( self, blit_surface: pygame.Surface, SIZE: tuple, POS: tuple, COLOR: tuple,\
        formula_size: tuple, formula_pos: tuple, Poison ):

        # Surface to be blitted on
        self._blit_surface = blit_surface

        # own rect and surface
        self._surface = None
        self._rect = None

        # name of the formula png
        self._file = 'formula.png'

        # Relative size and position
        self._POS = POS
        self._SIZE = SIZE
        self._COLOR = COLOR

        # Attributes of Formula
        self._formula_size = formula_size
        self._formula_pos = formula_pos

        # Poison object in sync with Beerline and Beer zi
        self._Poison = Poison

        self._curr_index = 0

    def _create_self( self ):

        self._POS = cm.get_relative_coords( relative_surface= self._blit_surface, relative_coords= self._POS )
        self._SIZE = cm.get_relative_size( relative_surface= self._blit_surface, relative_size= self._SIZE )

        self._surface = pygame.Surface( size= self._SIZE )
        self._surface.set_colorkey( self._COLOR  )
        self._rect = pygame.Rect( self._POS, self._SIZE )

    def _return_formula( self, N: str = '10^6', index: str = 'i', avg: str = '0.7231', fig_size=( 12, 4 ), font_size: int = 60, pos= ( 0, 0.5 ), convolve: bool = True ):
        # Latex
        cur_tex = r"$\frac{1}{" + N + r"} * " + r"\sum_{" + index + r"=0}^{" + N + r"} Z_i = " + avg + r"$"

        # add text to axis
        f_fig = plt.figure( figsize = fig_size ) # formula fig
        f_fig.text( pos[ 0 ], pos[ 1 ], cur_tex, fontsize=font_size )

        # hide axes
        fig = f_fig.gca()
        f_fig.get_axes()[0].set_visible( False )
        f_fig.tight_layout()

        # save
        f_fig.savefig( self._file )

        plt.close( 'all' )

        if( convolve ):
            cm.make_mono( file= self._file )


    def _create_formula( self ):
        self._formula_pos = cm.get_relative_coords( relative_surface = self._surface, relative_coords= self._formula_pos )
        self._formula_size = cm.get_relative_size( relative_surface = self._surface, relative_size = self._formula_size )

    def create( self ):
        self._create_self()
        self._create_formula()

    def _update( self ):
        # update the formula.png with new N and new average
        self._curr_index =  self._Poison.get_cur_index() - 100
        self._return_formula( N= str( self._curr_index ), index='i', avg = str( self._Poison.get_mean( from_index = 0, to_index = self._curr_index ) )[0:5] )

    def _render_self( self ):
        self._surface.fill( self._COLOR )
        formula = pygame.image.load( self._file )
        formula.set_colorkey( ( 255, 255, 255 ) )

        formula = pygame.transform.scale( surface = formula, size = self._formula_size )
        self._surface.blit( source = formula, dest= self._formula_pos )
        self._blit_surface.blit( source = self._surface, dest= self._POS )

    def render( self ):
        self._update()
        self._render_self()
        pass
