def fun(s:str):
    # return True if s is a valid email, else return False
    try:
        if len(s.split('@')) > 2 or len(s.split('.')) > 2:
            return False
        username, rest = s.split('@') 
        website,extension = rest.split('.')
    except:
        return False
    
    if username.replace('-','').replace('_','').isalnum() is False:
        return False
    
    elif website.isalnum() is False:
        return False

    return len(extension) <= 3 


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
