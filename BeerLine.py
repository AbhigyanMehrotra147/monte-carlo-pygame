
from imp import source_from_cache
import pygame
import common_methods as cm


# Beerline surface will be blitted on BeerDepict surface
# The position of the beerline surface will by default be relative to the BeerDepict surface
class BeerLine:
    # The capital arguments suggest that the value remain constant during execution
    # Line coordinates are given as a list in which both relative start_pos and relative_pos are specified as seperate tuples 
    def __init__( self, blit_surface: pygame.Surface, SIZE: tuple, POS: tuple, COLOR: tuple, line_coords: list, line_color: tuple, line_width: float, \
        sad_dot_colors: float, sad_dot_size: float, happy_dot_colors: tuple, happy_dot_size: float, \
            numer_of_dots: tuple, dot_pace: float, happy_popsickle_color: tuple, sad_popsickle_color: tuple, popsickle_width: float, happy_popsickle_length: float, \
                sad_smiley_pos: tuple, happy_smiley_pos: tuple, sad_smiley_size: tuple, happy_smiley_size: tuple, \
                    sad_popsickle_length: float, smiley_address: tuple, monte_file_path: str ):
        
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
        self._sad_dot_size = sad_dot_size
        self._happy_dot_colors = happy_dot_colors
        self._happy_dot_size = happy_dot_size

        # Creating the following class variable to ease moving and rolling the dots
        self._number_of_dots = numer_of_dots
        self._line_length = 0
        self._first_dot_position = 0
        self._dot_gaps = 0
        self._dot_pace = dot_pace
        self._dot_positions = []

        # Attributes for the popsickle
        # The popsickle_length is relative to the surface of the class
        self._happy_popsickle_color = happy_popsickle_color
        self._sad_popsikle_color = sad_popsickle_color
        self._popsickle_width = popsickle_width
        self._happy_popsickle_length = happy_popsickle_length
        self._sad_popsickle_length = sad_popsickle_length
        self._popsickle_end_positions = []

        # Attributs for the smiley
        self._sad_smiley = None
        self._happy_smiley = None
        self._smiley_address = smiley_address
        self._sad_position = sad_smiley_pos
        self._happy_position = happy_smiley_pos
        self._sad_smiley_size = sad_smiley_size
        self._happy_smiley_size = happy_smiley_size

        # Initializing the list of indices
        cm._read_file( file_path = monte_file_path, file_mode = 'r' )

    # rectangle and surface are created in this function
    def _create_surf( self ):

        # Converting Relative positions and coordinates weights to actual relatice position and coordinates
        self._POS = cm.get_relative_coords( relative_surface = self._blit_surface, relative_coords= self._POS )
        self._SIZE = cm.get_relative_size( relative_surface = self._blit_surface, relative_size = self._SIZE )

        self._surface = pygame.Surface( size = self._SIZE )
        # Setting colorkey the same as the color of the surface to kee[ background completely transparent ]
        self._surface.set_colorkey( self._COLOR )
        self._rect = pygame.Rect( self._POS, self._SIZE)

    #  Giving relative acutal positions to starting and ending position of line
    def _create_line( self ):
        self._line_start_pos = cm.get_relative_coords( relative_surface = self._surface, relative_coords = self._line_start_pos )
        self._line_end_pos  = cm.get_relative_coords( relative_surface = self._surface, relative_coords = self._line_end_pos )
    
    # The first_dot tell on which position the first dot should land.
    # the first dot is subtracted by the dot pace after each iteration(blitting)  
    def _create_dots( self ):

        self._line_length = abs(self._line_start_pos[0] - self._line_end_pos[0])
        self._dot_gaps = int(self._line_length/self._number_of_dots)
        self._first_dot_position = self._dot_gaps

        self._dot_pace = self._dot_gaps*self._dot_pace
        # Getting Actual Relative radius for dots
        # self._sad_dot_size = cm.get_relative_size( relative_surface= self._surface, relative_size= self._sad_dot_size )
        # self._happy_dot_size = cm.get_relative_size( relative_surface= self._surface, relative_size= self._happy_dot_size )

    # Getting the actual relative legnths of the popsickles
    # Getting the actual relative width of the popsickle
    def _create_popsickle( self ):
        self._happy_popsickle_length = self._SIZE[1]*self._happy_popsickle_length
        self._sad_popsickle_length = self._SIZE[1]*self._sad_popsickle_length
        self._popsickle_width = int(self._SIZE[0]*self._popsickle_width)

    def _create_smiley( self ):
        
        # Scaling and storing sad smiley
        # Getting the actual relative size for happy smiley from the fractional sizes
        self._sad_smiley = pygame.image.load( self._smiley_address + "sad_smiley.png" )
        self._sad_smiley_size = cm.preserved_relative_scaling( relative_surface = self._surface, relative_scale= 0.003, sub_surface= self._sad_smiley )
        self._sad_smiley = pygame.transform.scale( surface = self._sad_smiley, size = self._sad_smiley_size )
        
        # Scaling and storing happy smiley
        # Getting actual relative size for sad smiley from the fractional sizes
        self._happy_smiley = pygame.image.load( self._smiley_address + "happy_smiley.png" )
        self._happy_smiley_size = cm.preserved_relative_scaling( relative_surface = self._surface, relative_scale= 0.003, sub_surface= self._happy_smiley )
        self._happy_smiley = pygame.transform.scale( surface = self._happy_smiley, size = self._happy_smiley_size)


    # Calling all creates togethor
    def create( self ):
        self._create_surf()
        self._create_line()
        self._create_dots()
        self._create_popsickle()
        self._create_smiley()


    def _render_self( self ):
        self._surface.fill( self._COLOR ) 
    
    def _render_line( self ):
        # Drawing line on surface
        pygame.draw.line( surface = self._surface, color = self._line_color, start_pos = self._line_start_pos, \
            end_pos= self._line_end_pos, width = self._line_width )
    
    # Rendering dots
    # Dots will be rolling on the screen
    # Will return dot position array and pass it to _render_popsickle
    def _render_dots( self ):
        x_coord = self._line_start_pos[0] + self._first_dot_position
        y_coord = self._line_start_pos[1]
        self._dot_positions= []
        j = cm.list_index
        dot_center = ( x_coord, y_coord )
        for i in range( int(x_coord), int(self._line_end_pos[0] ), self._dot_gaps):
            if( cm.list_bool[j] == 1 ):
                pygame.draw.circle( surface= self._surface, color= self._happy_dot_colors, center= dot_center,\
                    radius= self._happy_dot_size, width= 0 )
            else:
                pygame.draw.circle( surface= self._surface, color= self._sad_dot_colors, center= dot_center,\
                    radius= self._sad_dot_size, width= 0 )
            self._dot_positions.append(dot_center)
            x_coord += self._dot_gaps
            dot_center = ( x_coord,y_coord )
            j+=1

    # Rendering popsickle
    # happy and sad popsickle will have different heights 
    def _render_popsickle( self ):
        # Depending on i the type of popsickle will be blitted
        i = cm.list_index

        self._popsickle_end_positions = []

        end_coord = None
        for coordinate in self._dot_positions:
            
            # Adjusting coordinates with size of popsickle 
            coordinate = (coordinate[0], coordinate[1])
            
            if( cm.list_bool[i] ) == 1:
                end_coord = ( coordinate[0], coordinate[1] - self._happy_popsickle_length )
                pygame.draw.line( surface= self._surface, color= self._happy_popsickle_color, start_pos= coordinate,\
                    end_pos= end_coord, width= self._popsickle_width )
            else:
                end_coord = ( coordinate[0], coordinate[1] - self._sad_popsickle_length )
                pygame.draw.line( surface = self._surface, color= self._sad_popsikle_color, start_pos= coordinate,\
                    end_pos= end_coord, width= self._popsickle_width )
            
            # Stroing end positions to be passed to _render_smiley
            self._popsickle_end_positions.append(end_coord)
            i+=1
    
    def _render_smiley( self ):
        # Depending on i happy or sad smiley will be blitted
        i = cm.list_index
        for coordinate in self._popsickle_end_positions:
            
            if( cm.list_bool[i] == 1 ):
                # Adjusting coordinates to the center
                coordinate = cm.adjust_to_center_draw( coordinates= coordinate, draw_size= self._happy_smiley_size )
                self._surface.blit( source= self._happy_smiley, dest= coordinate )
            else:
                coordinate = cm.adjust_to_center_draw( coordinates= coordinate, draw_size= self._sad_smiley_size)
                self._surface.blit( source= self._sad_smiley, dest= coordinate )
            # print(coordinate)
            i+=1


    # Updating self._first_dot_position
    def _update_dot_position( self ):
        if self._first_dot_position <= self._happy_dot_size:
            self._first_dot_position = self._dot_gaps
            cm._update_index( number_of_dots= self._number_of_dots)
        else:
            self._first_dot_position -= self._dot_pace

    def _update( self ):
        self._update_dot_position()


    def render( self ):
        # Rendering all objects in the surface
        # The sequence of drawing is very important
        self._render_self()
        self._render_line()
        self._render_dots()
        self._render_popsickle()
        self._render_smiley()
        self._blit_surface.blit( source = self._surface, dest = self._rect )
        self._update()
        