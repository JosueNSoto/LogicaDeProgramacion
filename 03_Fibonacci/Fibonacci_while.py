"""
Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    num1 = 0
    num2 = 1
    fib = 0
    index = 1
    while index <= 50:
        print(str(index) + " " + str(num1))
        fib = num1 + num2
        num1 = num2
        num2 = fib
        index += 1

#function call    
fibonacci()