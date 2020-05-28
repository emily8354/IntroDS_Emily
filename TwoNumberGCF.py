num1 = input("Enter a number")
num2 = input("Enter another number")
num1 = int(num1)
num2 = int(num2)
smallest = 0;
if num1 < num2 :
    smallest = num1
if num2 < num1 :
    smallest = num2
i = smallest
GCF = 0
while i > 0 :
    if num1 % i == 0 and num2 % i == 0 :
        GCF = i
        break
    i = i-1
print(GCF)
