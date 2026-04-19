class Square:
    def __init__(self,n:int):

        self.no = n

    def square_of_n_natural_no(self,n):
        if(n == 0):
            return 0
        else:
           return self.square_of_n_natural_no(n-1)+n**2
        
def main():
    n:int=int(input("Enter the value of N:"))
    obj:Square=Square(n)
    print("The sum of square is:", obj.square_of_n_natural_no(obj.no))

if __name__ == "__main__":
    main()