import regex
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


additon_regex = r'dodaje się (art|pkt|lit|ust|§)'
# removal_regex = r'(skreśla się (pkt|art|ust|lit|§))|([0-9]+[a-z]? skreśla się)'
# change_regex = r'(pkt|art\.|ust\.|§|lit\.) ([0-9]+[a-z]?( | i |, |-))+otrzymuj(e|ą) brzmienie'

#additon_regex = r'dodaje się (art|ust|pkt|§|lit)'
removal_regex = r'([0-9]+[a-z]? skreśla się)|(skreśla się (ust|art|pkt|§|lit))'
change_regex = r'(pkt|art\.|ust\.|§|lit\.) ([0-9]*[a-z]?( | i |, |-))+otrzymuj(e|ą) brzmienie'

USE_PRECOMPUTED = False

## asuming all was .lower()

test_str = None

with open('data/2004_2158.txt', 'r', encoding='utf-8') as f:
    test_str = f.read().lower()


onlyfiles = [f for f in listdir('data') if isfile(join('data', f))]


addtion_found = {}
removal_found = {}
change_found = {}
if USE_PRECOMPUTED:
    addtion_found = {'1993': 31, '1994': 99, '1995': 322, '1996': 480, '1997': 633, '1998': 216, '1999': 149, '2000': 736, '2001': 1055, '2002': 82, '2003': 916, '2004': 884}
    removal_found = {'1993': 3, '1994': 21, '1995': 57, '1996': 127, '1997': 168, '1998': 54, '1999': 40, '2000': 226, '2001': 161, '2002': 1, '2003': 3, '2004': 1}
    change_found = {'1993': 56, '1994': 156, '1995': 334, '1996': 816, '1997': 994, '1998': 273, '1999': 142, '2000': 1343, '2001': 1199, '2002': 91, '2003': 1082, '2004': 999}
else:
    for i,file in enumerate(onlyfiles):
        if i%50 == 0:
            print('processing {}/{}'.format(i,len(onlyfiles)))
            print('additions : {}\nremovals : {}\nchanges : {}'.format(addtion_found, removal_found, change_found))
        file_content = None
        year = file.split('_')[0]
        with open('data/'+file, 'r', encoding='utf-8') as f:
            file_content = f.read().lower()
        if not year in addtion_found:
            addtion_found[year] = 0
        if not year in removal_found:
            removal_found[year] = 0
        if not year in change_found:
            change_found[year] = 0
        addtion_found[year] = addtion_found[year] +  len(regex.findall(additon_regex, file_content))
        removal_found[year] = removal_found[year] + len(regex.findall(removal_regex, file_content))
        change_found[year] = change_found[year] + len(regex.findall(change_regex, file_content))
print('')

additions = sum(list(addtion_found.values()))
removals = sum(list(removal_found.values()))
changes = sum(list(change_found.values()))

print('additions : {}\nremovals : {}\nchanges : {}'.format(additions,removals,changes))
print(addtion_found)
print(removal_found)
print(change_found)


tick_label = list(addtion_found.keys())
red_patch = mpatches.Patch(color='red', label='removed')
green_patch = mpatches.Patch(color='green', label='added')
yellow_patch = mpatches.Patch(color='yellow', label='changed')


x_adds = []
x_rems = []
x_changes = []
x_labels = list(addtion_found.keys())
for year in list(addtion_found.keys()):
    x_adds.append(addtion_found[year]*100 / (addtion_found[year]+removal_found[year]+change_found[year]))
    x_rems.append(removal_found[year]*100 / (addtion_found[year]+removal_found[year]+change_found[year]))
    x_changes.append(change_found[year]*100 / (addtion_found[year]+removal_found[year]+change_found[year]))

plt.plot(x_labels,x_adds,color='green')
plt.plot(x_labels,x_rems,color='red')
plt.plot(x_labels,x_changes,color='yellow')
plt.legend(handles =[red_patch,green_patch,yellow_patch])
plt.xlabel('year')
plt.ylabel('% of total operations in given year')

plt.show()


