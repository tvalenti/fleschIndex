"""
Program: fleshIndex.py
Author: Tom

compute and displays the flesch index and the grade level equivalent for the readability of a text file.
"""

# take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
#replace the - to spaces for the "Sam-I-am" in the green eggs and ham text file
text = text.replace('-', ' ')
inputFileNew = open(fileName, 'w')
inputFileNew.write(text)

# count the sentences
sentences = text.count('.') + text.count('?') + \
    text.count(';') + text.count(':') + text.count('!') 

# count the words
words = len(text.split())

# count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'e', 'ed']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# compute the flesch indexand grade level
index = 206.835 - 1.015 *(words / sentences) - 84.6 * (syllables / words)
level = round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59)

# output the results
print("The flesch index is", index)
print("The grade level equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")