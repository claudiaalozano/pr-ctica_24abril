from banco import *
from casino import *

if __name__ == '__main__':
    ej = input("Seleccione bano o casino: ")
    
    if ej == "banco":
        main()
    
    elif ej == "casino":

        jugar()
    