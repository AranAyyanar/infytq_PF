def encode(message):
    count=1
    Join=""
    if len(message)>1:
        for alpha in range(0,len(message)-1):
            if (message[alpha]==message[alpha+1]):
                count=count+1
            else:
                Join=Join+(str(count)+message[alpha])
                count=1
        if message[-1]==message[-2]:
            Join=Join+(str(count)+message[-1])
        else:
            Join=Join+(str(count)+message[-1])
    else:
        Join=Join+(str(count)+message)           
    return Join
encoded_message=encode("M")
print(encoded_message)
