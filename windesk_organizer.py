import os
from datetime import datetime
from tkinter import messagebox
import shutil




org_path = os.path.expanduser('~' + '\\Desktop\\')

typelookup = ['png', 'jpg', 'jpeg', 'pdf']


class organizer:


    def __init__(self) -> None:
        
        self.timestamp = self.get_date()
        self.items = None
        self.file_detect()


    
    def get_date(self):
        now = datetime.now().strftime('%d%m%Y_%H%M')
        return now
    

    def file_detect(self):

        files = os.listdir(org_path)
        detected = []

        for file in files:

            for type in typelookup:
                if file.endswith(type):
                    detected.append(file)
                
        print(detected)

        #if there's file matches lookup
        #assign them to instance variable 'self.items'
        if len(detected) > 0:
            self.items = [i for i in detected]
            print(f"self.items = {self.items}")


    def create_folder(self):

        if self.items is not None:

            #create a folder that named with timestamp
            foldername = 'organize_' + self.timestamp
            create_path = os.path.join(org_path, foldername)
            os.mkdir(create_path)

            for item in self.items:
                shutil.move(org_path + item, create_path)

        else:
            messagebox.showinfo('Files not found', f'No {typelookup} files in {org_path}')
            return False



    def main(self):
        self.create_folder()




if __name__ == '__main__':


    inst1 = organizer()
    inst1.main()