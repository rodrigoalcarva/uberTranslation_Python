#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 032
# 50011 Rodrigo Alcarva
# 50030 João Miguel

import constants 

def removeHeader(file_name):
    """ Pass the save header forward
    Requires: Name of a file in str and fuction constants
    Ensures: Begins reading the file after the header ends
    """
    for lines in range(constants.NUMBEROfLinesInHeader):
        file_name.readline()
    return file_name
   
def saveHeader(file_name):
    """ Reads the file and returns the Header
    Requires: A .txt file
    Ensures: The Header associated to the txt file
    """
    lines = file_name.readlines()
    lines = lines[:7]
    
    return lines
        
    
    
def readTranslatorsFile(file_name):
    """Reads a file with a list of translators into a collection.
    Requires:
    file_name is str with the name of a .txt file containing
    a list of translators organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    dict where each item corresponds to a translator listed in
    file with name file_name, a key is the string with the name of a translator,
    and a value is the list with the other elements belonging to tha
    translator, in the order provided in the lines of the file.
    """

    inFile = removeHeader(open(file_name, "r"))     

    transDict = {}
    transList = []
    
    for line in inFile:
        transData = line.rstrip().split(", ")
        transList.append(transData)
        if len(line)>1:
            for x in range(len(transList)):
                transDict[transList[x][constants.INDEXTranslatorName]] = transList[x][constants.INDEXTranslatorLanguageFrom:]

    
                

    return transDict

       
        
def readTasksFile(file_name):
    """Reads a file with a list of translation tasks into a collection.
    Requires:
    file_name is str with name of a .txt file containing a list of tasks organized
    as in the examples provided in the general specification (omitted here in the
    sake of readability).
    Ensures:
    List where each item corresponds to a task listed in file with name file_name,
    key is string with the name of a translator, and a value is the list with the
    other elements belonging to that task, in the order provided in the lines of the
    file.
    """

    inFile = removeHeader(open(file_name, "r"))       

    tasksList = [] 
    for line in inFile:
        taskData = line.rstrip().split(", ")
        tasksList.append(taskData)

    return tasksList


def readTime(file_name):
    """ This function read the time
    Requires: 
    Ensures:
    """
    inFile = open(file_name, "r")
    lines = inFile.readlines()
    return lines[constants.NUMBERofLineTime].rstrip()


def readDate(file_name):
    """ This function read the date
    Requires:
    Ensures:
    """
    inFile = open(file_name, "r")
    lines = inFile.readlines()
    return lines[constants.NUMBERofLineDate].rstrip()

