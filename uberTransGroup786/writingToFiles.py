#-*- coding: utf-8 -*-

# 2016-2017 Fundamentos de Programacao
# Grupo 032
# 50011 Rodrigo Alcarva
# 50030 João Miguel

from readingFromFiles import *
from constants import *
from dateTime import *
from scheduling import *
from sys import argv

def writeScheduleFile(tasksAssigned, file_name, header):
    """Writes a collection of services into a file.
    Requires:
    tasksAssigned is a list with the structure as in the output of
    scheduling.scheduleTasks representing the translation tasks assigned;
    file_name is a str with the name of a .txt file;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability).
    Ensures:
    writing of file named file_name representing the list of
    translation tasks in tasksAssigned prefixed by header and 
    organized as in the examples provided  in the general specification 
    (omitted here for the sake of readability);
    the listing in this file keeps the ordering top to bottom of 
    the translations tasks as ordered head to tail in tasksAssigned.
    """
    time = readingFromFiles.readTime(argv[1])       #reads the time
    day  = readingFromFiles.readDate(argv[1])       #reads the date
    date = dateTime.ten_minutes(time,day)[0]        #plus 10 min
    hour = dateTime.ten_minutes(time,day)[1]
    header[3]=date+'\n'
    header[5]=hour+'\n'
    outFile = open(file_name,"w")
    notassined = False
    List=[]
    for task in tasksAssigned:
        if task[0] != 'not-assigned and not-applicable':     #if theres isnt a date to sort
            task[0]=DayPerYear(task[0])
            List.append(task)
            notassined = True
    tasksAssigned = sorted(List, key=itemgetter(0))
    for task in tasksAssigned:
        task[0]=DayPerYear(task[0])                         #will change the dd-mm-yyy to yyyy-mm-dd , to sort properly
    for line in header:
        outFile.write(str(line))
    for task in tasksAssigned:
        for elem in task:
            outFile.write(str(elem)+', ')
        outFile.write('\n')
    if notassined:
        outFile.write('not-assigned and not-applicable\n')   


def writeTranslatorsFile(translatorsUpdated, file_name, header):
    """
    Writes a collection of translators into a file.
    Requires:
    translatorsUpdates is a list with the structure as in the output of
    scheduling.scheduleTasks representing the updated translators;
    file_name is a str with the name of a .txt file;
    header is a string with a header, as in the examples provided in 
    the general specification.
    Ensures:
    writing of file named translators + updated time representing the list of
    translators and their info in translatorsUpdated prefixed by header and 
    organized as in the examples provided  in the general specification 
    (omitted here for the sake of readability);
    the listing in this file keeps the ordering top to bottom of 
    the translations tasks as ordered head to tail in translatorsUpdated.
    """
    time = readingFromFiles.readTime(argv[1])
    day = readingFromFiles.readDate(argv[1])
    date = dateTime.ten_minutes(time,day)[0]
    hour = dateTime.ten_minutes(time,day)[1]
    header[3]=date+'\n'
    header[5]=hour+'\n'
    outFile=open(file_name,"w")
    for line in header:
        outFile.write(str(line))
    for trad in translatorsUpdated:
        outFile.write(str(trad)+', ')
        for info in translatorsUpdated.get(trad):
            outFile.write(str(trad)+', ')
        outFile.write('\n')
    outFile.close()
