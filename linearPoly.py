def linearPoly(number,degree, constants):
    final = 0
    equation = ((constants[number-1]*degree+constants[number-2])*degree)

    for i in range(number-3,0,-1):
        equation = (equation + constants[i])* degree
    final = equation + constants[0]
    print("The final value is ", final) 

rotations = input("Insert a number")
exponet = input("Insert a number")
series = input("Input a list of numbers")



linearPoly(rotations,exponet,series)