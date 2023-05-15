import csv
import os

italian_dict = {}
english_dict = {}
chinese_dict = {}


with open("translations.csv", "r", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        key = row[0]
        italian_dict[key] = row[1]
        english_dict[key] = row[2]
        chinese_dict[key] = row[3]


directory_name = "OUT_JS_DICT_FILES"


def updateIt():
    f = open(os.path.join(directory_name, "italian.js"), "w+")
    f.write("const it = " + str(italian_dict))
    f.close()
    f = open(os.path.join("dicts", "it_dict.py"), "w+")
    f.write("complete_d = " + str(italian_dict))
    f.close()

def updateEn():
    f = open(os.path.join(directory_name, "english.js"), "w+")
    f.write("const en = " + str(english_dict))
    f.close()
    f = open(os.path.join("dicts", "en_dict.py"), "w+")
    f.write("english_d = " + str(english_dict))
    f.close()

def updateCh():
    f = open(os.path.join(directory_name, "chinese.js"), "w+")
    f.write("const ch = " + str(chinese_dict))
    f.close()
    f = open(os.path.join("dicts", "ch_dict.py"), "w+")
    f.write("chinese_d = " + str(chinese_dict))
    f.close()


updateIt()
updateEn()
updateCh()





