
#!/bin/bash
# Take input from user and calculate sum.

read -p "Enter first number: " num1
read -p "Enter second number: " num2

sum=$(( $num1 + $num2 ))

echo "Sum is: $sum"

