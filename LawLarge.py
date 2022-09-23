import pygame

class LawLarge( object ):

    def __init__( self, pos_x: float, pos_y: float, width: float, height: float, color_rect: tuple,color_line: tuple, monte_file_path: str, formula_image_path: str):
        self._pos = (pos_x,pos_y)
        self._size = (width,height)
        self._border_radius = 0
        self._color_rect = color_rect
        self._rect = None
        self._surface = None

        self._formula_surface = None
        self._formula_image_path = formula_image_path

        self._list_bool = []
        self._list_index = 0

        self._monte_file_path = monte_file_path

        self._line_surface = None
        self._color_line = color_line

    def initialize( self ):
        self._border_radius = int((self._size[0] + self._size[1])/5)

        self._read_file( file_mode = 'r')

        self._create_rect()
        self._create_line( surf_size =  ( self._size[0]*0.9,self._size[1]*0.3 ) )
        self._create_formula()


    def _read_file( self, file_mode: str ):
        file = open(self._monte_file_path,file_mode)
        temp_str = ""
        for line in file:
            temp_str += line
        self._list_bool = list(temp_str.split( " " ))
    
    # Creates the number line
    def _create_line( self, surf_size, ):
        self._line_surface = pygame.Surface( size = surf_size )
        self._line_rect = self._line_surface.get_rect()

    # Creates the rectangle where probability and the equation are displayed
    def _create_rect( self ):
        self._surface = pygame.Surface( size = self._size )
        self._rect = pygame.Rect( self._pos, self._size )
        pass


    
    def _create_formula( self ):
        self._formula_surface = pygame.image.load( self._formula_image_path )
        temp_size = self._formula_surface.get_size()
        self._formula_surface = pygame.transform.scale( surface = self._formula_surface, size = ( temp_size[0]/1.5, temp_size[1]/1.5 ))


    def _render_formula( self, screen: pygame.Surface, surface_pos: tuple ):
        screen.blit( source = self._formula_surface, dest = surface_pos )

    def _render_line( self, screen: pygame.Surface, start_pos: tuple, end_pos: tuple, line_width: int, surface_pos: tuple ):
        surf_size = self._line_surface.get_size()
        pygame.draw.line( surface = self._line_surface, color = self._color_line, start_pos = (surf_size[0]*start_pos[0], surf_size[1]*start_pos[1]), end_pos = (surf_size[0]*end_pos[0], surf_size[1]*end_pos[1]), width = line_width )
        self._line_rect.top = (self._pos[0],self._pos[1])
        # self._line_rect.center = ((self._pos[0] + self._size[0])*0.5,(self._pos[1] + self._size[1])*0.8) 
        screen.blit( source = self._line_surface, dest = self._line_rect )

        pass
    def _rend_rect( self, screen: pygame.Surface, line_color: int, start_pos_h: tuple, end_pos_h: tuple, start_pos_v: int, end_pos_v: int,  line_width: int ):
        self._surface.fill( color = self._color_rect )
        pygame.draw.line( surface = self._surface, color = line_color, start_pos = start_pos_h , end_pos = end_pos_h , width = line_width   )
        pygame.draw.line( surface = self._surface, color = line_color, start_pos = start_pos_v , end_pos = end_pos_v , width = line_width   )
        screen.blit( source = self._surface, dest = self._rect )
        self._surface.set_alpha( 60 )
        # pygame.draw.rect( surface = screen, color=self._color_rect, rect = self._rect, border_radius = self._border_radius )

    def _update():
        list_index += 1

    def render( self, screen: pygame.Surface ):
        self._render_formula( screen = screen, surface_pos = ( self._pos[0] + self._size[0]/(1.9), self._pos[1] + self._size[1]/20 ) )
        self._render_line( screen = screen, start_pos = (0.1,0.7), end_pos = (0.9,0.7), line_width = 4, surface_pos = (self._size[0]*0.1, self._size[1]*0.6 ) )
        self._rend_rect( screen = screen, line_color = (200,200,200), start_pos_h = (0,self._size[1]/2), end_pos_h = \
            (self._size[0],self._size[1]/2), start_pos_v = (self._size[0]/2,0), end_pos_v = (self._size[0]/2,self._size[1]/2), line_width=5 )

        
        pass
