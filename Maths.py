#factorial
'''
a=int(input("Enter num:"))
def factorial(n):
    num = 1
    while n>=1:
        num = num*n
        n=n-1
    return num;
print (factorial(a))

#prime number or not

b=int(input("Enter num:"))
for i in range(2,b):
    if (b%i) == 0:
            print ("No")
    else:
        print ("Yes")

#str
# Write a function, given a string of characters, return the string together with '_'s of the same length.
str1 = "Enter"
count = len(str1)
print (count)
addstr = count * "_"
print (str1+addstr)'''

#str1

str1  = 'xyzThis,is,the,target,string  xyz'
idx1 = str1.find('xyz')                    # get the position of 'xyz'
print (idx1)
idx2 = str1.find('xyz', idx1+1)            # get the next 'xyz'
print (idx2)
str1 = str1[idx1+3:idx2].replace(',','|')    # replace ',' with '|'
str1 = str1.strip()                             # strip trailing spaces. 
print (str1)

        



