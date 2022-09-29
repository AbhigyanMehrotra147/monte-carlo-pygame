
import matplotlib.pyplot as plt
import sympy

def create_latex_png( *, sub_i: str, h_s: bool = False, file: str = "zi.png", bool_axes: bool = False, font_size: int = 20, pos: tuple = ( 0, 0.4 ), fig_size: tuple = ( 2, 1 ) ):
    # current latex
    cur_tex = r"$Z_{" + sub_i + r"} = {" + str( int( h_s ) ) + r"}$"

    # Add the text s to the Axes at location x, y in data coordinates. Returns instance of Text
    z_fig = plt.figure( figsize = fig_size )
    z_fig.text( pos[ 0 ], pos[ 1 ], cur_tex, fontsize=font_size )

    # hide axes
    fig = z_fig.gca()
    z_fig.get_axes()[0].set_visible( bool_axes )

    # save file
    z_fig.tight_layout()
    z_fig.savefig( file )

    # to show the file  
    plt.show()

    return z_fig

if( __name__ == "__main__" ):
    return_z( sub_i=str( input( "Enter the i for ith Z: " ) ), h_s=True )

