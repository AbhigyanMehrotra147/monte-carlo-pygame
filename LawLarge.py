from asyncore import read
import pygame

class LawLarge( object ):

    def __init__( self, pos_x: float, pos_y: float, width: float, height: float, color_rect: tuple,color_line: tuple, monte_file_path: str, formula_image_path: str, number_of_dots: int, smiley_address: str ):
        self._POS = (pos_x,pos_y)
        self._SIZE = (width,height)
        self._border_radius = 0
        self._color_rect = color_rect
        self._rect = None
        self._surface = None

        self._formula_surface = None
        self._formula_rect = None
        self._formula_image_path = formula_image_path

        self._list_bool = []
        self._list_index = 0

        self._monte_file_path = monte_file_path

        self._line_surface = None
        self._color_line = color_line
        self._number_of_dots = number_of_dots

        self._happy_smiley = pygame.image.load( smiley_address + "happy_smiley.png" )
        self._sad_smiley = pygame.image.load( smiley_address + "sad_smiley.png" )
        self._smiley_address = smiley_address
    
    def initialize( self ):
        self._border_radius = int((self._SIZE[0] + self._SIZE[1])/5)

        self._read_file( file_mode = 'r')
        self._create_rect()
        self._create_line( surf_size =  ( self._SIZE[0]*0.9,self._SIZE[1]*0.3 ), smiley_size = (30,30) )
        self._create_formula()



    def _read_file( self, file_mode: str ):
        file = open(self._monte_file_path,file_mode)
        temp_str = ""
        for line in file:
            temp_str += line
        self._list_bool = list(temp_str.split( " " ))
        self._list_bool = [int(i) for i in self._list_bool]

    # Creates the number line
    def _create_line( self, surf_size, ):
        self._line_surface = pygame.Surface( size = surf_size )
        self._line_rect = self._line_surface.get_rect()
        self._list_bool = [int(i) for i in self._list_bool]

    def _select_smilie( self,index: int):
 
        if self._list_bool[index] == 0:
            return self._sad_smiley
        else:
            return self._happy_smiley


    # Creates the surface and rectangle on whch the number line will be displayed along with 
    
    def _scale_smiley( self, smiley_size: tuple):
        self._happy_smiley = pygame.transform.scale( surface = self._happy_smiley, size = smiley_size )
        self._sad_smiley = pygame.transform.scale( surface = self._sad_smiley, size = smiley_size)

    def _create_line( self, surf_size: tuple, smiley_size: tuple ):
        self._line_surface = pygame.Surface( size = surf_size )
        self._line_surface.set_colorkey( self._color_rect ) 
        self._line_rect = self._line_surface.get_rect()
        self._scale_smiley( smiley_size = smiley_size )

    # Creates the and surface rectangle where probability and the equation are displayed
    def _create_rect( self ):
        self._surface = pygame.Surface( size = self._SIZE )
        self._rect = pygame.Rect( self._POS, self._SIZE )
        pass


    def _create_formula( self ):
        self._formula_surface = pygame.image.load( self._formula_image_path )
        temp_size = self._formula_surface.get_size()
        self._formula_surface = pygame.transform.scale( surface = self._formula_surface, size = ( temp_size[0]/1.5, temp_size[1]/1.5 ))
        self._formula_rect = self._formula_surface.get_rect()

    def _get_blit_pos( self, relative_pos: tuple ):
        return ((self._POS[0] + self._SIZE[0]*relative_pos[0]),(self._POS[1] + self._SIZE[1]*relative_pos[1]))

    def _get_draw_rel_pos( self, relative_pos: tuple, relative_surf: pygame.Surface ):
        surf_size = relative_surf.get_size()
        return (surf_size[0]*relative_pos[0],surf_size[1]*relative_pos[1])

    def _draw_dots( self, surface: pygame.Surface, dot_colors: tuple, start_pos: tuple, end_pos: tuple, dot_radius: float ):
        line_length = abs(start_pos[0] - end_pos[0])
        gap = int(line_length/(self._number_of_dots+2))
        y_coord = start_pos[1]
        for i in range(int(start_pos[0]+gap),int(end_pos[0]-gap),gap):
            pygame.draw.circle(surface = surface, color = dot_colors, center = (start_pos[0]+i,y_coord), radius = dot_radius, width = 0 )

    def _draw_smiley( self, line_start_pos: tuple, line_end_pos: tuple):

        line_length = abs(line_start_pos[0]-line_end_pos[0])
        gap = int(line_length/(self._number_of_dots + 2))
        j = self._list_index
        smiley_size = self._sad_smiley.get_size()
        y_coord = (line_start_pos[1] - smiley_size[1]*0.5)
        x_coord = (line_start_pos[0] + gap - smiley_size[0]*0.5)
        for i in range(int(line_start_pos[0] + gap), int(line_end_pos[0] - gap), gap):
            smiley = self._select_smilie(j)
            self._line_surface.blit( source = smiley, dest = (x_coord, y_coord) )
            x_coord += gap
            j+=1

    def _render_formula( self, screen: pygame.Surface, relative_formula_pos: tuple ):
        formula_pos = self._get_blit_pos( relative_pos = relative_formula_pos )
        screen.blit( source = self._formula_surface, dest = formula_pos )

    def _render_line( self, screen: pygame.Surface, numb_rel_start_pos: tuple, numb_rel_end_pos: tuple, line_width: int, rect_relative_pos: tuple,transparency: int, dot_colors: tuple, dot_radius: int ):
        self._line_surface.fill(color=self._color_rect)
        # line_start and line_end position are relative to the line_surface here 
        line_start_pos = self._get_draw_rel_pos( relative_pos = numb_rel_start_pos, relative_surf = self._line_surface )
        line_end_pos = self._get_draw_rel_pos( relative_pos = numb_rel_end_pos, relative_surf = self._line_surface )
        rect_pos = self._get_blit_pos(relative_pos = rect_relative_pos)
        self._line_rect.update(rect_pos,(self._line_surface.get_size()))
        self._line_surface.set_alpha( transparency )
        pygame.draw.line( surface = self._line_surface, color = self._color_line, start_pos = line_start_pos, end_pos = line_end_pos, width = line_width )
        self._draw_dots( surface = self._line_surface, dot_colors = dot_colors, dot_radius = dot_radius, start_pos = line_start_pos, end_pos = line_end_pos )
        self._draw_smiley( line_start_pos = line_start_pos, line_end_pos = line_end_pos )
        screen.blit( source = self._line_surface, dest = self._line_rect )
        
    def _rend_rect( self, screen: pygame.Surface, line_color: int, rel_start_pos_h: tuple, rel_end_pos_h: tuple, rel_start_pos_v: int, rel_end_pos_v: int,  line_width: int, transparency: int ):
        self._surface.fill( color = self._color_rect )
        hline_start_pos = self._get_draw_rel_pos( relative_pos = rel_start_pos_h, relative_surf = self._surface )
        hline_end_pos = self._get_draw_rel_pos(relative_pos = rel_end_pos_h,relative_surf = self._surface )
        vline_start_pos = self._get_draw_rel_pos( relative_pos = rel_start_pos_v,relative_surf = self._surface )
        vline_end_pos = self._get_draw_rel_pos(relative_pos = rel_end_pos_v, relative_surf = self._surface )
        pygame.draw.line( surface = self._surface, color = line_color, start_pos = hline_start_pos , end_pos = hline_end_pos , width = line_width )
        pygame.draw.line( surface = self._surface, color = line_color, start_pos = vline_start_pos , end_pos = vline_end_pos , width = line_width )
        self._surface.set_alpha( transparency )
        screen.blit( source = self._surface, dest = self._rect )
        

    def _update_index( self ):

        if (self._list_index < (len(self._list_bool) - self._number_of_dots*2 - 1)):
            self._list_index += 1
        else:
            self._list_index = 0


    def render( self, screen: pygame.Surface ):
        self._render_formula( screen = screen, relative_formula_pos = (0.53,0.05))
        self._render_line( screen = screen, numb_rel_start_pos = (0,0.7), numb_rel_end_pos = (1,0.7), \
            line_width = 4, rect_relative_pos = (0.05,0.6), transparency = 255, dot_colors = (0,0,0), dot_radius = 4 )
        self._rend_rect( screen = screen, line_color = (200,200,200), rel_start_pos_h = (0,0.5), rel_end_pos_h = \
            (1,0.5), rel_start_pos_v = (0.5,0), rel_end_pos_v = (0.5,0.5), line_width=5, transparency = 60 )
        self._update_index()

