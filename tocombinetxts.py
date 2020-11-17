import os
import sys

walk_dir = './'

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
import os
import subprocess
list_file2 = ""
def doDatFlle(file_path):
    global list_file2
    try:
        f_content = str(subprocess.check_output('html2text "' + file_path + '" "utf-8"', shell=True))
        #print(f_content)


        list_file2 = list_file2 + (('<|startoftext|>'))
        list_file2 = list_file2 + ((f_content))
        list_file2 = list_file2 + (('<|endoftext|>'))
    except Exception as e:
        if 'No such file or directory' not in str(e) and ' returned non-zero exit status 1' not in str(e):
            print(e)
import threading
from time import sleep
oldlen = 0
files2 = []
for filename in os.listdir(os.getcwd()):
        files2.append(filename)
oldlen = len(files2)
        #list_file_path = os.path.join('my-directory-list-' + root.replace('./', '').replace('\\','') + '.txt')
        #print('list_file_path = ' + list_file_path)
"""
with open(list_file_path, 'wb') as list_file:
oldlen = oldlen + len(files)
print(oldlen)
for file in files:
    files2.append(file)
"""
count = 0

            
while (len(files2)) > 0:
    filename = files2[0]
    file_path = os.path.join('./', filename)
    if threading.activeCount()<=32:
        try:
            size = os.path.getsize(file_path)
        except:
            
            size = 1025
        #print(size)
        if size > 1024:
            #print('\t- file %s (full path: %s)' % (filename, file_path))
            if '.html' in file_path and 'my-directory-list' not in file_path:
                #print(file_path)
                print(str(count) + ' / ' + str(oldlen) + ', ' + str(round((count / oldlen) * 10000) / 100) + '%')
                print(len(list_file2))
                t = threading.Thread(target=doDatFlle, args=(file_path,))
                t.daemon = True
                t.start()
        count = count + 1
        files2.pop(0)
    else:
        sleep(0.2)
sleep(10)
with open('out.txt', 'w') as list_file:
    list_file.write(list_file2)
            