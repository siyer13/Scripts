def isPalindrome(word):
    if str(word) == str(word)[::-1]:
        return True
    return False

print(isPalindrome(word='abcdecba'))
