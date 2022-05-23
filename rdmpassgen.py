import random, string
import json
import os




push = input("Which app will this password be for? ")
#chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?[]`=+"
#chars could be used as our array of of possible characters for our password generator however this is not as modifyable as using the string module



def password(length,num=False, strength=''):
    #length of password num if you want a number and strength (weak, strong etc..)
    #this is all our different characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letters = lower + upper
    dig = string.digits
    punc = string.punctuation
    pwd = ''

#this will be for the different strengths of all the passwords so user can select the password strength
    if strength == 'weak':
        if num:
            length -= 1
            for i in range(1):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letters)

    
    elif strength == 'strong':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letters)

    elif strength == 'very':
        ran = random.randint(2,5)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punc)    
        for i in range(length):
            pwd += random.choice(letters)    

    elif strength == 'extreme':
        ran = random.randint(4,6)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punc)    
        for i in range(length):
            pwd += random.choice(letters)  
    #this is so our passwords will change up the order of the password that was generated
    pwd = list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)


    

#may set up so it auto lowers incase I implement this on to a site
strength = input("How strong do you want your password? weak, strong or very? ")
pwdstrength =   (strength)
if pwdstrength == 'weak':
    newpwd = str(password(7, num=True, strength='weak'))
    
elif pwdstrength == 'strong':
    newpwd = str(password(10, num=True, strength='strong'))
    
elif pwdstrength == 'very':
    newpwd = str(password(15, num=True, strength='very'))
    
elif pwdstrength == 'extreme':
    newpwd = str(password(25, num=True, strength='extreme')) 
    
else:
    print ("That is not an option")

passwords = {push: newpwd}

def append_record(record):
    with open('passwords.txt', 'a') as f:
        json.dump(record,f)
        f.write(os.linesep)

append_record(passwords)
    # If i want to use a csv use 
# field_name = ['app','password']
# dict={ 'app':push,'password': passwords}
# with open('passwords.csv', 'a') as f:
#     dictwriterobject = DictWriter(f, fieldnames=field_name)
#     dictwriterobject.writerow(dict)

print (passwords)