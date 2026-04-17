class Reverse_of_number:
    def __init__(self,n):
        self.no = n

    def reverse(self,n):
        if n == 0:
            return
        else:
            print(n%10,end="")
            self.reverse(n//10)


def main():
    n : int = int(input("Enter the number:"))
    obj : Reverse_of_number = Reverse_of_number(n)
    obj.reverse(obj.no)


if __name__ == "__main__":
    main()