import sys
import time
import random

import os 
import shutil
 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 

from_dir = "C:/Users/intex/Downloads"
to_dir = "C:/Users/intex/Desktop/alish ali"

dir_tree= {
    "Image_file":['.jpg','.jpeg','.png','.gif']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):

        name,extention = os.path.splitext(event.src_path)

        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extention in value:

                file_name = os.path.basename(event.src_path)

                print("Downloads"+file_name)

                path1 = from_dir + '/'+ file_name
                path2 = to_dir +'/' + key
                path3 = to_dir + '/' +key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving" + file_name + "....")
                    shutil.move(path1,path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("moving" + file_name + "....")
                    shutil.move(path1,path3)
                    time.sleep(1)

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir,recursive=True)

observer.start()

while True:
    
    time.sleep(2)
    print("running...")

