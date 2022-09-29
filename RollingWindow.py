
import pygame
import pygame.image
from matplotlib import pyplot as plt

# for biffering the generated image
import io
from PIL import Image

class RollingWindow( object ):
    """
    For the rolling Zi-s on the left window
    """

    def __init__( self, *, window_size: tuple[ int, int ], fps: int ):

        # worth mentioning here that the self._height has no understanding of self._num_zi below
        # neither does the Zi image generator
        # so the value of the window need to be aptly, of course emperically passed, for num_zi images that the image generator gives of whatever size
        self._width, self._height = window_size

        # should actually be derived from parent class
        self._FPS = fps

        # will be passed into update from the BeerWindow main class, the current i in Zi
        self._cur_index = 0

        # the last updated index, to check when the index is updated, inductively
        self._last_index = self._cur_index

        # will be used internally, passed internally, is used for increasing cur index gradually by delta_T each frame
        self._buf_index = self._cur_index

        # max number of Zis at once, vertically  
        self._num_zi = 4

        # holds the current surface
        self._cur_zi_surf = pygame.Surface( ( self._width, self._height ) ).convert_alpha()
        self._RECT = self._cur_zi_surf.get_rect()

        # the y-scroll-off of the current surface
        self._y_scroll_off = 0

        # file name/location
        self._file_latex = 'zi.png'

        self._speed = 2

        # image buffer,
        # self._img_buf = io.BytesIO()

    def _return_z( self, *, sub_i: str, file: str = 'zi.png', h_s: bool = False, bool_axes: bool = False, font_size: int = 20, pos: tuple = ( 0.25, 0.4 ), fig_size: tuple = ( 2, 1 ) ):
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
        z_fig.get_axes()[ 0 ].set_visible( bool_axes )
        z_fig.tight_layout()

        # save file in buffer
        z_fig.savefig( file )

        # to show the file  
        # plt.show()

        # /Users/pogovishal/Documents/tmp/RollingWindow.py:32: RuntimeWarning: More than 20 figures have been opened. 
        # Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory.
        plt.close( 'all' )

        return None

    def update( self, delta_T ):
        # updates/creates the new image  
        self._return_z( sub_i=self._cur_index, file=self._file_latex )

        # increases the list index, this later on needs to be handled by parent function, this attribute should be derived from the parent  
        self._buf_index += ( 2.1 ) * delta_T  # somehow this works, please do not ask how : (), the hardcoded 2, oof!!
        self._cur_index = int( self._buf_index )

        self._y_scroll_off -= ( self._height / self._num_zi ) * delta_T

    def render( self, screen ):
        # converting the PIL buffer to a pygame surface
        # I am assuming this would be faster then loading the image in every frame
        # img = Image.frombuffer( "L", ( self._width, self._height ), self._img_buf.tostring(), "raw", "L", 0, 1  )
        # mode = self.img.mode
        # size = self.img.size
        # data = self.img.tobytes()
        # self._cur_zi_surf.fill( ( 250, 250, 0 ) )
        if( self._cur_index > self._last_index ):
            """
            this is for when the index actually increases from last time, this is agnostic of how much it increases
            """
            print( 'updated ', self._cur_index, ' ', self._last_index )
            self._last_index = self._cur_index

            # resetting the y scroll
            self._y_scroll_off = 0

            image = pygame.image.load( self._file_latex ).convert_alpha()
            
            image.set_colorkey( ( (255,255,255) ) )
            # this loading makes things slow, I tried doing buffers without success
            self._cur_zi_surf.blit( image, ( 0, self._height * ( self._num_zi - 1 ) / self._num_zi ) )#  0 + ( self._num_zi - 1 ) * self._height / self._num_zi ) )

            # self._cur_zi_surf = self._cur_zi_surf.subsurface( ( 0, 0, self._width, self._height ) )

        else:
            print( 'shifting ', self._y_scroll_off )
            # the y_scroll off increases every frame in update by height / delta_T
            # the non-visible part of the image is also stored till the screen runs
            # self._cur_zi_surf.blit( self._cur_zi_surf, ( 0, self._height / self._num_zi + self._y_scroll_off ), ( 0, self._height / self._num_zi, self._width, self._height * ( self._num_zi - 1 ) / self._num_zi ) )

            # self._cur_zi_surf.fill( ( 0, 0, 0, 0 ) )
            self._cur_zi_surf.blit( self._cur_zi_surf, ( 0, 0 ), ( 0, -1 * self._y_scroll_off, self._width, self._height + self._y_scroll_off ) )

        # screen.blit( self._cur_zi_surf, ( 0, 0 ), self._RECT )
        screen.blit( self._cur_zi_surf, ( 0, 0 ) )

