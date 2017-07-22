

#find a word in a txt file and print the line nos which have it -- case insensitive

word = input("Enter the word you want to find:")
wordlower = word.lower()
file = open(r'C:\Users\prasanthi.kondamudi\Desktop\B.txt', 'r', encoding="utf8")
line_no = 0
for line in file.readlines():
    line_no += 1
    line = line.lower()
    if (line.find(wordlower) >= 0):
        print (line_no)
else :
        print("Not found")
file.close()
