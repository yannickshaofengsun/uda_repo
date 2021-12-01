def add(a, b):
    return (a + b)

if __name__ == "__main__":
    print("This programme return a + b")
    a = float(input("Number a: "))
    b = float(input("Number b: "))
    print("{} + {} = {}".format(a, b, add(a,b)))
