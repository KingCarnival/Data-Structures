def palindrome(text):
    questionWord = list(text)
    if questionWord == questionWord.reverse():
        print("This is a palindrome")
    else
        print("This is not a palindrome")
