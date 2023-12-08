import re

text = 'How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.'

word = re.split('[ ,.]', text)

NoEmpty = [word[i] for i in range(len(word)) if word[i] != '']

num = list(map(len, NoEmpty))

str = list(map(str, num))

print("".join(str))
