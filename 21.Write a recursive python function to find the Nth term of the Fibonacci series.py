class Fibo:
    def __init__(self):
        pass
    def fibo(self,i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
           return self.fibo(i-1)+self.fibo(i-2)
        
    def printf(self,n:int,i:int = 0):
        if n == i:
            return
        print(self.fibo(i),end=" ")
        self.printf(n,i+1)


def main():
    obj:Fibo = Fibo()
    n:int=int(input("Enter the value of N:"))
    obj.printf(n)

if __name__ == "__main__":
    main()