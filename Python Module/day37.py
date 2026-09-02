#Day 37 --> re module, 

import re

'''
pattern  = re.compile(r'\d+') #compiles a pattern that can later be used for other purpose by pairing with other methods and for repeated use
#print(pattern)

result = pattern.findall('Hello my name is pavan, my roll number is 23')
print(result)
f = pattern.search('Hello my name is pavan, my roll number is 23')
print(f.group())

p = re.escape('google.com') #adds a \ before special characters in a string to treat it like a literal string
print(p) #prints google\.com
'''
#form validation using re --> email validation, mobile numbers, Pan validation.
'''
mailid = input("Enter your email?")
iff = re.fullmatch(r'[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}',mailid)
print(iff.group())
'''
'''
phone_number = input("Enter your Phone number:")
result = re.fullmatch(r'^[6-9]\d{9}',phone_number)
print(result.group())
'''
'''
pan_number = input("Enter pan number?")
result = re.fullmatch(r'^[A-Z]{5}\d{4}[A-Z]{1}$',pan_number)
print(result.group())
'''

#username --> alphabets, _, numbers and .

pattern = re.compile(r'^[A-z0-9_.]+$')

if pattern.fullmatch(input("Enter a username to check:")).group():
    print('valid')
else:
    print("invalid")