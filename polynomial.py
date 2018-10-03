def polynomial(N,P,A):
    final= 0
    holder = 0

    for i in range(N, -1, -1): 
        holder= A[i] * (P ** i)
        final += holder
    print("The final function is ", final)

polynomial(5,5,[1,1,1,1,1,1])