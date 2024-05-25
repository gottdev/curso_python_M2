if __name__ == "__main__":
    
    palabra = input("Porfavor ingresa una palabra de 4 a 8 caracteres: ")

    tamaño = len(palabra) 

    if tamaño < 4 :
        print(f"Hacen falta letras. Solo tiene {tamaño} letras ")

    elif tamaño > 8 :
        print("tu palabra es mayor a 8 caracteres ")
    else :
        print("tu palabra es correcta ")

