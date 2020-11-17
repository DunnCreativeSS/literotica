import os
import sys

walk_dir = './'

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):

    print('--\nroot = ' + root)
    if root is not './' and '.git' not in root:
        list_file_path = os.path.join(root, 'my-directory-list-' + root.replace('./', '').replace('\\','') + '.txt')
        print('list_file_path = ' + list_file_path)

        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print('\t- subdirectory ' + subdir)

            for filename in files:
                file_path = os.path.join(root, filename)

                print('\t- file %s (full path: %s)' % (filename, file_path))
                if '.txt' in file_path and 'my-directory-list' not in file_path:
                    print(file_path)
                    with open(file_path, 'rb') as f:
                        f_content = f.read()
                        try:
                            list_file.write(('<|startoftext|>').encode('utf-8'))
                            list_file.write((f_content))
                            list_file.write(('<|endoftext|>').encode('utf-8'))
                        except Exception as e:
                            print(e)
    