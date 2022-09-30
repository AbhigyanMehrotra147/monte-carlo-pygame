
from monochrome import make_mono
import matplotlib.pyplot as plt

def return_formula( index: str = 'i', N: str = r'10^3', avg: str = '0.73', file: str = 'formula.png', convolve: bool = True, font_size: int = 20, pos : tuple = ( 0.1, 0.4 ), fig_size: tuple = ( 3, 1 ) ):

    # Latex
    cur_tex = r"$\frac{1}{" + N + r"} * " + r"\sum_{" + index + r"=0}^{" + N + r"} Z_i = " + avg + r"$"

    # add text to axis
    f_fig = plt.figure( figsize = fig_size ) # formula fig
    f_fig.text( pos[ 0 ], pos[ 1 ], cur_tex, fontsize=font_size )

    # hide axes
    fig = f_fig.gca()
    f_fig.get_axes()[0].set_visible( False )
    f_fig.tight_layout()

    # save
    f_fig.savefig( file )

    plt.close( 'all' )

    if( convolve ):
        make_mono( file= file )

if( __name__ == "__main__" ):
    return_formula( )
