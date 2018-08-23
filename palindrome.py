def palindrome(text):
    questionWord = list(text)
    testWord = list(text)
    testWord.reverse()
    print(questionWord)
    print(testWord)
    if questionWord == testWord:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

first = 'true'
palindrome(first)
second = 'false'
palindrome(second)
third = 'bob'
palindrome(third)
