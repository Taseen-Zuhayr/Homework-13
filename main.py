n = int(input("Enter the number of rows you want : "))

for i in range(1, n+1):
    for space in range((n-i)):
        print(" ", end="")
    for stars in range(i):
        print("*", end="")
        
    print("")