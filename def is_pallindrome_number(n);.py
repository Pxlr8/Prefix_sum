def is_pallindrome_number(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter the number:"))
if is_pallindrome_number(num):
    print ("pallindrome")
else:
    print("not a pallindrome")