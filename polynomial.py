def polynomial(N,P,A):
    final= 0
    holder = 0

    for i in range(N, -1, -1): 
        holder= A[i] * (P ** i)
        final += holder
    print("The final function is ", final)

polynomial(3,4,[7,6,8,6])