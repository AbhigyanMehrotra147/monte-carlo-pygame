
import pygame

class Sprite( object ):

    def __init__( self, path: str ):

        self._path = path
        self._image = pygame.image.load( path ).convert()

    def get_sprite( x: int, y: int, w: int, h: int ):
        tmp_surf = pygame.Surface( ( w, h ) ).set_colorkey( (0, 0, 0) )

        # return the image surface cut at a specific x, y, w, h
        return tmp_surf.blit( self._image, ( 0, 0 ), ( x, y, w, h ) )

