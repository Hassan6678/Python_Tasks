"""2– Counting Occurrences of Search Word"""
import os.path

# This function read a file and return a string containing
# the text of the file.
'''Part (a) of Question'''
"""Write a program that asks for a string and a search word. The program
then determines and displays how many time the search word appears in
the string.
"""

def count_Occurrence_part_a(line, word):
    '''To Handle the Case "Make the search case-insensitive"'''
    # lowercase to avoid case mismatch
    line = line.lower()

    # Build-in function to count a word in file
    # Word may occur as a “stand-alone word” or part of another word
    count = line.count(word)

    # Return Final Result with your word
    return count


'''Part (b) of Question'''
"""b. The following program provides a function which takes a file name, reads
the file and returns a string containing the content of the file.
Complete the program to ask the user for a file name and a search word,
and then determine and display how many times the search word appears
in the file.
"""
def readFile(fileName):
    # Open the file
    inFile = open(fileName)

    # Read File
    text = inFile.read()

    # return text
    return text


def count_Occurrence(file, word):
    # call readFile function
    line = (readFile(file))
    '''To Handle the Case "Make the search case-insensitive"'''
    # lowercase to avoid case mismatch
    line = line.lower()

    # Build-in function to count a word in file
    # Word may occur as a “stand-alone word” or part of another word
    count = line.count(word)

    # Return Final Result with your word
    return count

'''Why I Do this'''
'''
        If a Word occur as a “stand-alone word” 
        Not a part of another word.
'''

def special_case(file,word):
    # call readFile function
    line = (readFile(file))

    # lowercase to avoid case mismatch
    line = line.lower()

    # Split line into Words
    words = line.split(" ")

    # Initialize counter
    count = 0

    # Iterate over each word in line
    for i in words:
        # Check if word in line equal to Search Word
        if i == word:
            count = count + 1
    # return final Result
    return count



# Part (a)

input_string = str(input("Please Type the string : "))
word = str(input("Please Type the word Which you want to search : "))
'''Print Final Result'''
print("Occurrences of " + word + " Word in file ", count_Occurrence_part_a(input_string, word) ," times.\n")



# Part (b)
'''User Input'''
file_name = str(input("Please Type the file name which you want to read : "))

if os.path.isfile(file_name):
    # do nothoing
    word = str(input("Please Type the word Which you want to search : "))
    '''Print Final Result'''
    print("Occurrences of " + word + " Word in file ", count_Occurrence(file_name, word) ," times.")

    #print(special_case(file_name,word))
else:
    print("Error ! File not exist")


