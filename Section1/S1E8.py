

def C_to_F():
    C = int(input("insira a temperatura em celcius: "))
    F = (9 * C + 160) / 5
    print(F)

def C_to_F2(C):
    F = (9 * C + 160) / 5
    print(F)

def C_to_F3(C):
    F = (9 * C + 160) / 5
    return F

C_to_F()

C_to_F2(41)

t = C_to_F3(42)
print(t)
