class Sum_of_naturtal_no:
    def __init__(self,n:int):
        self.no = n

    def sum_of_natural_no(self,n):
        if (n==0):
            return 0
        else:
            return self.sum_of_natural_no(n-1)+n
        

def main():
    n:int = int(input("Enter the value of N:"))
    obj:Sum_of_naturtal_no = Sum_of_naturtal_no(n)
    print("SUM is:",obj.sum_of_natural_no(obj.no))



if __name__ == "__main__":
    main()