n = 5

for i in range(1, n + 1):  #1  5

    print(" " * (n - i), end="")  #"1" * 3
    for j in range(i): # 0 1
        print("*", end=" ")

    print()

