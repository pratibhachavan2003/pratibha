def factorial_iterative(n):
factorial=1
for i in range(1,n+1):
   factorial *=i
   
n=int(input("Enter a number:"))
print("Factorial (Iterative):",factorial_iterative(n))

