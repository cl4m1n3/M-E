def isPalindrome(text: str) -> bool:
    return text == text[::-1]

print(isPalindrome(input()))