
from PIL import Image

def make_mono( file: str = 'zi.png', thresh = 230, reverse: bool = False ):
    # image_file = Image.open( file ) # open colour image
    # image_file = image_file.convert('1') # convert image to black and white
    # image_file.save( 'zi.png' )

    # white if greater than threshold
    image_file = Image.open( file )
    filter = lambda x : 255 * int( not( reverse  ) ) if x > thresh else 0
    image_file = image_file.convert( 'L' ).point( filter, mode='1' )
    image_file.save( file )
    print( 'Saved the converted image' )

if( __name__ == "__main__" ):
    make_mono()
