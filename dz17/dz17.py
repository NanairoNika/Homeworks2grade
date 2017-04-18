import re
import os

allfolders = []
kirfold = []
    
def CyrillicFolders():
    for root, dirs, files in os.walk('C:/Users/student/Documents'):
        allfolders.append(dirs)
    print (allfolders)
    for flayer in allfolders:
        for slayer in flayer:
            if re.match ('([а-яА-Я])+', slayer):
                kirfold.append(slayer)
    return kirfold


def main()
    kirfold = CyrillicFolders()
    print (len(kirfold))


main()

