from simplecrypt import decrypt

inp = open('encrypted.bin', 'rb')
encrypted = inp.read()
pass_file = open('passwords.txt', 'r')


for password in pass_file:
    try:
        mystring = decrypt(password.rstrip('\n'), encrypted).decode('utf8')
    except:
        print('ooops')
    else:
        print(mystring)

#mystring = decrypt('RVrF2qdMpoq6Lib'.rstrip('\n'), encrypted).decode('utf8')
#print(mystring)

inp.close()
pass_file.close()


