
def main():  
    try: 
        x = int(input("ingresa una coordenada X:"))
        y= int(input("ingresa una coordenada Y:"))  
        
        if(x == 0 or y == 0):
            print("las cordenadas deben ser mayor a 0. ")
        elif(x > 0 and y > 0 ):
          print("El punto se encuentra en el cuadrante I")
        elif(x < 0 and y > 0 ):
           print("El punto se encuentra en el cuadrante II")
        elif(x < 0 and y < 0 ):
           print("El punto se encuentra en el cuadrante III")
        elif(x > 0 and y < 0 ):
          print("El punto se encuentra en el cuadrante IV")
       
          
    except ValueError:
       print("solo se permiten valores numericos")

      

if __name__ == "__main__":
    main()