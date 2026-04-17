class Natural:

    def __init__(self, n:int):
       self.no:int = n

    def Natural_number_reverse(self, n) ->None:
        if n == 0:
            return;
        else:
            print(n, end=" ")
            self.Natural_number_reverse(n - 1)



def main():
    n : int = int(input("Enter a number: "))
    obj : Natural = Natural(n)
    obj.Natural_number_reverse(obj.no)


if __name__ == "__main__":
    main()