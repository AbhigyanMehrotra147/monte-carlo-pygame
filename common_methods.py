import pygame

list_bool = []
list_index = 0

def get_relative_coords( relative_surface: pygame.Surface, relative_coords: tuple ):
    surf_size = relative_surface.get_size()
    return (int(surf_size[0]*relative_coords[0]),int(surf_size[1]*relative_coords[1]))

def get_relative_size( relative_surface: pygame.Surface, relative_size: tuple):
    surf_size = relative_surface.get_size()
    return ( int(surf_size[0]*relative_size[0]), int(surf_size[1]*relative_size[1]) )

def _read_file( file_path, file_mode: str ):
    global list_bool
    file = open( file_path, file_mode )
    temp_str = ""
    for line in file:
        temp_str += line
    list_bool = list(temp_str.split( " " ))
    list_bool = [int(i) for i in list_bool]

def _update_index( number_of_dots ):
    
    global list_index
    if (list_index < (len(list_bool) - number_of_dots*2 - 1)):
        list_index += 1
    else:
        list_index = 0