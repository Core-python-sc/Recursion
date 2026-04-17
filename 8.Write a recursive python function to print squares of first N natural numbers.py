class Square:
    def __init__(self,n:int):
        self.no:int = n

    def square_number(self,n)->None:
        if n == 0:
            return

        else:
            self.square_number(n-1)
            print(n**2,end=" ")



def main():
    n : int = int(input("Enter a number:"))
    obj : Square = Square(n)
    obj.square_number(obj.no)


if __name__ == "__main__":
    main()