f = open('lexicon.txt', "r", encoding='utf-8') # the file that contains the lexicon
f2 = open('foo2.txt', "r", encoding='utf-8') # the file that contains the lexicon
f3 = open('new_file2.txt', "w", encoding='utf-8')  #the out put file

def verify(word,lexicon): #this function verifys if the tweet contains at least one negative or positive word
    if word in lexicon: 
       return True

lexicon = list() #list that contain all the lexicon

for line in f:
    lexicon.append(line)

lines = f2.readlines()

for line in lines:
    for word in line.split(' '):
        if verify(word,lexicon): #verify if the tweet contains at least one lexicon
            f3.write(line) #write the final out put on the new_file
        
        
            

