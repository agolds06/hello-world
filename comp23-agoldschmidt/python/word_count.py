import collections, sys
try:
    file = open("input_file", 'r')
except IOError:
    exit()

data = file.readlines()
words = []
for line in data:
    words.extend(line.split())
wordlist = {}
for i in words:
    if i.lower() in wordlist:
        wordlist[i.lower()] = wordlist[i.lower()] + 1
    else:
        wordlist[i.lower()] = 1
orderedlist = collections.OrderedDict(sorted(wordlist.items()))
sum = 0
for i in orderedlist:
    sum = sum + orderedlist[i]
    print str(i) + " " + str(orderedlist[i])
print "There are " + str(sum) + " words in this file"

