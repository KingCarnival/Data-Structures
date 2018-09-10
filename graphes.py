#Preston Bruce
#

def edge(v, w):
    if v in w[0] or w[1]:
        print("True")
    else:
        print("False")


v = input("Enter a value")
w = input("Enter a second value")
edge(v,w)