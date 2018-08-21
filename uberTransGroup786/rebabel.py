#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 032
# 50011 Rodrigo Alcarva
# 50030 João Miguel


import constants
import dateTime
import scheduling
import readingFromFiles
import writingToFiles
from sys import argv


def assign(translatorsFileName, tasksFileName):
    """Obtains the assignment of translation tasks to translators.

    Requires:
    translatorsFileName is a str with the name of a .txt file containing a list
    of translators, organized as in the examples provided;
    tasksFileName is a str with the name of a .txt file containing a list
    of translation tasks requested in the 10 minute period right after the update
    time of translatorsFileName, organized as in the examples provided;
    both these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the list of translation tasks assigned
    to translators and the updated list of translators, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    translatorsXXhYY.txt, where XXhYY represents the time and date 10 minutes
    after the time and date indicated in the files translatorsFileName and 
    tasksFileName, and are written in the same directory of the latter.
    """
    translators = readingFromFiles.readTranslatorsFile(translatorsFileName)
    tasks = readingFromFiles.readTasksFile(tasksFileName)
    time = readingFromFiles.readTime(translatorsFileName)
    day = readingFromFiles.readDate(translatorsFileName)
    date = dateTime.ten_minutes(time,day)[0]
    hour = dateTime.ten_minutes(time,day)[1]
    schedule = scheduling.scheduleTasks(translators, tasks, date, hour, 10)
    file_name = 'schedule'+hour.replace(':','h')+'.txt'
    header = readingFromFiles.saveHeader(open(tasksFileName))
    writingToFiles.writeScheduleFile(schedule, file_name, header)
    file_name = 'translators' + hour.replace(':','h')+'.txt'
    translatorsUpdated = translators
    writingToFiles.writeTranslatorsFile(translatorsUpdated, file_name, header)

##    try:
##        header = readingFromFiles.saveHeader(open(translatorsFileName))
##        trans_fileTime = translatorsFileName[11:16]
##        headerTime = header[5].replace(':','h')
##        assert headerTime == trans_fileTime 
##
##    except AssertionError:
##        raise IOError('Input file error: scope or time inconsistency between name and header in file ' + translatorsFileName)
##
##    try:
##        header = readingFromFiles.saveHeader(open(tasksFileName))
##        tasks_fileTime = tasksFileName[5:10]
##        headerTime = header[5].replace(':','h')
##        assert headerTime == tasks_fileTime
##
##    except AssertionError:
##        raise IOError('Input file error: scope or time inconsistency between name and header in file ' + tasksFileName)


assign(argv[1], argv[2])
        

