
import pygame

class Background( object ):

    def __init__( self, screen : pygame.Surface ):

        self._GRAD = 30
        self._ALPHA = 1
        self._DAWN = [ 219, 132, 120, self._ALPHA ]
        self._NIGHT = [ 8, 30, 50, self._ALPHA]

        self._cur_rgba = self._DAWN

        self._arr_index = 0

        self._hue = pygame.Surface( screen.get_size() ).convert_alpha()
        self._arr_colors = [ [], [], [], [], [], [], [], [] ]
        self._promenard = pygame.transform.scale( pygame.image.load( "./background.png" ).convert(), screen.get_size() )

    def update( self ):

        for i in range( 0, 3 ):
            self._cur_rgba[ i ] -= 100/ self._GRAD
            self._cur_rgba[ i ] %= 255

        # self._arr_index += 1
        # if self._arr_index == len(self._arr_colors):
        #     self._arr_index = 0

    def render_background( self, screen : pygame.Surface ): 
        screen.blit( self._promenard, ( 0, 0 ) )

    def render_hue( self, screen : pygame.Surface ):
        self._hue.fill( self._cur_rgba )
        screen.blit( self._hue, ( 0, 0) )
