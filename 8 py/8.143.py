from itertools import product

words = list(product('РУСТАМ', repeat = 6))
i = []

for x in range(len(words)):
    if (words[x].count('Р'))+(words[x].count('С'))+(words[x].count('Т'))+(words[x].count('М'))>=3:
        i.append(words[x])



print(len(i))
