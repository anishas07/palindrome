number1 = input("Enter a number:")
r=number1[::-1]
print(r)
if number1 == r:
    print("If both of them are equal it is a palindrome")
else:
    print("If both of them don't equal to each other, it is not a palindrome")