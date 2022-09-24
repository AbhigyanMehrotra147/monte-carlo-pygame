
from sympy import *

def create_latex_png( text: str ):
    preview( text, viewer='file', filename='test.png', euler=False )
    return None

if( __name__ == "__main__" ):
    text = r'$$\int_0^1 e^x\,dx$$'
    create_latex_png( text )

