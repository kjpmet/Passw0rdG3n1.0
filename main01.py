#!/usr/bin/env python
import random
import string

#Generate a random string of lower case.

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
#WeakG3n
print("#####################################")
print("8 Characters Long (Weak)\n")
print("Your First (Weak) Password is here", randomString())
print("Your Second (Weak) Password is her", randomString(8))
print("Your Third (Weak) Password is her", randomString(8))

#Generate a random string of lower case & Upper Case.
def randomString1(stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range (stringLength))
print("#####################################")
print("10 Characters Long (Medium)\n")
print("Random String with the combination of lowercase and uppercase letters")
print("Your First (Medium) Password is here", randomString1(10))
print("Your Second (Medium) Password is here", randomString1(10))
print("Your Third (Medium) Password is here", randomString1(10))

#Generate a random string of lower case & Upper Case & Numeral
def randomString2(stringLength=14):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range (stringLength)))
print("#####################################")
print("14 Characters Long (Strong)\n")
print("Your First (Strong) Password is here", randomString2(14))
print("Your Second (Strong) Password is here", randomString2(14))
print("Your Third (Strong) Password is here", randomString2(14))

#Generate a random password that contains either one L-case one U-case one int, and one S-character
def securePass(stringLength=16):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range (stringLength))

print("#####################################")
print("16 Characters Long Very Strong\n")
print("Your First (Very Strong) Password is here", securePass(16))
print("Your Second (Very Strong) Password is here", securePass(16))
print("Your Third (Very Strong) Password is here", securePass(16))



