
if( __name__ == "__main__" ):
    from Game import Game
    game = Game()
    game.execute()

else:
    raise Exception( "main.py was not supposed to be imported." )

