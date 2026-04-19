class Binary:
    def __init__(self,n):
        self.no = n

    def convert_decimal_to_binary(self,n):
        if(n==0):
            return
        else:
           
           self.convert_decimal_to_binary(n//2)
           print(n%2,end=" ")
           


def main():
    n:int=int(input("Enter the value of Decimal number:"))
    obj:Binary = Binary(n)
    print("Binary of the decimal:",end=":")
    obj.convert_decimal_to_binary(obj.no)


if __name__ == "__main__":
    main()
