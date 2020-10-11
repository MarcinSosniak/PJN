import regex
additon_regex = r'dodaje się (art\.|ust\.|pkt) [0-9]+'
removal_regex = r''
change_regex = r'(pkt|art\.|ust\.) [0-9]+[a-z]? otrzymuje brzmienie'

## asuming all was .lower()

test_str = None

with open('data/2004_2158.txt', 'r', encoding='utf-8') as f:
    test_str = f.read().lower()

print(test_str)
print(regex.findall(additon_regex,test_str))
print(regex.findall(removal_regex,test_str))
print(regex.findall(change_regex,test_str))

