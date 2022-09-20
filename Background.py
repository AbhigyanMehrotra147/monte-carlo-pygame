
import pygame

class Background( object ):

    def __init__( self, screen : pygame.Surface ):
        self._arr_index = 0

        self._grad = 30

        self._ALPHA = 0.3
        self._DAWN = [ 219, 132, 120, self._ALPHA ]
        self._cur_rgba = self._DAWN
        self._NIGHT = [ 8, 30, 50, self._ALPHA]

        self._hue = pygame.Surface( screen.get_size() )

        self._arr_colors = []

    def update( self ):
        
        for i in range( 0, 3 ):
            self._cur_rgba[ i ] -= 100/ self._grad
            self._cur_rgba[ i ] %= 255
        # self._arr_index += 1
        # if self._arr_index == len(self._arr_colors):
        #     self._arr_index = 0

    def render( self, screen : pygame.Surface ):
        self._hue.fill(self._cur_rgba)
        screen.blit( self._hue, ( 0, 0) )
