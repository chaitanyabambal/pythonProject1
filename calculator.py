def add(x, y):
    return x + y


def substract(x, y):
    return x - y

def multiply(x ,y):
    return x * y

def divisible(x, y):
    return x/y

if __name__=="__main__":
    num1= float(input("enter 1st number:"))
    num2 = float(input("enter 2nd number:"))
    result =add(num1, num2)
    print(result)
    result =substract(num1, num2)
    print(result)
    result = multiply(num1, num2)
    print(result)
    result = divisible(num1, num2)
    print(result)