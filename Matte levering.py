løsninger = 0
for x in range (-100, 101):
    for y in range (-100, 101):
        for z in range (-100, 101):
            for n in range (0, 11):
                if x**3 + z**3 + y**3 == n:
                    print ("x", x, "y", y, "z", z,"^2", " n", n,)
                    løsninger += 1
                    print("løsning: ", løsninger)