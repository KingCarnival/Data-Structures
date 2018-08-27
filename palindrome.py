def palindrome(text): #Creating the function
    questionWord = list(text)
    testWord = list(text)
    testWord.reverse() #reverses the word list to test
    print(questionWord)
    print(testWord)
    if questionWord == testWord: #checks if the list are equal
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

first = 'true'
palindrome(first)
second = 'false'
palindrome(second)
third = 'bob'
palindrome(third)
