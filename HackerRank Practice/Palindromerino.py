''' user enters a string, if it's a palindrome, print 'Palindromerino', if not, print 'Enter a palindrome.' '''

palindrome = input().strip()

def split_palindrome(palindrome):
    
    array = list(palindrome.replace(' ', ''))
    
    count1 = 0
    count2 = len(array)-1
    
    for i in range(len(array)):
        while count1 < count2:
            if array[count1] == array[count2]:
                count1 = count1 + 1
                count2 = count2 - 1
            else:
                return 'Not a palindrome.'
        return 'Palindromerino!'

print(split_palindrome(palindrome))