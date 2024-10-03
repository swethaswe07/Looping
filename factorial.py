'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
'''

# Function to check if a number is a factorial
def is_factorial(num):
    if num < 1:
        return False
    
    # Start checking factorials from 1!
    factorial = 1
    i = 1
    
    while factorial < num:
        i += 1
        factorial *= i
        
    return factorial == num

# Input from user
n = int(input("Enter a number: "))

# Check if n is a factorial number and print the result
if is_factorial(n):
    print("Yes")
else:
    print("No")

'''
Sample Input:
6
Sample Output:
Yes
'''
