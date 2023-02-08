def solve(numheads,numlegs):
    R=numlegs/2-numheads
    C=numheads-R
    solution = "number of rabbits is {} number of chikkens is {}".format(R,C)
    return solution
numheads=input("number of heads")
numlegs=input("number of legs")
print(solve(float(numheads),float(numlegs)))
