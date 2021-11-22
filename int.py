import os
import json
import xml
encoding = 'utf-8'
class Man:
    nam = str 
    Age = int

my_file = open("BabyFile.txt", "w+")
my_file.write("Привет, файл!")
my_file.close()
file = open("BabyFile.txt", "r")
print(file.read())
file.close()
os.remove("BabyFile.txt")

jsonfile = open("BabyFile.json", "w+")
me = Man()
me.Age=21
me.nam="Ilias"
jsonstr = json.dumps(me, default=lambda o: o.__dict__, sort_keys=True, indent=4)
print(jsonstr)
jsonfile.write(jsonstr)
jsonfile.close()
jsonfile = open("BabyFile.json", "r")
print(jsonfile.read())
jsonfile.close()
os.remove("BabyFile.json")

import xml.etree.ElementTree as ET
name1=input()
name2=input()
data = ET.Element(name1)
item = ET.SubElement(data,name2)
mydata = ET.tostring(data)
file = open("items.xml","w+")
file.write(mydata.decode(encoding))
file.close()

myfile =open ("items.xml","r")
print(myfile.read())
myfile.close()
os.remove("items.xml")

file = open(os.environ['USERPROFILE'] + '\Desktop'+'\items.txt',"w+")
file.write("asdasdasdasd")
file.close()
import shutil
shutil.make_archive(os.environ['USERPROFILE'] + '\Desktop' +'\pet1', 'zip', os.environ['USERPROFILE'] + '\Desktop','items.txt')
import zipfile
#print(os.environ['USERPROFILE'] + '\Desktop' +'\pet.zip')
fantasy_zip = zipfile.ZipFile(os.environ['USERPROFILE'] + '\Desktop' +'\pet1.zip')
fantasy_zip.extract('items.txt',os.environ['USERPROFILE'] + '\Desktop'+'\ecxFiles')
fantasy_zip.close()

file = open(os.environ['USERPROFILE'] + '\Desktop'+'\ecxFiles'+'\items.txt',"r")
print(file.read())
file.close()

shutil.rmtree(os.environ['USERPROFILE'] + '\Desktop'+'\ecxFiles')
os.remove(os.environ['USERPROFILE'] + '\Desktop'+'\items.txt')
os.remove(os.environ['USERPROFILE'] + '\Desktop'+'\pet1.zip')