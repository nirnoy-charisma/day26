import openpyxl
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
import pip

#TODO 1. Create a dictionary in this format:
data = pandas.DataFrame(pandas.read_excel("Book2.xlsx"))
new_dictionary = {row.letter:row.code for (index,row) in data.iterrows()}
print(new_dictionary.keys())
print(new_dictionary.values())
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
answer = input("Enter a word: ").lower()

new_list = [new_dictionary[letter] for letter in answer]
print(new_list)
