

def porta_not(x):
    if x == 0:
        x += 1
        return x
    elif x == 1:
        x -= 1
        return x
    else:
        print('Inserire numero valido')
