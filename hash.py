import hashlib



def md5():
    hashmd5 = hashlib.md5()
    hashmd5.update(hashValue.encode())
    print('\nMD5 : ' + hashmd5.hexdigest())

def sha1():
    hashsha1 = hashlib.sha1()
    hashsha1.update(hashValue.encode())
    print('\nSHA1 : ' + hashsha1.hexdigest())

def sha224():
    hashsha224 = hashlib.sha224()
    hashsha224.update(hashValue.encode())
    print('\nSHA224 : ' + hashsha224.hexdigest())

def sha256():
    hashsha256 = hashlib.sha256()
    hashsha256.update(hashValue.encode())
    print('\nSHA256 : ' + hashsha256.hexdigest())

def sha512():
    hashsha512 = hashlib.sha512()
    hashsha512.update(hashValue.encode())
    print('\nSHA512 : ' + hashsha512.hexdigest())


hashValue = input('Enter String to Hash: ')

n = int(input("Now, choose algorithm : \n| 1 : MD5\n| 2 : SHA1\n| 3 : SHA224 \n| 4 : SHA256 \n| 5 : SHA512\n| 6 : All\n\n"))


if n == 1:
    md5()
if n == 2:
    sha1()
if n == 3:
    sha224()
if n == 4:
    sha256()
if n == 5:
    sha512()
if n == 6:
    md5(), sha1(), sha224(), sha256(), sha512()
if n < 1 & n > 6:
    print("\nPlease choose a number between 1 and 6")
