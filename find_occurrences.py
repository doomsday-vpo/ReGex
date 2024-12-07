import re

sentence = input()
searched_word = input()

pattern = r'\b{}\b'.format(searched_word)

matches = re.findall(pattern, sentence, re.IGNORECASE)
print(len(matches))