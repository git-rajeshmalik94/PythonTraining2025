
# Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found
import glob
import re
import os

print('*********Assignment 1 starts**************')
txtfiles = glob.glob("SampleDataFiles/*.txt")
print(f" .txt files are {txtfiles}")
search_str = "Python"
pattern = re.compile(re.escape(search_str), re.IGNORECASE)

for file in txtfiles:
    with open(file, 'r') as f:
     content = f.read()
    if pattern.search(content):
        print(f"The file {file} contains the string {search_str}")


print('*********Assignment 1 ends**************')



print('*********Assignment 2 starts**************')
# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
all_files = glob.glob("SampleDataFiles/*")
print(f"All files are {all_files}")
pattern = re.compile(r"^data_.*\.csv$", re.IGNORECASE)
for file_path  in all_files:
   file_name = os.path.basename(file_path)
   if pattern.match(file_name):
      print(f"Matched file: {file_name}")

 
print('*********Assignment 2 ends**************')


print('*********Assignment 3 starts**************')
# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890

phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "(987)654-3210",
    "(456) 789-1234",
    "(321 654-9870",
    "(555) 123-4567"
]
pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')

for number in phone_numbers:
    if pattern.match(number):
        print(f"Valid:   {number}")
    else:
        print(f"Invalid: {number}")

print('*********Assignment 3 ends**************')
