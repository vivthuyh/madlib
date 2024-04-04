'''
Author: Vivian Huynh
Date: 04/04/2024
Class: ISTA 130
Section Leader: Taaon Fraser 

Description:
Homework Assignment 7
'''

# imports:
import string 

# functions: 

def print_report(file_name):
    '''
    This function will read a given file and print a report giving the total number of vowels, consonants, whitespaces, and punctuation. It will also report the total number of characters in the file, as well as the percent of the file composed of vowels, consonants, whitespaces, and punctuation. 

    Parameters: This function has one parameter. The parameter is a string that represents the name of the file that the user wants to use for the mad lib. 

    Returns: This function will print a report of total number of vowels, consonants, whitespaces, and punctuation, as well as the percentage values. The report will vary based on which file the user uses. 
    '''
    vowels_cnt=0
    consonants_cnt=0
    whitespace_cnt=0
    punctuation_cnt=0
    char_cnt=0

    vowels = 'aeiouAEIOU'
    consonants= 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    punctuation= string.punctuation

    with open(file_name, 'r') as file:
        for line in file:
            for ch in line:
                if ch in vowels:
                    vowels_cnt+=1
                elif ch in consonants:
                    consonants_cnt+=1
                elif ch.isspace():
                    whitespace_cnt+=1
                elif ch in punctuation:
                    punctuation_cnt+=1
                char_cnt+=1
    
    percent_vowels= round(vowels_cnt/char_cnt*100,1)
    percent_consonants= round(consonants_cnt/char_cnt*100,1)
    percent_spaces=round(whitespace_cnt/char_cnt*100,1)
    percent_punc=round(punctuation_cnt/char_cnt*100,1)

    print('\n'f'{file_name.center(25,"-")}')
    print(f"Vowels:".ljust(20), f"{vowels_cnt}".rjust(4))
    print(f"Consonants:".ljust(20), f"{consonants_cnt}".rjust(4))
    print(f"Whitespace:".ljust(20), f"{whitespace_cnt}".rjust(4))
    print(f"Punctuation:".ljust(20), f"{punctuation_cnt}".rjust(4))
    print('-' * 25)
    print(f"Total:".ljust(20), f"{char_cnt}".rjust(4))
    print('\n'f"Percent vowels:".ljust(20), f"{percent_vowels}".rjust(5))
    print(f"Percent consonants:".ljust(20), f"{percent_consonants}".rjust(4))
    print(f"Percent spaces:".ljust(20), f"{percent_spaces}".rjust(4))
    print(f"Percent punctuation:".ljust(20), f"{percent_punc}".rjust(4))
    print('=' * 25)

def replace_parts_of_speech(sentance,label):
    '''
    This function will take a given string and for each occurence of a part of speech, ask the user for a word of the part of speech. It will then replace the part of speech placeholder with the word provided by the user.

    Parameters: This function has two parameters. The first parameter is a string representing a line from a file. The second parameter is a string indicating which part of speech label to replace, e.g. "NOUN", "VERB", etc.

    Returns: When called, this function will replace all parts of speech placeholders of the indicated type, and return the new version of the given string. 
    '''
    count=sentance.count(label)
    for i in range(count):
        user=input(f"Enter {' '.join(label.split()).lower()}: ")
        sentance= sentance.replace(label,user,1)
    return sentance
    
def complete_mad_lib(file_name):
    '''
    This function will read the given file line by line and replace all parts of speech labels with words entered by the user. Then it will print the complete story out in a new file. 

    Parmeters: This function has one parameter. The parameter is a string that represents the name of a Mad Lib template file to be read. 

    Returns: When called, the function will write a completed story to a new file with the same name as the original file, prepended with the string "MAD_". 
    '''
    with open(file_name, 'r') as reader:
        new_file= "MAD_" + file_name
        with open(new_file, 'w') as writer:
            for line in reader:
                line= replace_parts_of_speech(line, 'PLURAL NOUN')
                line= replace_parts_of_speech(line, 'VERB PAST')
                line= replace_parts_of_speech(line, 'VERB')
                line= replace_parts_of_speech(line, 'NOUN')
                line= replace_parts_of_speech(line, 'ADJECTIVE')
                writer.write(line)


#==========================================================
def main():
    '''
    This function will run through a Mad Lib game with the user. 

    Parameters: This function has no parameters

    Returns: This function will ask the user to enter the file name, then it will print the character report of the given file, then have the user complete the Mad Lib story, and then finally print the new completed mad lib story into a new file. 
    '''
    file_name=input("Enter file name: ")
    print_report(file_name)
    complete_mad_lib(file_name)


if __name__ == '__main__':
    main()
