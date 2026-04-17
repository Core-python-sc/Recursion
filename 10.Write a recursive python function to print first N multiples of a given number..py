class Multiple:
    def __init__(self,x:int,n:int):
        self.x=x
        self.no:int = n

    def multiple_number(self,x,n)->None:
        if n == 0:
            return 
        else:
            self.multiple_number(x,n-1)
            print(f"{x} X {n} = {x*n}")



def main():

    x : int = int(input("Enter a number:"))
    n : int = int(input("Enter the value of n:"))
    obj : Multiple = Multiple(x,n)
    obj.multiple_number(obj.x,obj.no)


if __name__ == "__main__":
    main()