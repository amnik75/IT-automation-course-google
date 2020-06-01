
def add(a,b):
    if a < 0 or b < 0:
        raise ValueError("The numbers are negative")
    return a + b

if __name__ == '__main__':
    print(add(5,6))