import pygame
from common_methods import get_relative_coords, get_relative_size


# Beerline surface will be blitted on BeerDepict surface
# The position of the beerline surface will by default be relative to the BeerDepict surface
class BeerLine:
    # The capital arguments suggest that the value remain constant during execution
    # Line coordinates are given as a list in which both relative start_pos and relative_pos are specified as seperate tuples 
    def __init__( self, blit_surface: pygame.Surface, SIZE: tuple, POS: tuple, COLOR: tuple, line_coords: list, line_color: tuple, line_width: float, \
        sad_dot_colors: float, sad_dot_radius: float, happy_dot_colors: tuple, happy_dot_radius: float, \
             popsickle_color: tuple, popsickle_width: float, popsickle_end_pos, \
                sad_smiley_pos: tuple, happy_smiley_pos: tuple, sad_smiley_size: tuple, happy_smiley_size, smiley_address ):
        
        self._blit_surface = blit_surface
        self._surface = None
        self._rect = None
        
        # Attributes for the surface 
        self._POS = POS
        self._SIZE = SIZE
        self._COLOR = COLOR

        # Attributes for the line
        self._line_start_pos = line_coords[0]
        self._line_end_pos = line_coords[1]
        self._line_color = line_color
        self._line_width = line_width

        # Attributes for the dots
        self._sad_dot_colors = sad_dot_colors
        self._sad_dot_radius = sad_dot_radius
        self._happy_dot_colors = happy_dot_colors
        self._happy_dot_radius = happy_dot_radius

        # Attributes for the popsickle
        self._popsickle_color = popsickle_color
        self._popsickle_width = popsickle_width
        self._popsickle_end_pos = popsickle_end_pos

        # Attributs for the smiley
        self._sad_smiley = None
        self._happy_smiley = None
        self._smiley_address = smiley_address
        self._sad_position = sad_smiley_pos
        self._happy_position = happy_smiley_pos
        self._sad_smiley_Size = sad_smiley_size
        self._happy_smiley_size = happy_smiley_size


    
    def _create_surf( self ):
        self._POS = get_relative_coords( relative_surface = self._blit_surface, relative_coords= self._POS ) 
        self._SIZE = get_relative_size( relative_surface = self._blit_surface, relative_size = self._SIZE )
        self._surface = pygame.Surface( size = self._SIZE )
        self._surface.set_colorkey( self._COLOR )
        self._rect = pygame.Rect( self._POS, self._SIZE)

    def _create_line( self ):
        self._line_start_pos = get_relative_coords( relative_surface = self._surface, relative_coords = self._line_start_pos )
        self._line_end_pos  = get_relative_coords( relative_surface = self._surface, relative_coords = self._line_end_pos )

    def _create_smiley( self ):
        
        # Scaling and storing sad smiley
        self._sad_smiley = pygame.image.load( self._smiley_address + "sad_smiley.png" )
        self._sad_smiley = pygame.transform.scale( surface = self._sad_smiley, size = self._sad_smiley_Size )
        
        # Scaling and storing happy smiley
        self._happy_smiley = pygame.image.load( self._smiley_address + "happy_smiley.png" )
        self._happy_smiley_size = pygame.transform.scale( surface = self._happy_smiley, size = self._happy_smiley_size)
    
    def create( self ):
        self._create_surf()
        self._create_line()
        self._create_smiley()
    

    def _render_line( self ):
        # Drawing line on surface
        pygame.draw.line( surface = self._surface, color = self._line_color, start_pos = self._line_start_pos, \
            end_pos= self._line_end_pos, width = self._line_width )
    
    def _render_surface( self ):

        self._surface.fill( self._COLOR )
        

        
    def render( self ):
        # Rendering all objects in the surface
        # The sequence of drawing is very important
        self._render_surface()
        self._render_line()
        self._blit_surface.blit( source = self._surface, dest = self._rect )
        