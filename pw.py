password = 'a123456'
t = 3
while True:
    pw = input ('please enter your password: ')
    if password == pw:
        print ('correct')
        break
    else:
        t = t-1
        print ('wrong password' 'rest of :' ,t, 'times')
        if t == 0:
            break
