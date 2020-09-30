import os
import shutil

in_base = '#competition'

words = []
# get word
for name in os.listdir('.'):
    if ' ' in name:
        words.append([name, name.split(' ')[-1]])
# print(words)

for name, word in words:
    out_base = name
    for name in os.listdir(in_base):
        in_path = os.path.join(in_base, name)
        out_path = os.path.join(out_base, name)
        if word.lower() in name.lower():
        # if word in name:
            print(in_path)
            shutil.move(in_path, out_path)
