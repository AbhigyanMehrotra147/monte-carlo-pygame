import pygame

class LawLarge( object ):

    def __init__( self, pos_x: float, pos_y: float, width: float, height: float, color: tuple, file_path: str):
        self._pos = (pos_x,pos_y)
        self._size = (width,height)
        self._border_radius = 0
        self._file_path = file_path
        self._color = color
        self._list_bool = []
        self._list_index = 0
        self._rect = None

    def initialize( self ):
        self._border_radius = int((self._size[0] + self._size[1])/5)

        self._read_file( file_mode = 'r')

        self._creat_rect()
        self._creat_line()


    def _read_file( self, file_mode: str ):
        file = open(self._file_path,file_mode)
        temp_str = ""
        for line in file:
            temp_str += line
        self._list_bool = list(temp_str.split( " " ))
    
    
    def _creat_line( self ):
        pass
    def _creat_rect( self ):
        self._rect = pygame.Rect((self._pos),(self._size))
        pass
    def _update():
        list_index += 1
    
    def _render_line():
        pass
    def _rend_rect( self, screen: pygame.Surface):
        pygame.draw.rect( surface = screen, color=self._color, rect = self._rect, border_radius = self._border_radius )
        pass
    def render(self, screen: pygame.Surface):
        self._rend_rect( screen = screen)
        pass
