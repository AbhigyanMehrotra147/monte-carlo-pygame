
import pygame
import json


class Sprite( object ):

    def __init__( self, image_path: str, json_path: str ):

        self._path = image_path
        self._frame_dict = json.load( open( json_path ) )["frames"]

        self._image = pygame.image.load( image_path ).convert_alpha()
        self._image_arr = []
        
    def _get_sprite( self, x: int, y: int, w: int, h: int ):
        # .set_colorkey( (0, 0, 0) ) raises a problem when function colorkey is added
        tmp_surf = pygame.Surface( ( w, h ) )
        pygame.Surface.set_colorkey( tmp_surf, (0, 0, 0) )
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
                data_dict = self._frame_dict[ posture ][ "frame" ]
                self._image_arr.append( self._get_sprite( data_dict[ 'x' ], data_dict[ 'y' ], data_dict[ 'w' ], data_dict[ 'h' ] ) )

            frame_number += 1
        
        return self._image_arr
