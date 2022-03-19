password = 'a123456'
t = 3
while t > 0:
    t = t - 1
    pw = input ('please enter your password: ')
    if password == pw:
        print ('correct')
        break
    else:
        print ('wrong password')
        if t > 0:
            print ('rest of : ' , t, 'times')
