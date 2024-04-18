s = input("Enter a value: ")
reverse_s = s[::-1]
if(s==reverse_s):
    print(f"{s} is palindrome")
else:
    print(f"{s} is not a palindrome")
