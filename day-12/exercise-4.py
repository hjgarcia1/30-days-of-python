def is_palindrome(text):
    text = text.strip().lower()
    text_reversed = text[::-1]
    if(text == text_reversed):
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")


is_palindrome("Hannah")
is_palindrome("Fred")
