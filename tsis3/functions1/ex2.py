def conv_cel(fahr):
    cels = (5/9) * (int(fahr) - 32)
    return cels
print(conv_cel(input()))