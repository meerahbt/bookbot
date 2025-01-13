# opening a file 
with open("books/Frankenstein") as f:
    file_contents = f.read() # reading the file

words = file_contents.split()
word_count = 0 

for word in words:
    word_count += 1

print(word_count)

alpha = {
    }

for char in file_contents:
    lower = char.lower()
    if lower in alpha :
        alpha[lower] += 1
    else:
        alpha[lower] = 1

alpha_list =[]
for char, count in alpha.items():
    char_dict = {"char": char, "num": count}
    alpha_list.append(char_dict)

def sort_on(dict):
    return dict["num"]

sorted_list = alpha_list.sort(reverse=True, key=sort_on)



print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")

for char_dict in alpha_list:
    if char_dict["char"].isalpha(): 
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

print("-- End report ---")