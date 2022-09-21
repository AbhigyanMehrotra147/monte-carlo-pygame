
import pygame
import json

class Sprite( object ):

    def __init__( self, image_path: str, json_path: str, x_name : str, y_name: str, width_name : str, height_name : str):

        self._path = image_path
        self._frame_dict = json.load( open( json_path ) )["frames"]

        self._image = pygame.image.load( image_path ).convert_alpha()
        self._image_arr = []

        # need to pramatrise this for compatibility with larger spritesheets
        self._x_name = x_name
        self._y_name = y_name
        self._width_name = width_name
        self._height_name = height_name

    def _get_sprite( self, x: int, y: int, w: int, h: int ):
        # .set_colorkey( (0, 0, 0) ) raises a problem when function colorkey is added
        tmp_surf = pygame.Surface( ( w, h ) )
        pygame.Surface.set_colorkey( tmp_surf, ( 0, 0, 0 ) )
        if tmp_surf is None:
            raise Exception("Unable to make Sprite surface")

        # return the image surface cut at a specific x, y, w, h
        tmp_surf.blit( self._image, ( 0, 0 ), ( x, y, w, h ) )

        return tmp_surf

    def get_frames( self, num_frame: int ):
        # this returns the array of surfaces of the character
        frame_number = 0
        for posture in self._frame_dict.keys():
            if( frame_number > num_frame ):
                break
            else:
                data_dict = self._frame_dict[ posture ]
                self._image_arr.append( self._get_sprite( data_dict[ self._x_name ], data_dict[ self._y_name ], data_dict[ self._width_name ], data_dict[ self._height_name ] ) )

            frame_number += 1

        return self._image_arr
