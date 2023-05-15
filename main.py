import csv

from dicts.it_dict import complete_d
from dicts.en_dict import english_d
from dicts.ch_dict import chinese_d


def add_italian_val(k):
    return complete_d[k]


def add_english_val(k):
    try:
        return english_d[k]
    except:  # if key does not exist
        return ""


def add_chinese_val(k):
    try:
        return chinese_d[k]
    except:  # if key does not exist
        return ""


def write_csv_line(k, italian_v, english_v, chinese_v, open_mode):
    with open('translations.csv', open_mode, newline='') as csv_file:
        csv_file.write('\n' + '"' + k + '";'
                            + '"' + italian_v + '";'
                           + '"' + english_v + '";'
                           + '"' + chinese_v + '";')
        csv_file.close()


write_csv_line("key", "it", "en", "ch", "w+")
for key in complete_d:
    it = add_italian_val(key)
    en = add_english_val(key)
    ch = add_chinese_val(key)
    write_csv_line(key, it, en, ch, "a")

