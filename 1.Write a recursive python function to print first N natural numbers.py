class Natural:

    def __init__(self, n: int):
        self.no: int = n

    def natural_number(self, n) -> None:
        if n == 0:
            return
        else:
            self.natural_number(n - 1)
            print(n, end=" ")


def main():
    n : int = int(input("Enter a number: "))
    obj : Natural = Natural(n)
    obj.natural_number(obj.no)

# The line `if __name__ == "__main__":` is used so that the code inside it only runs when you run this file directly.
# If you import this file into another file, the code inside won't run automatically.
if __name__ == "__main__":
    main()