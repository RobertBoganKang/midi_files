import glob
import shutil
import os

fs = glob.glob(os.path.join('#competition', '**/*.mid'), recursive=True)
# for f in fs:
    # path_split = f.split('/')
    # name = path_split[-1]
    # if '-' in name:
        # name_split = name.split('-')
        # if name_split[0].isdigit():
            # new_name = '-'.join(name_split[1:]).replace(',', '')[:-3] + 'mid'
            # out_path = '/'.join(path_split[:-1] + [new_name])
            # print(out_path)
            # shutil.move(f, out_path)

for f in fs:
    path_split = f.split('/')
    name = path_split[-1]
    if '2006' in name:
        # new_name = name.split('Prize - ')[-1]
        new_name = name.replace('2006 ', '')
        out_path = '/'.join(path_split[:-1] + [new_name])
        print(out_path)
        shutil.move(f, out_path)

# for f in fs:
    # path = f[:-3] + 'mid'
    # shutil.move(f, path)
