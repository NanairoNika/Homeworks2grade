import re
import os
filenames = []
texts = []
author = []
year = []
for root,dirs,files in os.walk('D:/Downloads/news'):
        filenames = files
        for file in files:
                if re.match('.+\.xhtml', file):
                          with open(file) as f:
                                text = f.read()
                                f.close()
                                author = re.findall('<meta content=.+name="author"', text)
                                author = re.sub('<meta content="','',author)
                                author = re.sub('" name="author"/>','',author)
                                year = re.findall('<meta content=.+name="created"', text)
                                author = re.sub('<meta content="','',year)
                                author = re.sub('" name="created"/','',author)
                                print (file, author, year) 
                                words = re.findall('<w>.+</w>', text)           
                                fl = open ('counter.txt', 'a', encoding = 'utf-8')
                                fl.write(file)
                                fl.write('\t')
                                fl.write(str(len(words)))
                                fl.write('\n')
                                fl.close()
