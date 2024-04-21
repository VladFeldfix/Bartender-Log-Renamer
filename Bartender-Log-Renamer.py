# Download SmartConsole.py from: https://github.com/VladFeldfix/Smart-Console/blob/main/SmartConsole.py
from SmartConsole import *
import os

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("Bartender Log Renamer", "1.0")
        
        # set-up main memu
        self.sc.add_main_menu_item("RUN", self.run)

        # get settings
        self.main_path = self.sc.get_setting("BarTender Logs")

        # test all paths
        self.sc.test_path(self.main_path)

        # display main menu
        try:
            self.sc.start()
        except Exception as e:
            print(str(e))
    
    def run(self):
        try:
            path = self.main_path.replace("\\", "/")
            path = path.split("/")
            pathlength = len(path)
            for path, dirnames, filenames in os.walk(self.main_path):
                for file in filenames:
                    path = path.replace("\\", "/")
                    path_split = path.split("/")
                    if len(path_split) == pathlength and len(file) == 12:
                        newfilename = file[4:8]+"-"+file[0:2]+"-"+file[2:4]+".txt"
                        self.sc.print("Changing "+file+" To "+newfilename)
                        os.rename(path+"/"+file, path+"/"+newfilename)
            self.sc.restart()
        except Exception as e:
            self.sc.fatal_error(str(e))

main()