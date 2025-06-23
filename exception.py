def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b) #I try to division it by 0
        print("the operation is successful")
    except NameError as ne:
        print(f"Name Error {ne}")
    except Exception as exc:
        print(f"The Exception: {exc.__class__}")
        print(f"Error: {exc}")


additoin(10, 20)