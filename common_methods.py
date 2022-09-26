import pygame

def get_relative_coords( relative_surface: tuple, relative_coords: tuple ):
    surf_size = relative_surface.get_size()
    return (surf_size[0]*relative_coords[0],surf_size[1]*relative_coords[1])