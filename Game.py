
import pygame
import time
import math

class Game( object ):

    def __init__( self ):
        self._TITLE = " Monte Carlo Beer Simulation "
        self._WIDTH = 640
        self._HEIGHT = 480
        self._FLAGS = pygame.RESIZABLE

        self._SIZE = ( self._WIDTH, self._HEIGHT )
        self._BCK_COL = [ 255, 2, 0 ]
        self._NUM_IMAGES = 5
        self._SURFACES = []
        self._FPS = 5

        self._running = True
        self._window = None
        self._clock = None

        self._ash = None

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

            self._window = pygame.display.set_mode( size=self._SIZE, flags=self._FLAGS, depth=0, display=0, vsync=0 )
            pygame.display.set_caption( self._TITLE )
            self._clock = pygame.time.Clock()

            self._ash = Person( cur_x= 0, cur_y= self._HEIGHT/2, image_path = "./trainer_sheet.png",  json_path= "./trainer_sheet.json", NUM_FRAMES=5, sprite_index=0 )

            self._prev_time = time.time()

        return success

    def _update( self ):

        self._ash.move( dx= float( 50 * self._delta_T ), dy= 50 * math.sin( self._ash.cur_x ) )
        self._ash._sprite_index += 1

    def _render( self ):
 
        # clearing the window
        self._window.fill( self._BCK_COL )

        # changing the background colour
        self._BCK_COL[ 0 ] = ( self._BCK_COL[ 0 ] - 5 ) % 255
        self._BCK_COL[ 2 ] = (self._BCK_COL[0] + self._BCK_COL[2]) %255 

        self._ash.render( self._window )
        
        self._clock.tick_busy_loop( self._FPS )

        cur_fps = self._clock.get_fps()
        fps_text = pygame.font.SysFont( "impact", 50 ).render( str(cur_fps), 1, (0,0,0))
        self._window.blit( fps_text, ( self._WIDTH / 2, 100) )

        pygame.display.update()

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

                cur_time = time.time()
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
