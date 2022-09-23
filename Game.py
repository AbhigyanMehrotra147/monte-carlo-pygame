
import pygame
from time import time
import math

class Game( object ):

    def __init__( self ):
        self._TITLE = " Monte Carlo Beer Simulation "
        self._WIDTH = 1200
        self._HEIGHT = 760
        self._FLAGS = pygame.RESIZABLE

        self._SIZE = ( self._WIDTH, self._HEIGHT )
        self._BCK_COL = [ 255, 2, 0 ]
        self._NUM_IMAGES = 5
        self._SURFACES = []
        self._FPS = 15

        self._running = True
        self._window = None
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

            self._window = pygame.display.set_mode( size= self._SIZE, flags= self._FLAGS, depth= 1, display= 0, vsync= 0 )
            pygame.display.set_caption( self._TITLE )
            self._clock = pygame.time.Clock()

            self._background = Background( screen = self._window )

            self._LawLarge = LawLarge(pos_x = self._WIDTH - 400, pos_y = 10, width = 250, height = 150, color_rect = (60,60,60), color_line = (200,200,200), file_path = "temp.txt", )
            self._LawLarge.initialize()
            # self._ash = Person( cur_x = self._WIDTH/(3/2), cur_y= self._HEIGHT/(3/2) , image_path = "./boy.png",  json_path= "./boy.json", NUM_FRAMES=5, sprite_index=0, x_name="x", y_name = "y", width_name = "width", height_name = "height" )

            self._prev_time = time()

        return success

    def _update( self ):

        self._background.update()
        # self._ash.move( screen = self._window, dx= -float( 10 * self._delta_T ), dy= -1)

    def _render( self ):

        self._background.render_background( screen = self._window )
        # self._ash.render( self._window )
        self._background.render_hue( self._window )
        self._LawLarge.render(screen = self._window )


        # fps_text = pygame.font.SysFont( "impact", 50 ).render( str(cur_fps), 1, (0,0,0))
        # self._window.blit( fps_text, ( self._WIDTH / 2, 100) )

        pygame.display.update()

        self._clock.tick_busy_loop( self._FPS )
        cur_fps = self._clock.get_fps()

    def _handle_events( self ):
        # The event loop
        for event in pygame.event.get():
            if( event.type == pygame.QUIT ):
                self._running = False

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
                self._update()
                self._render()

        self._clean()
        print( 'Exited game instance!' )


    def _clean( self ):
        # needs to delete / free elements
        # quits pygame sub-systems
        pygame.quit()
