'''def main():
    try :
        configurar = open("config.txt")
    except FileNotFoundError:
        print("No se puede encontrar el archivo config.txt :C")
if __name__ == '__main__':
    main()'''

'''def main():
    try :
        configurar = open("config.txt")
    except Exception:
        print("No se puede encontrar el archivo config.txt :C")
if __name__ == '__main__':
    main()'''

def main():
    try :
        open("config.txt")
        print("Se pudo abrir :D")
    except FileNotFoundError:
        print("No se puede encontrar el archivo config.txt :C")
    except PermissionError:
        print("No tienes permisos para acceder a este archivo :c")
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivos bajo carga pesada, no se puede completar la lectura del archivo de configuracion")
if __name__ == '__main__':
    main()

