# Day 36 --> Regular Expression (re module)

#Regular Expression --> It is a special sequence of characters which helps in pattern matching, it helps to match,search,find,extract or replace
#given pattern. It is widely used in text processing, text analysis, web development and Ai
#in python it is available as re module

import re
#we use representation as r'
'''
a = '\n'
print(a) #prints a new line
b = r'\n'
print(b) #prints literally \n because the string is treated as raw string and anything inside is simply a string 
#and it cannot \n is not treated as escape character
print(len(b))
'''
#print(dir(re))

#for suppose we have received order as Order ID : 34512 # in this string we have to extract order id
'''
string = "Order ID : 34512"
result = re.search(f'\d+',string).group()#\d to match digits and returns the first occurance, if we add + then it returns all the matching instances
print(result) #re.search() only gives the first found instance and if other matches exist they are ignore
'''
'''
#extract the age of the user from the data
data = "My name is rahul and my age is 25,I live in hyderabad"
age = re.search(r'\d+',data).group()
print(age.start()) #returns the start of the matching object
print(age) #returns the matching object
print(age.end()) #returns the end of matching object
print(age.span()) #returns start andd end in a tuple
print(age.group()) #returns the match
'''
'''
match(pattern,string)
search(pattern,string)
findall(pattern,string)
finditer(pattern,string)
fullmatch(pattern,string)
sub(pattern,replacement,string)
split(pattern,string)
compile(pattern)
escape(string)
'''

#meta characters
'''
. - matches any single characters except newline
^ - Beginning of the string
$ - end of the string
+ - one or more matches
* - zero or more matches
? zero or one matches
'''
'''
#re.match() -->  it is used to match the beginning pattern of a string
greeting = ""
result = re.match(r'Hi',greeting)
#print(result)
if result:
    print(f'matching is found "{result.group()}"') #None is returned when the beginning of the string does not match with the pattern
else:
    print("Match not found")
#re.search() --> it checks for the first matched pattern
'''
'''
greeting = 'Good Afternoon guys'

f = re.findall(r'[A-z]\w+',greeting) #returns words that have capital letters
print(f)
print(*f)
'''
'''
string1 = "Python 35 Agents 25 GENAI"

a = re.findall(r'[A-Z][a-z]+',string1)
print(a)

b = re.findall(r'\d\w+',string1)
print(b)

c = re.findall(r'\b[A-Z]+\b',string1)
print(c)
'''
'''
ids = '12 23 34 codegnan'
g = re.finditer(r'\d+',ids)
print(g)
for i in g:
    print(i.start())
'''

data = 'Codegnan is in Hyderabad,Vijayawada & vizag,contact number is 9876543201'
'''for i in data.split():
    if re.fullmatch(r'\d+',i):
        print(i)

result = re.fullmatch(r'\d{10}','9876543201')
print(result.group())
'''

#re.sub() --> Where we can replace the original pattern
#re.split() --> we can specify the split pattern
'''
f = 'I love food adsf food adga food'
g = re.sub('food','agents',f)
print(g)
h = re.sub(r'\s','*',f)
print(h)
'''
p = 'Agents,GENAI:RAG,Python'
k = re.split(r'[,:]',p)
print(k)