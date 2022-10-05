
import pygame

class Background( object ):

    def __init__( self, screen : pygame.Surface ):

        self._GRAD = 30
        self._ALPHA = 1
        self._DAWN = [ 219, 132, 120, self._ALPHA ]
        self._NIGHT = [ 8, 30, 50, self._ALPHA]

        self._cur_rgba = self._DAWN

        self._cur_focus = -1

        self._hue = pygame.Surface( screen.get_size() ).convert_alpha()
        self._arr_colors = [ [ 255, 0, 0, 0 ], [ 125, 181, 217, 0 ], [ 73, 159, 214, 0 ], [ 45, 132, 215, 0 ], [ 54, 117, 205, 0 ], [ 47, 93, 197, 0 ], [ 32, 74, 156, 0 ], [ 255, 52, 127, 0 ] ]
        self._len_colors = len( self._arr_colors )

        # self._PROMENARD = pygame.image.load( "./Environment.png" ).convert_alpha()
        self._PROMENARD = pygame.Surface( screen.get_size() )
        self._PROMENARD.fill( ( 250, 250, 250 ) )
        self._PROMENARD = pygame.transform.scale( surface= self._PROMENARD, size= screen.get_size())

    def update( self ):
        self._cur_focus = ( self._cur_focus + 1 ) % self._len_colors
        # print( "The current focus is: ", self._cur_focus )

    def _return_alpha( self, cur_index: int, cur_focus: int ):
        # using the function 1/2 next next
        return ( 2 ** ( -1 * ( 2 * abs( cur_index - cur_focus ) + 1 ) ) )

    def render_background( self, screen : pygame.Surface ):
        screen.blit( self._PROMENARD, ( 0, 0 ) )

    def render_hue( self, screen : pygame.Surface ):
        for cur_index in range( 0, self._len_colors ):
            self._arr_colors[ cur_index ][ -1 ] = self._return_alpha( cur_index, self._cur_focus )

        for cur_index in range( 0, self._len_colors ):
            self._hue.fill( self._arr_colors[ cur_index ] )
            screen.blit( self._hue, ( 0, 0 ) )

