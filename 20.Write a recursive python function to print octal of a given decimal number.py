class Octa:
    def __init__(self,n):
        self.no = n

    def covert_decimal_to_octa(self,n):
        if(n==0):
            return
        else:
            self.covert_decimal_to_octa(n//8)
            print(n%8,end="")

def main():
    n:int=int(input("Enter the value of N:"))
    obj:Octa=Octa(n)
    print("The octa value of decimal:",end="")
    obj.covert_decimal_to_octa(obj.no)


if __name__ == "__main__":
    main()