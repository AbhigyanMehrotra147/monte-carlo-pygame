
import pygame
from Sprite import Sprite

class Person( object ):
    def __init__( self, cur_x : int, cur_y : int,  image_path : str, json_path : str, NUM_FRAMES : int, sprite_index):
        self._NUM_FRAMES = NUM_FRAMES

        self._cur_x = cur_x
        self.cur_x = cur_x
        self._cur_y = cur_y
        self._scale = 1

        self._sprites = Sprite( image_path= image_path, json_path= json_path).get_frames( num_frame= NUM_FRAMES )
        self._sprite_index = sprite_index

    def move( self, dx : float , dy : float):
        self._cur_x += dx
        self._cur_y += dy
        self.cur_x = self._cur_x

    def render( self, screen: pygame.Surface ):
        # renders the current frame/sprite-frame to the cur_x, cur_y
        sprite_surf = ( self._sprites[ self._sprite_index % self._NUM_FRAMES] )
        sprite_rect = sprite_surf.get_rect()
        sprite_rect.center = ( self._cur_x, self._cur_y )
        screen.blit( sprite_surf, sprite_rect )
    