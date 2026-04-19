class Sum_odd_Natural:
    def __init__(self,n:int):
        self.no = n

    def sum_of_natural(self,n:int)->int:
        if(n==0):
            return 0
        else:
            if (n%2!=0):
                return self.sum_of_natural(n-1)+n
            else:
              return  self.sum_of_natural(n-1)


def main():
    n:int = int(input("Enter the N:"))
    obj: Sum_odd_Natural = Sum_odd_Natural(n*2)
    print("Sum is:",obj.sum_of_natural(obj.no))

if __name__ == "__main__":
    main()