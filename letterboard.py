#!/usr/local/bin/python3
import collections

#variables
filename = "letters.csv"
double_quote = '"'
fail_string = ""

letterboard_dict = {}
counts_dict = {}

#read lines from letter box file and fill dictionary
file = open(filename, mode='r', encoding='utf-8-sig')
lines = file.readlines()
file.close()

index = 0
for line in lines:
    if double_quote in line:
        (letter, count) = line.split('",",') #comma CSV export from Excel
        letter = ','
    else:
        (letter, count) = line.split(',')
        letter = letter.lower()
    letterboard_dict[letter] = int(count)

#ask for user input
sentence = input("What sentence would you like to test?\n=> ")
sentence = sentence.lower()
counts_dict = collections.Counter(sentence)
for letter in counts_dict:
    if not letter == " ":
        if counts_dict[letter] > letterboard_dict[letter]:
            fail_string += str(counts_dict[letter]) + " " + letter + "'s (Only " + \
            str(letterboard_dict[letter]) + " available)\n"

if not fail_string:
    print("\nSentence is doable with Letter Box\n")
else:
    print("\nSentence is NOT doable with Letter Box\n")
    print(fail_string)
