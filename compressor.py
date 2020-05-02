from os import listdir, walk, makedirs
from os.path import exists, isdir, join, relpath, split
from subprocess import Popen
from sys import argv


def has_subdir(directory):
    for file in listdir(directory):
        if isdir(join(directory, file)):
            return True
    return False


def comp(target_root, directory):
    for root, dirs, files in walk(directory, topdown=False):
        for d in dirs:
            source_dir = join(root, d)
            if not has_subdir(source_dir):
                target_file = split(join(target_root, relpath(source_dir, directory)))
                if not exists(target_file[0]):
                    makedirs(target_file[0])
                Popen(f'"C:/Program Files/WinRAR/Rar.exe" a -m5 -ma5 -rr20 -s -md1g -oi- -htb -qo- -ts -ep "{join(target_file[0], target_file[1])}.rar" "{source_dir}/*"').wait()


if __name__ == '__main__':
    source = argv[1]
    target = argv[2]
    comp(target, source)
