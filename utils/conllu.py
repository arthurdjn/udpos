# -*- coding: utf-8 -*-
# Created on Sun Mar 15 00:51:53 2020
# @author: arthurd



def conllu2txt(filename):
    """Convert a conllu file to a txt tab separated table.
    The converted file is saved in the same directory as the original file.
    The txt file structure follows the one from torchtext UD datasets.
    
    Parameters
    ----------
    filename : str
        Path to the conllu file.

    Returns
    -------
    None. Write a txt file.
    """
    # The template of a conllu file is described as follow:
    # #SENT_ID #TEXT | ID FORM LEMMATIZED UDPOS XPOS FEAT HEAD DEPREL DEPS MISC
    #
    # Template used : TEXT   LEMMATIZED   UDPOS 
    # header = "TEXT\tLEMMATIZED\tUDPOS" + "\n"    
    document = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # Get the id and full text in a separate column
            if line[0] != '#':
                # Select the fields (all are not important for our tasks)
                document += '\t'.join(line.split('\t')[1:4]) + '\n'
    
    # Saving as a tab separated txt file
    with open(filename.replace('.conllu', '.txt'), 'w', encoding='utf-8') as f:
        f.write(document)
    





