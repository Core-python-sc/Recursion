class Even:

    def __init__(self, n:int):

        self.no:int = n

    def Even_number(self,n)->None:
        if n == 0:
            return

        else:
           
            [print(n,end=" ") if n%2==0 else None]
            self.Even_number(n -1)


def main():
    n : int = int(input("Enter a number:"))
    obj : Even =  Even(n*2)
    obj.Even_number(obj.no)


if __name__ == "__main__":
    main()