'''
Created on Dec 5, 2016

@author: ryanmann
'''
import sys
import os 

def createlist(directory):
    '''Creates a list consisting of strings of the file names'''
    filelist=[]
    for file in os.listdir(directory):
        filelist.append(file)
    return filelist
        
def findduplicates(filelist):
    '''Returns a list of duplicate files.'''
    duplicates = []
    realduplicates = []
    names = []
    for file in filelist:
        name = file[0:5]
        names.append(name)
    for name in names:
        if names.count(name) != 1 and name not in duplicates:
            duplicates.append(name) 
    for name in duplicates:
        index = names.index(name)
        realduplicates.append(filelist[index])

    return realduplicates

if __name__ == '__main__':
    input_dir = sys.argv[1]
    filelist = createlist(input_dir)
    duplicates = findduplicates(filelist)
    print "Duplicate files:",duplicates
    