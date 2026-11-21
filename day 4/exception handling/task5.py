while True:
    try:
        no=int(input("enter number between 1 to 10 :"))
        if no<1 or no>10:
            raise ValueError("number must be between 1 to 10")
        print("valid number:",no)
        break
    except ValueError as e:
        print("error:",e)