"""
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def req_number():
    userNum = input("Write a number: ")
    return userNum

def even_number_check(number):
    number = int(number)
    if number % 2 == 0:
        print(f"The number {number} is even")
    else: print(f"The number {number} isn't even")

def even_number_oneToOneHundred():
    for x in range(1,101):
        if x % 2 == 0:
            print(f"{x} is even")
        else: print(f"{x}")
        
    

#Function call
number = req_number()
even_number_check(number)
even_number_oneToOneHundred()