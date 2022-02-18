'''def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()'''

#Cuando se necesita acceder al error en especifico se realiza lo siguiente: 
'''try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("Hubo un problema al tratar de leer el archivo:", err)'''

import errno


try:
    open("mars.jpg")
except OSError as err:
    if err.errno == 2 :
        print("No se puede encontrar el archivo :c")
    elif err.errno == 13:
        print("Se encontro el archivo pero no se puede leer :c")
    
