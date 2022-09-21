
import pygame
from Sprite import Sprite

class Person( object ):
    def __init__( self, cur_x : int, cur_y : int,  image_path : str, json_path : str, NUM_FRAMES : int, sprite_index, x_name : str, y_name: str, width_name : str, height_name : str):
        self._NUM_FRAMES = NUM_FRAMES

        self._cur_x = cur_x
        self._cur_y = cur_y
        self._scale = 1

        self._sprites = Sprite( image_path= image_path, json_path= json_path,  x_name = x_name, y_name = y_name, width_name = width_name, height_name = height_name).get_frames( num_frame= NUM_FRAMES )
        self._sprite_index = sprite_index

    def move( self, screen : pygame.Surface, dx : float , dy : float):
        if ( self._cur_x <= screen.get_width() and self._cur_y <= screen.get_height() ):
            self._cur_x += dx
            self._cur_y += dy
            self._sprite_index += 1

    def render( self, screen: pygame.Surface ):
        # renders the current frame/sprite-frame to the cur_x, cur_y
        if ( self._cur_x <= screen.get_width() and self._cur_y <= screen.get_height() ):
            # Accessing the next sprite
            sprite_surf = ( self._sprites[ self._sprite_index % self._NUM_FRAMES] )

            # Accurate draw, centering the blit
            sprite_rect = sprite_surf.get_rect()
            sprite_rect.center = ( self._cur_x, self._cur_y )
            screen.blit( sprite_surf, sprite_rect )
