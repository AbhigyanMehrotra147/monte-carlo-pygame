
line_surface_coords = (0.1,0.65)
line_surface_size = (0.8,0.3)
line_surface_color = None 

line_coords = [(0.1,0.9),(0.9,0.9)]
line_color = (20,20,20)
line_width = 5

happy_dot_color = (100,220,100)
happy_dot_size = 5

sad_dot_color = (220,100,100)
sad_dot_size = 5

number_of_dots = 8
dot_pace = 5

# Popsickkle dimensions are relative to beerline surface and not Beerdepict surface
happy_popsickle_color = happy_dot_color
happy_popsickle_length = 0.6

sad_popsickle_color = sad_dot_color
sad_popsicle_length = 0.35

popsickle_width = 0.0075

sad_smiley_pos = (5,5)
sad_smiley_size = (0.1,0.1)
sad_smiley_scale = 0.0015

happy_smiley_pos = (5,5)
happy_smiley_size = (0.1,0.1)
happy_smiley_scale = 0.0015

smiley_address = "./assets/smiley/"

monte_file_path = "temp.txt"

beer_zi_surface_pos = (0,0)
beer_zi_surface = (0.8,0.8)

beer_zi_color = (125,20,78)

beer_zi_pace = 10
beer_number_of_zi = 3



import pygame
from BeerLine import BeerLine
from Beer_Zi import Beer_Zi
from common_methods import get_relative_coords

class DepictBox:

    # The capitalized arguments represent constant values only to assigned once
    # blit screen is the screen on which we will blit our surface
    # Line coordinates are always relative to the surface
    def __init__( self, SIZE: tuple, POS: tuple, BORDER_RADIUS: float, color: tuple, blit_screen: pygame.Surface, h_line_color: tuple, h_line_coords: list, v_line_color: tuple, v_line_coords: list, h_line_width: float, v_line_width: float ):
        
        self._SIZE = SIZE
        self._POS = POS
        self._BORDER_RADIUS = BORDER_RADIUS
        self._color = color
        self._rect = None
        self._surface = None
        self._blit_screen = blit_screen
        
        # Attributes of the horizontal division
        self._h_line_start = h_line_coords[0]
        self._h_line_end = h_line_coords[1]
        self._h_line_width = h_line_width
        self._h_line_color = h_line_color

        # Attributes of the vertical division
        self._v_line_start = v_line_coords[0]
        self._v_line_end = v_line_coords[1]
        self._v_line_width = v_line_width
        self._v_line_color = v_line_color

        self._BeerLine = None
        self._RollingWindow = None

    def create( self ):
        # Creating the surface for the self
        self._create_self()
        
        # The surface is now created and hence can be passes to BeerLine 
        self._BeerLine = BeerLine( blit_surface = self._surface, SIZE= line_surface_size, POS= line_surface_coords,\
            COLOR= self._color, line_coords= line_coords, line_color= line_color, line_width= line_width,\
                sad_dot_colors= sad_dot_color, sad_dot_size= sad_dot_size, happy_dot_colors= happy_dot_color,\
                    happy_dot_size= happy_dot_size, numer_of_dots= number_of_dots, dot_pace= dot_pace,\
                        happy_popsickle_color= happy_popsickle_color, sad_popsickle_color= sad_popsickle_color, popsickle_width= popsickle_width, happy_popsickle_length= happy_popsickle_length, 
                            sad_popsickle_length= sad_popsicle_length, sad_smiley_pos= sad_smiley_pos, sad_smiley_size= sad_smiley_size,\
                                happy_smiley_pos= happy_smiley_pos, happy_smiley_size= happy_smiley_size, smiley_address= smiley_address,\
                                     monte_file_path= monte_file_path )
        
        self._BeerZi = Beer_Zi( blit_surface= self._surface, SIZE= beer_zi_surface, POS= beer_zi_surface_pos, COLOR= beer_zi_color,\
             zi_pace= beer_zi_pace, number_of_zi= beer_number_of_zi, monte_file_path= monte_file_path )

        self._BeerLine.create()
        self._BeerZi.create()

    def _create_self( self ):
        # Setting color key so that the background gets removed gets removed. 
        self._surface = pygame.Surface( size = self._SIZE )
        self._surface.set_colorkey (self._color)
        self._rect = pygame.Rect( self._POS, self._SIZE )
 
        # Getting position of lines to be drawn
        self._h_line_start = get_relative_coords( relative_surface = self._surface, relative_coords = self._h_line_start )
        self._h_line_end = get_relative_coords( relative_surface = self._surface, relative_coords = self._h_line_end )
        self._v_line_start = get_relative_coords( relative_surface = self._surface, relative_coords = self._v_line_start )
        self._v_line_end = get_relative_coords( relative_surface = self._surface, relative_coords = self._v_line_end )
    
    def _update( self ):
        self._RollingWindow.update(  )

    def _render_lines( self ):

        # Drawing action kept seperatly in a function to ease reading
        # Drawing the horizontal and vertical dividers
        pygame.draw.line( surface= self._surface, color= self._h_line_color, start_pos= self._h_line_start, end_pos= self._h_line_end, width=self._h_line_width )
        pygame.draw.line( surface= self._surface, color= self._v_line_color, start_pos= self._v_line_start, end_pos= self._v_line_end, width= self._v_line_width )
    
    def _render_self( self ):
        self._surface.fill( color=self._color )
        self._render_lines()
        # self._BeerLine._blit_surface = self._surface
        
       
    
    # Function will call all renders, including self, BeerLine, Formula and Zi's
    def render( self ):
    
        self._render_self()
        self._BeerZi.render()
        self._BeerLine.render()
        self._blit_screen.blit( source = self._surface, dest = self._rect ) 

        
        