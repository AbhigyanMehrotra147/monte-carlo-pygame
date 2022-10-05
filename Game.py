
import pygame
from time import time
import math
from Poisson import Poison

Poisson_t = 3
Poisson_lambda = 5
N = 10 ** 3
beer_price = 120

# Depict box 
depict_box_v_line_width = 5
depict_box_v_line_coords = [(0.5,0),(0.5,0.5)]
depict_box_v_line_color = (100,100,100)

depict_box_h_line_width = 5
depict_box_h_line_color = (100,100,100)

depict_box_pos = ( 0.0, 0.0 )

update_index_pace = 5

class Game( object ):

    def __init__( self ):
        self._TITLE = " Monte Carlo Beer Simulation "
        self._WIDTH =  1980
        self._HEIGHT = 1080
        self._FLAGS = pygame.RESIZABLE

        self._SIZE = ( self._WIDTH, self._HEIGHT )
        self._BCK_COL = [ 255, 2, 0 ]
        self._NUM_IMAGES = 5
        self._SURFACES = []
        self._FPS = 1100

        self._running_timer = 1

        self._running = True
        self._window = None

        # the screen for temp blitting and scaling
        self._screen = pygame.Surface( self._SIZE )

        self._clock = None

        self._ash = None
        self._background = None

        self._delta_T = 0
        self._prev_time = 0

    def _initialize( self ):
        success = True

        # initialising pygame subsystems
        pygame.init()

        if( not pygame.get_init() ):
            print( "Error in initializing pygame!" )
            success = False

        else:
            from Person import Person
            from Background import Background
            from LawLarge import LawLarge
            from BeerDepict import DepictBox

            self._window = pygame.display.set_mode( size= self._SIZE, flags= self._FLAGS, depth= 1, display= 0, vsync= 0 )
            pygame.display.set_caption( self._TITLE )
            self._clock = pygame.time.Clock()

            self._background = Background( screen = self._screen )

            self._LawLarge = LawLarge(pos_x = self._WIDTH*0.05, pos_y = self._HEIGHT*0.01, width = 500, height = 300, color_rect = ( 100,100,140 ), \
                color_line = (255,255,255,255), monte_file_path = "temp.txt", formula_image_path = "formula.png", number_of_dots = 6, smiley_address = "./assets/smiley/" )

            # self._ash = Person( cur_x = self._WIDTH/(3/2), cur_y= self._HEIGHT/(3/2) , image_path = "./boy.png",  json_path= "./boy.json", NUM_FRAMES=5, sprite_index=0, x_name="x", y_name = "y", width_name = "width", height_name = "height" )

            self._Poison = Poison( t = Poisson_t, Lambda= Poisson_lambda, N=N, beer_price= beer_price  )
            self._DepictBox = DepictBox( SIZE = (self._WIDTH*0.45,self._HEIGHT*0.28) ,POS = depict_box_pos,BORDER_RADIUS= 10, color=(100,100,100), blit_screen=self._screen, \
                 h_line_color= depict_box_h_line_color, h_line_coords=[(0,0.5),(1,0.5)], h_line_width= depict_box_h_line_width,\
                     v_line_color= depict_box_v_line_color, v_line_coords= depict_box_v_line_coords, v_line_width= depict_box_v_line_width, update_index_pace = update_index_pace, Poison = self._Poison )

            for i in range(100):
                self._Poison.update()

            self._DepictBox.create()
            self._prev_time = time()

        return success

    def _update( self ):

        self._background.update()

        if self._running_timer < update_index_pace:
            self._running_timer += 1
        else:
            self._Poison.update()
            self._running_timer = 1
        # self._ash.move( screen = self._window, dx= -float( 10 * self._delta_T ), dy= -1)

    def _render( self ):

        self._background.render_background( screen = self._screen )
        # self._ash.render( self._window )
        # self._background.render_hue( self._screen )
        # self._LawLarge.render( screen = self._screen )

        self._DepictBox.render()

        # fps_text = pygame.font.SysFont( "impact", 50 ).render( str(cur_fps), 1, (0,0,0))
        # self._window.blit( fps_text, ( self._WIDTH / 2, 100) )
        self._window.fill( ( 0, 0, 0, 1 ) )
        self._window.blit( pygame.transform.scale( self._screen, self._SIZE ), dest = (0,0) )
        pygame.display.update()

        self._clock.tick_busy_loop( self._FPS )
        cur_fps = self._clock.get_fps()

    def _handle_events( self ):
        # The event loop
        for event in pygame.event.get():
            if( event.type == pygame.QUIT ):
                self._running = False
            elif event.type == pygame.VIDEORESIZE:
                # in the running frame it is updated later on:
                print( 'Updated' )
                self._SIZE = event.dict["size"]

    def execute( self ):

        if not self._initialize():
            print( 'Failed to initialise from execute!' )
            self._running = False
        else:
            while( self._running ):

                cur_time = time()
                self._delta_T = cur_time - self._prev_time
                self._prev_time = cur_time

                self._handle_events()
                self._render()
                self._update()

                # pygame.time.delay(0)

        self._clean()
        print( 'Exited game instance!' )

    def _clean( self ):
        # needs to delete / free elements
        # quits pygame sub-systems
        pygame.quit()

