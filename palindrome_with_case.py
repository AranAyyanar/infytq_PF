def is_palindrome(word):
    word=word.lower()
    join=''
    for i in word[::-1]:
        join=join+i
    if join==word:
        return True
    else:
        return False
    
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
