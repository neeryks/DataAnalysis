num = int(input("Enter a Number to check if its prime or not: "))
  
if num > 1:
  
    for i in range(2, int(num/2)+1):
  
        if (num % i) == 0:
            print(num, "NOT PRIME")
            break
    else:
        print(num, "PRIME")
  
else:
    print(num, "PRIME")
