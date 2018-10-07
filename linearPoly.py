def linearPoly(number,degree, constants):
    final = 0
    equation = ((constants[number-1]*degree+constants[number-2])*degree)

    for i in range(number-3,0,-1):
        equation = (equation + constants[i])* degree
    final = equation + constants[0]
    print("The final value is ", final) 

linearPoly(5,3,[1,2,4,3,6]) 
