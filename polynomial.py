def polynomial(N,P,A):
    final= 0
    holder = 0

    for i in range(N, -1, -1): 
        holder= A[i] * (P ** i)
        final += holder
    print("The final function is ", final)

polynomial(7,5,[3,10,5,12,9,4,6,8])