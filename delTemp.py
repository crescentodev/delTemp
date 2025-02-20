import os
import shutil
folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'

del_count_files = 0
del_count_dir = 0

def deleteThem():
    global del_count_dir, del_count_files
    for files in os.listdir(folder):
        item_path = os.path.join(folder, files)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
                del_count_files += 1
            
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                del_count_dir += 1
        except PermissionError:
            print(f"Permission denied: {item_path}")
        except Exception as e:
            print(f"Error deleting {item_path}: {e}")

if __name__ == "__main__":
    deleteThem()
    print(f"Detected files: {del_count_files} and folders: {del_count_dir}")
    input("Press Enter")


