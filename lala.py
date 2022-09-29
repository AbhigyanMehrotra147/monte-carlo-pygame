
import pygame

from RollingWindow import RollingWindow

if( __name__ == "__main__" ):
    pygame.init()

    WIDTH, HEIGHT = 200, 300

    screen = pygame.display.set_mode( size = ( WIDTH, HEIGHT ) )
    clock = pygame.time.Clock()
    FPS = 10

    a_rolling_window = RollingWindow( window_size=( WIDTH, HEIGHT ), fps=FPS )

    running = True
    while running:
        # The function returns milliseconds since the previous call.
        deltaTime = clock.tick_busy_loop( FPS ) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill( ( 0, 0, 0, 0 ) )
        a_rolling_window.update( delta_T=deltaTime )
        a_rolling_window.render( screen )

        pygame.display.update()

