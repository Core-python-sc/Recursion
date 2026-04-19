class Sum_of_Digit:
    def __init__(self,n):
        self.no = n

    def sum_of_digit(self,n):
        if(n==0):
            return 0
        else:
            r:int = n//10
            return self.sum_of_digit(r)+(n%10)
            

def main():
    n:int=int(input("Enter the digit:"))
    obj:Sum_of_Digit = Sum_of_Digit(n)
    print("The sum of digit:",obj.sum_of_digit(obj.no))


if __name__ == "__main__":
    main()