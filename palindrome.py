#Preston Bruce
#Palindrome 
def palindrome(text): #Creating the function
    questionWord = list(text)
    reverseWord = list(text)
    reverseWord.reverse() #reverses the word list to test
    print(questionWord)
    print(reverseWord)
    if questionWord == reverseWord: #checks if the list are equal
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

word = input("Enter a word to see if it is a Palindrome: ") #User input
palindrome(word)
first = 'true'
palindrome(first)
second = 'false'
palindrome(second)
third = 'bob'
palindrome(third)
