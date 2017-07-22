#download a file

import urllib.request #import requests
b= 'http://www.gutenberg.org/files/2852/2852-0.txt' #reading URL
print ("downloading")
urllib.request.urlretrieve(b, "B.txt")# location is taken by default 
#downloaded to local disk C:\Users\prasanthi.kondamudi\AppData\Local\Programs\Python\Python36-32
print ("downloaded")

#count words in a file

with open(r'C:\Users\prasanthi.kondamudi\Desktop\B.txt', 'r', encoding="utf8") as f: #open file
    p = f.read() # p contains contents of file
    words = p.split()# split the file into words
    wordCount = len(words)#count
    print ("The total word count is:", wordCount)

#find the number of commas
    
numCommas = 0
with open(r'C:\Users\prasanthi.kondamudi\Desktop\B.txt', 'r', encoding="utf8") as f:
    numCommas = f.read().count(',') #read the file and count commas and store it into variable
    print (numCommas)

#to identify no of Capital letters in a file

numCaps = 0
with open(r'C:\Users\prasanthi.kondamudi\Desktop\B.txt', 'r', encoding="utf8") as f:
    data = f.read() #read the file
    for character in data: #chking for all the characters - so for loop
        if character.isupper(): # chk capital
            numCaps += 1 #increasing the counter for every yes
print (numCaps)
