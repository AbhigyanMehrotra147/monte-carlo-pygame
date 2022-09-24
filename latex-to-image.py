
import sympy

def lat_to_image( text: str ):
    expr = 'sin( sympy.sqrt( x ** 2 + 20 ) ) + 1'
    sympy.preview( expr, viewer='file', filename='output.png' )

if( __name__ == "__main__" ):
    txt2render = r'$$\int_0^1 e^x\,dx$$'
    lat_to_image( txt2render )

