def palindrome(n):
    if n==n[::-1]:
        return "word is palindrome"
    return " it is not palindrome"
n=input()
print(palindrome(n))