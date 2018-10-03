def linearPoly(degree, constants):
    final = 0
    holder = 0

    for i in range(degree,-1,-1):
        holder = (constants[i]*degree)
        final += holder
    print("The final value is ", final) 

linearPoly(5,[1,1,1,1,1,1])
