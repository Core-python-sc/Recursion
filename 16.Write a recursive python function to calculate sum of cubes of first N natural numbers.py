class Cube:
    def __init__(self,n):
        self.no = n
    def cal_sum_of_cubes(self,n):
        if(n==0):
         return 0
        else:
           return self.cal_sum_of_cubes(n-1)+n**3
    
def main():
   n:int = int(input("Enter the value of N:"))
   oj:Cube = Cube(n)
   print("Sum of cube:",oj.cal_sum_of_cubes(oj.no))
    
    
if __name__ == "__main__":
   main()