def fizzBuzz():
    for index in range(1,101):
        #Declaration of variables
        divBy3= index % 3 == 0 #We confirm that it is 0
        divBy5= index % 5 == 0 #We confirm that it is 0
        #Conditionals
        if divBy3 and divBy5:
            print(str(index) + " fizzbuzz")
        elif divBy3:
            print(str(index) + " fizz")
        elif divBy5:
            print(str(index) + " buzz")
        else: print(str(index) + " ")

#Function call
fizzBuzz()
