"""
Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

def areaPolygon():
    print("1. Triangle")
    print("2. Square")
    print("3. Rectangle")
    userChoosen = input("Select a option: ")
    if userChoosen == "1":
        print(f"Your selection was Triangle")
        print("Area = Base por altura entre 2")
        
        base = int(input("Ingresa el valor de la base: "))
        altura = int(input("Ingresa el valor de la altura: "))
        area = (base * altura) / 2
        return area
        
    if userChoosen == "2":
        print(f"Your selection was Square")
        print("Area = Lado por lado")
        
        lado1 = int(input("Ingresa el valor de un lado: "))
        area = lado1 * lado1
        return area
        
    if userChoosen == "3":  
        print(f"Your selection was Rectangle")
        print("Area = Largo por ancho")
        
        largo = int(input("Ingresa el valor de lo largo: "))
        ancho = int(input("Ingresa el valor de lo ancho: "))
        area = largo * ancho
        return area
#function call
finalArea = areaPolygon()
print(f"El area del polígono seleccionado es {finalArea}")