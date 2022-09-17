
from Sprite import Sprite
import pygame

class Game( object ):

    def __init__( self ):
        self._TITLE = " Monte Carlo Beer Simulation "
        self._WIDTH = 640
        self._HEIGHT = 480
        self._FLAGS = pygame.RESIZABLE

        self._SIZE = ( self._WIDTH, self._HEIGHT )
        self._BCK_COL = ( 255, 0, 0 )
        self._NUM_IMAGES = 5
        self._SURFACES = []
        self._FPS = 60

        self._window = None
        self._surf_index = 0
        self._clock = None
        self._running = True

        self._Bck_CHANGE_TIME = 2000
        self._tmp = 

    def _initialize( self ):
        success = True

        # initialising pygame subsystems
        pygame.init()
        if( not pygame.get_init() ):
            print( "Error in initializing pygame!" )
            success = False
        else:
            self._window = pygame.display.set_mode( size=self._SIZE, flags=self._FLAGS, depth=0, display=0, vsync=0 )
            pygame.display.set_caption( self._TITLE )
<<<<<<< HEAD
<<<<<<< HEAD
            self._clock = self.pygame.time.Clock()
            pygame.time.set_time(pygame.USEREVENT,self._Bck_CHANGE_TIME)
=======
            self._clock = pygame.time.Clock()
>>>>>>> 4961fea1a70159e2f3724228103f825642cc5ef0
=======
            self._clock = pygame.time.Clock()
>>>>>>> db33589e0759fde2aadf7fda319c6558e0db2901

        return success

    def load_media( self ):
        success = True
        extension = ".jpg"
        for i in range(self._NUM_IMAGES):
            self._SURFACES[i] = pygame.image.load(self._path + str(i) + extension).convert_alpha()
        
        return success 
    
    def _update( self ):
        pass

    def _render( self ):

        self._window.fill( self._BCK_COL )
        self._window.blit(self._SURFACES[self._surf_index], (0,0)))
        self._clock.tick( self._FPS )
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
                self._handle_events()
                self._update()
                self._render()
        
        self._clean()
        print( 'Exited game instance!' )

    def _clean( self ):
        # needs to delete / free elements
        # quits pygame sub-systems
        pygame.quit()
