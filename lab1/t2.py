import regex
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


DATA_PATH  = '../data'
#
# ustawa_regex = r'ustaw(a|y|ie|ę|ą|o|y|om|ami|ach)'
#
# ustawa_z_z_dnia = r'ustaw(a|y|ie|ę|ą|o|y|om|ami|ach) z dnia'
# ustwa_bez_z_dnia =r'ustaw(a|y|ie|ę|ą|o|y|om|ami|ach)(?! \bz dnia\b)'
# ustawa_regex = r'ustaw(a|y|ie|ę|ą|o|y|om|ami|ach)'
ustawa_regex = r'(\bustawa\b|\bustawy\b|\bustawie\b|\bustawę\b|\bustawą\b|\bustawo\b|\bustawy\b|\bustaw\b|\bustawom\b|\bustawami\b|\bustawach\b)'

ustawa_z_z_dnia = ustawa_regex+r' z dnia'
ustwa_bez_z_dnia =ustawa_regex+r'(?! \bz dnia\b)'
ustawa_bez_o_zmiania = r'(?<!o zmianie )('+ustawa_regex+r')'
ustawa_z_o_zmianie = r'\bo \bzmianie\b ' + ustawa_regex


ustaw = 0
ustaw_z = 0
ustaw_bez = 0
usataw_bez_o_zmianie = 0
utawa_z_o_zmianie = 0

# print(regex.findall(ustwa_bez_z_dnia, 'ustawa z dnia'))


onlyfiles = [f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
for i, file in enumerate(onlyfiles):
    if i % 50 == 0:
        print('processing {}/{}'.format(i, len(onlyfiles)))
    file_content = None
    year = file.split('_')[0]
    with open(DATA_PATH+'/' + file, 'r', encoding='utf-8') as f:
        file_content = f.read().lower()
    # print(regex.findall(ustawa_regex,file_content))
    # print(regex.findall(ustawa_z_z_dnia,file_content))
    # print(regex.findall(ustwa_bez_z_dnia,file_content))
    # break
    ustaw+= len(regex.findall(ustawa_regex, file_content))
    ustaw_z+= len(regex.findall(ustawa_z_z_dnia, file_content))
    ustaw_bez+= len(regex.findall(ustwa_bez_z_dnia, file_content))
    usataw_bez_o_zmianie+= len(regex.findall(ustawa_bez_o_zmiania, file_content))
    utawa_z_o_zmianie+= len(regex.findall(ustawa_z_o_zmianie, file_content))


print('ustaw : {}\nustaw_z : {}\nustaw_bez : {}\nusatwa_bez_o_zmianie : {}\nustawa_z_o_zmianie : {}\nustaw - (ustawa_z+ustaw_bez): {}'.format(ustaw,ustaw_z,ustaw_bez,usataw_bez_o_zmianie,utawa_z_o_zmianie,ustaw-ustaw_z-ustaw_bez))
patches =[]
red_patch = mpatches.Patch(color='red', label='occurences \'ustawa\'')
green_patch = mpatches.Patch(color='green', label='occurences \'ustawa\' followed by \'z dnia\'')
yellow_patch = mpatches.Patch(color='yellow', label='occurences \'ustawa\' not followed by \'z dnia\'')
blue_patch = mpatches.Patch(color='blue', label='occurences \'ustawa\' not following \' o zmianie\'')
tick_label = ['' for i in range(4)]

plt.bar(0.5,ustaw,color ='red')
plt.bar(1.5,ustaw_z,color='green')
plt.bar(2.5,ustaw_bez,color='yellow')
plt.bar(3.5,usataw_bez_o_zmianie,color='blue')
plt.legend(handles =[red_patch,green_patch,yellow_patch,blue_patch])
plt.xlabel('expressions')
plt.ylabel('total matches')
plt.show()
