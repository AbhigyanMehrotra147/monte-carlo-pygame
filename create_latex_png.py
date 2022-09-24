
from sympy import *
from io import BytesIO  # https://docs.sympy.org/latest/modules/printing.html?highlight=sympy+preview#module-sympy.printing.preview:~:text=There%20is%20also%20support%20for%20writing%20to%20a%20io.BytesIO%20like%20object%2C%20which%20needs%20to%20be%20passed%20to%20the%20outputbuffer%20argument.

def create_latex_png( text: str, file_name: str ):
    obj = BytesIO()  # A BytesIO object isn’t associated with any real file on the disk. It’s just a chunk of memory that behaves like a file does.
    return preview( text, viewer='file', filename=file_name, euler=False, outputbuffer=obj )

if( __name__ == "__main__" ):
    text = r'$$\int_0^1 e^x\,dx$$'
    create_latex_png( text )

