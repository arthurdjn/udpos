# -*- coding: utf-8 -*-
# Created on Sun Mar 15 00:51:53 2020
# @author: arthurd


import os


def open_files(dirpath, ext="conllu"):
    """Get the path of all files in a directory.

    Parameters
    ----------
    dirpath : string
        Name or path to the directory where the files you want to
        open are saved..
    ext : string, optional
        The files extension you want to open. The default is "conllu".

    Returns
    -------
    list
        A list of the path of all files saved in the directory.
   

    Example
    -------
        >>> dir_name = "path/to/your/directory"
        >>> files = open_files(dir_name, ext="geojson")
        >>> files
            ['fr_gsd-ud-dev.conllu',
             'fr_gsd-ud-train.conllu',
             'fr_gsd-ud-test.conllu']
    """
    try :
        ls = os.listdir(dirpath)
    except FileNotFoundError as e:
        raise e('the path to the directory was not found')
    files_list = []
    for f in ls :
        if f.endswith(ext):
            filename = os.path.join(dirpath, f)
            files_list.append(filename)
    return files_list



if __name__ == "__main__":
    
    from conllu import conllu2txt
    
    # Load all conllu files in directory
    print("Getting the path to conllu files...")
    dirpath = 'conversion'
    files = open_files(dirpath)
    print("Done.")

    # Convert the conllu files to txt
    print("\nConverting...")
    for filename in files:
        print("\tConverting {}".format(filename.split(os.sep)[-1]))
        conllu2txt(filename)
    print("Done.")



