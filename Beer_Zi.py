
from numpy import source
import pygame
import common_methods as cm
import matplotlib.pyplot as plt

class Beer_Zi:

    # Blit surface is surface on which zi's will be built togethor 
    # The position of the Beerzi surface will by default be relative to the BeerDepict(blit_surface) surface
    # The size is relative to blit_surface
    def __init__( self, blit_surface: pygame.Surface , SIZE: tuple, POS: tuple, COLOR: tuple, number_of_zi , zi_pace: float,\
                monte_file_path: str ):

        # Initializing all required variables and constants

        self._blit_surface = blit_surface

        # Surface and rectangle for the rect
        self._surface = None
        self._rect = None

        self._SIZE = SIZE
        self._POS = POS

        self._COLOR = COLOR

        # zi attributes
        self._number_of_zi = number_of_zi
        self._zi_pace = zi_pace
        self._zi_size = None
        self._zi_y_pos = 0
        self._zi_path = "zi.png"
        self._zi_color = (255,255,255)
        # zi_first_blit is where the first image of zi will be blit in each iteration on the screen
        self._zi_first_blit = None
        # Array storing the current imagetemp_image.set_colorkey( self._zi_color )s of zi's

        self._current_zi_array = []
        # Initializing the list of indices
        cm._read_file( file_path = monte_file_path, file_mode = 'r' )

        self._list_index = 0
        self._list_bool = [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]

    # Creating surface and rectangle for the class
    # Making surface completly transparent

    def _create_self( self ):

        self._SIZE = cm.get_relative_size( relative_surface= self._blit_surface , relative_size= self._SIZE )
        self._POS = cm.get_relative_coords( relative_surface= self._blit_surface , relative_coords= self._POS )
        self._surface = pygame.Surface( size= self._SIZE )
        self._surface.set_colorkey( self._COLOR )
        self._rect = pygame.Rect( self._POS, self._SIZE)

    def _create_zi( self ):

        self._zi_y_pos = (self._SIZE[1]*((self._number_of_zi - 1)/self._number_of_zi))
        self._zi_first_blit = self._zi_y_pos
        temp_size = None
        for i in range( self._number_of_zi + 1):

            self._return_z( sub_i = self._list_bool[i], file= self._zi_path, h_s= self._list_bool[self._list_index] )

            temp_image = pygame.image.load( self._zi_path )
            temp_size = temp_image.get_size()
            temp_image.set_colorkey( self._zi_color )
            temp_image = pygame.transform.scale( surface= self._surface , size= ( temp_size[0], self._SIZE[1]/self._number_of_zi  )  )
            self._current_zi_array.append( temp_image )
            # self._blit_surface.bli

        self._zi_size = ( temp_size[0], self._SIZE[1]/self._number_of_zi )

        self._zi_pace = self._zi_size[1]*self._zi_pace + 2
    
    def create( self ):
        self._create_self()
        self._create_zi()

    def _shift_zi( self ):
        self._current_zi_array.pop(0)
        self._return_z( sub_i = self._list_index, h_s= self._list_bool[self._list_index] )
        temp_image = pygame.image.load( self._zi_path )
        temp_image = pygame.transform.scale( surface= temp_image, size= ( self._zi_size[ 0 ], temp_image.get_size()[ 1 ] ) )
        temp_image.set_colorkey( self._zi_color )
        self._current_zi_array.append( temp_image )
        cm._update_index_zi( number_of_zi= self._number_of_zi)

    def _update_zi( self ):

        if self._zi_y_pos > self._zi_first_blit + self._zi_pace - self._zi_size[1] :
            self._zi_y_pos -= self._zi_pace
        else:
            self._zi_y_pos = int(self._SIZE[1]*((self._number_of_zi - 1)/self._number_of_zi))
            self._shift_zi()
    


    def _return_z( self, sub_i: str, file: str = 'zi.png', h_s: bool = False,  font_size: int = 30, pos: tuple = ( 0, 0.4 ), fig_size: tuple = ( 2, 2 ) ):


        """
        Saves the current figure in the IO buffer as png, not quite, changed so that saves image
        """
        # latex text
        cur_tex = r"$Z_{" + str( sub_i ) + r"} = {" + str( int( h_s ) ) + r"}$"

        # Add the text s to the Axes at location x, y in data coordinates. Returns instance of Text
        z_fig = plt.figure( figsize = fig_size )
        z_fig.text( pos[ 0 ], pos[ 1 ], cur_tex, fontsize=font_size )

        # hide axes
        fig = z_fig.gca()
        z_fig.get_axes()[ 0 ].set_visible( False )
        z_fig.tight_layout()

        # save file in buffer
        z_fig.savefig( file )

        # to show the file  
        # plt.show()
        

        # /Users/pogovishal/Documents/tmp/RollingWindow.py:32: RuntimeWarning: More than 20 figures have been opened. 
        # Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory.
        
        plt.close( 'all' )

        # Performing convolution
        cm.make_mono()

        return None

    def _render_zi( self ):
        i = self._number_of_zi
        for y_coord in range( int( self._zi_y_pos ), int( -self._zi_size[1] ) , int( -self._zi_size[1] ) ):
            self._surface.blit( source= self._current_zi_array[i], dest= (0,y_coord) )
            i -= 1
        
        
        self._update_zi()

    def _render_self( self ):
        self._surface.fill( self._COLOR )
        

    def render( self, Poison):

        self._list_index = Poison.get_cur_index() - 95
        self._list_bool = Poison.get_list()

        self._render_self()
        self._render_zi()
        self._blit_surface.blit( source = self._surface, dest= self._rect )
