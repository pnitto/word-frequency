
import re

def histo_gram(phrase):
    with open('sample.txt') as in_file:
        x = in_file.read()
        x = re.sub(r'[^\n \w]','',x).lower().split()
        # print(x)
        text = {}
    for word in x:
        if word in text:
            text[word] = text[word] + 1
        else:
            text[word] = 1
    return text
    returned_text = histo_gram(1)
histo_gram(1)
def one_list(text):
    new_list = []
    for key, value in text.items():
        two_append = [key, value]
        new_list.append(two_append)
        new_list.sort(key=lambda tup: tup[1], reverse=True)

    return new_list

# newer_dict = histo_gram(1)
# newer_list = one_list(newer_dict)
print(newer_list[0:20])
