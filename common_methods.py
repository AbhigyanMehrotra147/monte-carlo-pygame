import pygame

list_bool = []
list_index = 0

def get_relative_coords( relative_surface: pygame.Surface, relative_coords: tuple ):
    surf_size = relative_surface.get_size()
    return (int(surf_size[0]*relative_coords[0]),int(surf_size[1]*relative_coords[1]))

def get_relative_size( relative_surface: pygame.Surface, relative_size: tuple):
    surf_size = relative_surface.get_size()
    return ( int(surf_size[0]*relative_size[0]), int(surf_size[1]*relative_size[1]) )

# Relative scaling for the case in which aspect reatio has to preserved 
def preserved_relative_scaling( relative_surface: pygame.Surface, sub_surface: pygame.Surface, relative_scale: int, ):
    surf_size = relative_surface.get_size()
    surf_area = surf_size[0]*surf_size[1]
    sub_surf_size = sub_surface.get_size()
    sub_surf_width_ratio = sub_surf_size[0]/(sub_surf_size[0] + sub_surf_size[1])
    sub_surf_height_ratio = 1 - sub_surf_width_ratio
    return( surf_area*relative_scale*sub_surf_width_ratio, surf_area*relative_scale*sub_surf_height_ratio)


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

# Method changes coordinates so that an smaller surface is centered on the coordinates on the blitted surface
def adjust_to_center_surface( coordinates: tuple, surface: pygame.Surface):
    surf_size = surface.get_size()
    return (( coordinates[0]- (surf_size[0] * 0.5)), ( coordinates[1] - (surf_size[1] * 0.5) ) )

# Method centers drawn objects
def adjust_to_center_draw( coordinates: tuple, draw_size: tuple):
    return (( coordinates[0]- (draw_size[0] * 0.5)), ( coordinates[1] - (draw_size[1] * 0.5) ) )