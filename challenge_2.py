import operator

text = open('cryptic_challenge_2.txt').read()
mapping = {}
for ch in text:
    if ch not in mapping:
        mapping[ch] = 1
    else:
        mapping[ch] += 1

sorted_mapping = sorted(mapping.items(), key = operator.itemgetter(0))
for each in sorted_mapping:
    print(each)

# we see aeilqtuy
pure = ""
for ch in text:
    if ch in "aeilqtuy":
        pure += ch

print(pure)
# the answer was equality
# next level link => http://www.pythonchallenge.com/pc/def/equality.html 
