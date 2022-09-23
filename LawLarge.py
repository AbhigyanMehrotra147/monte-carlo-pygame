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
    def initialize( self ):
        self._border_radius = int((self._size[0] + self._size[1])/5)

        self._read_file( file_mode = 'r')

        self._create_rect()
        self._create_line()
        self._create_formula()


    def _read_file( self, file_mode: str ):
        file = open(self._monte_file_path,file_mode)
        temp_str = ""
        for line in file:
            temp_str += line
        self._list_bool = list(temp_str.split( " " ))
    
    # Creates the number line
    def _create_line( self ):
        pass

    # Creates the rectangle where probability and the equation are displayed
    def _create_rect( self ):
        self._surface = pygame.Surface( size = self._size )
        self._surface.set_alpha( 60 )
        self._rect = pygame.Rect( ( self._pos ), ( self._size ) )
        pass

    def _update():
        list_index += 1
    
    def _create_formula( self ):
        self._formula_surface = pygame.image.load( self._formula_image_path )
        temp_size = self._formula_surface.get_size()
        self._formula_surface = pygame.transform.scale( surface = self._formula_surface, size = ( temp_size[0]/1.5, temp_size[1]/1.5 ))


    def _render_line():
        pass
    def _rend_rect( self, screen: pygame.Surface):
        self._surface.fill( color = self._color_rect )
        pygame.draw.line( surface = self._surface, color = (220,200,200), start_pos = (0,self._size[1]/2), end_pos=(self._size[0],self._size[1]/2), width = 5   )
        pygame.draw.line( surface = self._surface, color = (220,200,200), start_pos = (self._size[0]/2,0), end_pos=(self._size[0]/2,self._size[1]/2), width = 5   )
        screen.blit( source = self._surface, dest = self._rect )
        screen.blit( source = self._formula_surface, dest = ( self._pos[0] + self._size[0]/(1.9), self._pos[1] + self._size[1]/20 ) )
        # pygame.draw.rect( surface = screen, color=self._color_rect, rect = self._rect, border_radius = self._border_radius )
        
    def render( self, screen: pygame.Surface ):
        self._rend_rect( screen = screen )
        pass
