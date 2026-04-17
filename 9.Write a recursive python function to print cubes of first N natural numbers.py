class Cube:
    def __init__(self,n:int):
       self.no:int = n

    def cube_number(self,n)->None:
        if n == 0:
            return
        else:
            self.cube_number(n-1)
            print(n**3,end=" ")

def main():
    n : int = int(input("Enter a number:"))
    obj : Cube = Cube(n)
    obj.cube_number(obj.no)

if __name__ == "__main__":
    main()