#Thomas Morris
#CSC 499 - HW1
#Command-line program that locates a file called 'Sort Me.Txt' and then sorts the contents of
#the folder by length in ascending order and then alphabetically.

#!/usr/bin/env python3
def sort():
    #open the file 
    f = open("./Sort Me.txt","r")
    f1 = f.readlines()
    #make a list with all the words to be sorted
    words = []
    for x in f1:
        #strip extra spaces
        words.append(x.strip())
    f.close()
    
    #sort alphabetically
    words.sort()
    #sort by length
    words.sort(key=len)
    
    f = open("./Sort Me.txt","w")
    for i in range(len(words)):
        f.write(words[i]+"\n")
    f.close()
    
if __name__ == "__main__":
    sort()