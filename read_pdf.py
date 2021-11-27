# my_roots_list//lippincottlibrary.wordpress.com/2020/02/05/python-find-files-with-os-walk/
import os
def list_files(filepath, filetype):
    paths = []
    roots = []
    path1 = []
    file1 = []
    path = ''
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()) and os.path.isfile(os.path.join(root, file)):
                paths.append(os.path.join(root, file))
                roots.append(root)
                path = os.path.join(root, file)
                path1.append(path[path.find('\\',4,len(path)):])
                file1.append(file)
    return(roots,path1,paths,file1)

my_roots_list,my_path_list,my_files_list,my_filenames_list = list_files('.\\2021', '.pdf')