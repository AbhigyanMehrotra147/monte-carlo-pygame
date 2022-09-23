import pygame

class LawLarge( object ):

    def __init__( self, pos_x: float, pos_y: float, width: float, height: float, color_rect: tuple,color_line: tuple, file_path: str):
        self._pos = (pos_x,pos_y)
        self._size = (width,height)
        self._border_radius = 0
        self._file_path = file_path
        self._color_rect = color_rect
        self._list_bool = []
        self._list_index = 0
        self._rect = None
        self._formula = None
        

    def initialize( self ):
        self._border_radius = int((self._size[0] + self._size[1])/5)

        self._read_file( file_mode = 'r')

        self._create_rect()
        self._create_line()


    def _read_file( self, file_mode: str ):
        file = open(self._file_path,file_mode)
        temp_str = ""
        for line in file:
            temp_str += line
        self._list_bool = list(temp_str.split( " " ))
    
    # Creates the number line
    def _create_line( self ):
        pass
    # Creates he rectangle where probability and the equation are displayed
    def _create_rect( self ):
        self._surface_rect = pygame.Surface( size = self._size ).convert_alpha()
        self._rect = pygame.Rect(( self._pos ),( self._size ))
        pass
    def _update():
        list_index += 1
    
    def _create_formula():
        
    def _render_line():
        pass
    def _rend_rect( self, screen: pygame.Surface):
        self._surface_rect.fill( color = self._color_rect )
        pygame.draw.line( surface = self._surface_rect, color = (220,200,200), start_pos = (0,self._size[1]/2), end_pos=(self._size[0],self._size[1]/2), width = 5   )
        pygame.draw.line( surface = self._surface_rect, color = (220,200,200), start_pos = (self._size[0]/2,0), end_pos=(self._size[0]/2,self._size[1]/2), width = 5   )
        screen.blit( source = self._surface_rect, dest = self._rect )
        # pygame.draw.rect( surface = screen, color=self._color_rect, rect = self._rect, border_radius = self._border_radius )
        
    def render( self, screen: pygame.Surface ):
        self._rend_rect( screen = screen )
        pass
