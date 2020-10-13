import regex
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


ustawa_regex = r'(ustawa|ustawy|ustawie|ustawą|ustawę|ustawo)'

ustawa_z_z_dnia = ustawa_regex + r' z dnia'
ustwa_bez_z_dnia = ustawa_regex + r'( |)(?!z dnia)'


ustaw = 0
ustaw_z = 0
ustaw_bez = 0



onlyfiles = [f for f in listdir('data') if isfile(join('data', f))]
for i, file in enumerate(onlyfiles):
    if i % 50 == 0:
        print('processing {}/{}'.format(i, len(onlyfiles)))
    file_content = None
    year = file.split('_')[0]
    with open('data/' + file, 'r', encoding='utf-8') as f:
        file_content = f.read().lower()
    ustaw+= len(regex.findall(ustawa_regex, file_content))
    ustaw_z+= len(regex.findall(ustawa_z_z_dnia, file_content))
    ustaw_bez+= len(regex.findall(ustwa_bez_z_dnia, file_content))


print('ustaw : {}\nustaw_z : {}\nustaw_bez : {}\nustaw - (ustawa_z+ustaw_bez): {}'.format(ustaw,ustaw_z,ustaw_bez,ustaw-ustaw_z-ustaw_bez))