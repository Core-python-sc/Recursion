class Factorial:
    def __init__(self,n):
        self.no = n

    def calculate_factorial(self,n):
        if(n==0):
            return 1
        else:
           return self.calculate_factorial(n-1)*n

def main():
    n:int = int(input("Enter the value of N:"))
    obj:Factorial = Factorial(n)
    print("Factorial:",obj.calculate_factorial(n))


if __name__ == "__main__":
    main()