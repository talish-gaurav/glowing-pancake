try:

    x = int(input("Enter your number:"))

    print("The number entered is:",x)

except ValueError as ex:

    print(" Exception,",ex)