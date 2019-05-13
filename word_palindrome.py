def check_palindrome(word):
    count=-1
    join=""
    list1=[0 for i in range(0,len(word))]
    for alpha in word:
        list1[count]=alpha
        count=count-1
    for alpha2 in list1:
        join=join+alpha2
    if join==word:
        return True
    else:
        return False
        

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
