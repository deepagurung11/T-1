height = int(input("Enter the height of the triangle (number of rows): "))
print("Right Triangle Pattern:")
for i in range(i, height + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
