print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(x))<= y) and ((not(y))==z) and w
                F = int(F)
                if F == 1:
                    print(x, y, z, w, F)
