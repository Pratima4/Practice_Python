#Create an index for a text file

file = open(r'C:\Users\prasanthi.kondamudi\Desktop\B.txt', 'r', encoding="utf8")

'''
algorithm
find distinct words
find their location
get their locations into a list
'''

with open(r'C:\Users\prasanthi.kondamudi\Desktop\B.txt', 'r', encoding="utf8") as f: #open file
    p = f.read() # p contains contents of file
    words = p.split()# split the file into words
        for word in words:
            if word not in words:
                file.write(str(word) + "\n")
        file.close()
