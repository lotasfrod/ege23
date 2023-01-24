print("x y z w")
for x  in 0,1:
    for y in 0,1:
        for z  in 0,1:
            for w in 0,1:
                f = ((x<=(y==w)) and (y==(w<=z)))
                if f:
                    print(y,x,w,z)