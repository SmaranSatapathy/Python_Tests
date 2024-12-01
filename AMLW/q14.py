def expand(n):
    
    numbers={
    0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
 }
    
    for i in n:
        print(numbers.get(int(i)),end=" ")


n=list(input("Enter number: "))
expand(n)

