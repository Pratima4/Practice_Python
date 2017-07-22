#find a word in a txt file and print the line nos which have it

file = open(r'C:\Users\prasanthi.kondamudi\Desktop\B.txt', 'r', encoding="utf8")
line_no = 0
for line in file.readlines():
    line_no += 1
    if line.find(word) >= 0:
        print (line_no)
file.close()
