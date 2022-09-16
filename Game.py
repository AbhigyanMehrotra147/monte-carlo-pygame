
import pygame
from Person import Person
from os import environ

class Game( object ):

    def __init__( self ):
        self._running = True
        self._display_surf = None
        self._SIZE = self._width, self._height = 640, 480
        self._TITLE = "Monte Carlo Beer Simulation"
        self._media_dict = dict()
        self._background = (23, 38, 38)
        self._clock = None

        self._fps = 30
        self._g = 9.8

    def on_init( self, mass: float, length: float, theta: float, theta_dash: float, theta_double_dash: float, color: tuple, pivot: tuple ):
        environ["SDL_VIDEO_CENTERED"] = '1'

        pygame.init()

        # the display surface, screen surface
        self._display_surf = pygame.display.set_mode( size=self._SIZE )
        pygame.display.set_caption( self._TITLE )

        # clock
        self._clock = pygame.time.Clock()

        # humans array ?

        self._running = True

    def on_load_media( self, name, path: str, convert_alpha: bool ):
        if name not in self._media_dict.keys():
            if alpha:
                self._media_dict[name] == pygame.image.load( path ).convert_alpha()

            else:
                self._media_dict[name] = pygame.image.load( path ).convert()

        else:
            print(f"Media with the name {name} was already defined!")

    def on_loop( self ):
        pass

    def on_render( self ):

        self._clock.tick_busy_loop( self._fps )
        self._display_surf.fill( self._background )

        pygame.display.update()

    def on_cleanup( self ):
        pygame.quit()

    def on_execute( self ):

        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if( __name__ == "__main" ):
    one_game = Game()
