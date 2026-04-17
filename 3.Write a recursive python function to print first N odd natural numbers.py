class Odd:

    def __init__(self, n:int):

        self.no:int = n

    def Odd_number(self,n)->None:
        if n == 0:
            return

        else:
            self.Odd_number(n -1)
            [print(n,end=" ") if n%2!=0 else None]


def main():
    n : int = int(input("Enter a number:"))
    obj : Odd =  Odd(n*2)
    obj.Odd_number(obj.no)


if __name__ == "__main__":
    main()