# new post
# test!!
# setup some global things yourself...
# argv[1] : title, argv[2] : category
import re

timezone = "+0900"
layout = "post"

from sys import argv
import datetime, os

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
if (len(argv) > 3):
    date = argv[3]
    
categoryList = argv[2].split(',')
dirn = '_posts/{0}/{1}'.format(categoryList[0] if len(categoryList) >= 1 else '', categoryList[1]+'/' if len(categoryList) == 2 else '')
print(dirn)
if not os.path.exists(dirn):
	os.makedirs(dirn)
filename = '{0}{1}-{2}.md'.format(dirn,date,re.sub("[\[\]\{\}\(\),/]", "",argv[1].replace(" ", "-").lower()))
filecont = "---\nlayout: " + layout
filecont +=  "\ntitle: \"{}\"".format(argv[1])
print(filecont)
filecont += "\ndate: " + (now.strftime("%Y-%m-%d %H:%M:00") if len(argv) <= 3 else date) + ' ' + timezone
filecont += "\ncategories: [{}{}]".format(categoryList[0] if len(categoryList) >= 1 else '',','+categoryList[1] if len(categoryList) == 2 else '')
#filecont += "\npublished: false"
filecont += "\n---\n\n"

writer = open(filename, "w")

writer.write(filecont)
print('Created Post')