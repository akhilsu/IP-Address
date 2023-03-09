x1 = 200
x2 = 255
x3 = 254
x4 = 200

xvalue = 2000

for x in range(0,xvalue):
    x4 = x4 + 1
    if (x4 == 256):
        x3 = x3 + 1
        x4 = 0
        if(x3 == 256):
            x2 = x2 + 1
            x3 = 0
            x4 = 0
            if(x2 == 256):
                x1 = x1 + 1
                x2 = 0
                x3 = 0
                x4 = 0
    print(str(x1)+"."+str(x2)+"."+str(x3)+"."+str(x4))
