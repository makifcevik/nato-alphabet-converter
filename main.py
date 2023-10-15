import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row["letter"]: row["code"] for index, row in data.iterrows()}

input_name = input("Enter your name: ")
letters = [letter.upper() for letter in input_name]
coded_list = [data_dict[key] for key in data_dict.keys() if key in letters]
print(letters)
print(coded_list)
