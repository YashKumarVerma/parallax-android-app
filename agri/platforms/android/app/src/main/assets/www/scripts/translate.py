# using https://pypi.python.org/pypi/googletrans
# pip install googletrans

import sys
import shutil
from googletrans import Translator
from datetime import datetime
translator = Translator()

"""
FILE HANDLES
"""
languageList = [line.rstrip() for line in open("./languages.ykv")]
jsonData= [line.rstrip() for line in open(sys.argv[1])]

print(jsonData)

log = open("./worklog.ykv","w");
# print(languageList);
# print(jsonData);
print("***********************************************************\n\n");
print(" TRANSLATING BOT APPLICATION \n");
print(" https://github.com/yashkumarverma/\n\n")
print("***********************************************************");

log.write("***********************************************************\n\n");
log.write(" TRANSLATING SUSI AI CHAT APPLICATION \n");
log.write(" https://github.com/yashkumarverma/\n\n")
log.write("***********************************************************");

"""
TRANSLATE ITEMS
"""
for language in languageList:
	log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Working on language : "+language+"\n");
	log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Translation to " + language + " started\n")
	
	# translate
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Translation to " + language + " started");
	translations = translator.translate(jsonData, dest=str(language));
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Translation to " + language + " completed");
	log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Translation to " + language + " completed\n");
	
	# create json, build file and save
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Export to json for " + language + " started");
	log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"Export to json for " + language + " started");
	jsonFile = open("build/"+language+".json","w",encoding="utf8");
	jsonRender = "{";
	for translation in translations:
		jsonRender= jsonRender+'"'+translation.origin+'":'+'"'+translation.text+'",';
	jsonRender = jsonRender[:-1]
	jsonRender += "}";
	jsonFile.write(jsonRender);
	jsonFile.close();
	log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"Export to json for " + language + " completed");
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Export to json for " + language + " completed");

	# write logs
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Translation to " + language + " completed");	
	log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Translation to " + language + " completed \n --- \n")

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Export to zip ...");
log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"starting zip export");
# creating zip
shutil.make_archive("translated", "zip", "build")
log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"zip export complete");
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|\t\t"+"Everything Done.");

print("***********************************************************\n\n");
print(" Converted Application to 102 Languages \n");
print(" Original Work of Yash Kumar Verma \n\n")
print("***********************************************************");

log.write("***********************************************************\n\n");
log.write(" Converted Application to 102 Languages \n");
log.write(" Original Work of Yash Kumar Verma \n\n")
log.write("***********************************************************");

log.close();