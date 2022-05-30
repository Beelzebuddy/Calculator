j = input("+, -, *, / :" )
while True:
    if j in ("+, -, *, / :" ):
        i = float(input("1st number: "))
        k = float(input("2nd number: "))

        if j == "+":
            print( i + k)

        elif j == "-":
            print( i - k)

        elif j == "*":
            print( i * k)

        else:
            j == "/"
            print( i / k)
        break
    else:
        print("Invalid operation")
        j = input("+, -, *, /")