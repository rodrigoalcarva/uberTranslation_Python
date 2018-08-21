#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 032
# 50011 Rodrigo Alcarva
# 50030 João Miguel

import readingFromFiles                      
from operator import itemgetter
import constants
import math
import dateTime

def scheduleTasks(translators, tasks, date, hour, periodAfter):

        """Assigns translation tasks to translators.
        
        Requires:
        translators is a dict with a structure as in the output of
        readingFromFiles.readTranslatorsFile concerning the update time; 
        tasks is a list with the structure as in the output of 
        readingFromFiles.readTasksFile concerning the period of
        periodAfter minutes immediately after the update time of translators;
        date is string in format DD:MM:YYYY with the update time;
        hour is string in format HH:MN: with the update hour;
        periodAfter is a int with the number of minutes of a period 
        of time elapsed.
        Ensures:
        a list of translation tasks assigned according to the conditions
        indicated in the general specification (omitted here for 
        the sake of readability).
        """
        ListSchedule = []
        
        ##print translators
        for tasksList in range(len(tasks)):                                                                                 #Para cada elemento na lista 
                ProbablyTranslators = []                                                                                        #Lista vazia
                PrimacyTask = tasks[tasksList][constants.INDEXTaskPriority]                                                     #Variavel PrimacyTask vai ser igual ao elemento da lista localizada na posição 5
                for transList in translators:
                        LanguageTrans1 = translators[transList][constants.INDEXTranslatorLanguageFromW]                             #From
                        LanguageTasks1 = tasks[tasksList][constants.INDEXTaskLanguageFrom]                                          #From
                        LanguageTrans2 = translators[transList][constants.INDEXTranslatorLanguageForW]                              #For
                        LanguageTasks2 = tasks[tasksList][constants.INDEXTaskLanguageFor]                                           #For
                        if LanguageTasks1 in LanguageTrans1 and LanguageTasks2 in LanguageTrans2:
                                NumberWordsTasks = int(tasks[tasksList][constants.INDEXTaskNumberWords])                #int(Fazer contas com este numero), numero de palavras da task
                                NumberWordsTrans = int(translators[transList][constants.INDEXTranslatorAccumulatedW])   #int(Fazer contas com este numero), numero de palavras que o translator já tem traduzidas
                                NumberMaxTrans = int(translators[transList][constants.INDEXTranslatorMaxAccumulatedW])  #int(Fazer contas com este numero), numero máximo de palavras que ele pode traduzir
                                if NumberWordsTasks + NumberWordsTrans <= NumberMaxTrans:                               #Se a soma do numero de palavras da task e do numero das palavras do tradutor for menor ou igualque o seu maximo
                                        newList= []
                                        newList.append(transList)
                                        newList.extend(translators[transList])
                                        ProbablyTranslators.append(newList)
        
                if len(ProbablyTranslators)>1:
                        for TRANS in ProbablyTranslators:
                                TRANS[8]=DayPerYear(TRANS[8])
                        if "quality" in PrimacyTask:
                                for TRANS in ProbablyTranslators:
                                        if TRANS[constants.INDEXTranslatorQuality]!='3*':
                                                ProbablyTranslators.remove(TRANS)
                                ProbablyTranslators=sorted(ProbablyTranslators, key=itemgetter(8, 4, 0))                
                        if "price" in PrimacyTask:
                                ProbablyTranslators=sorted(ProbablyTranslators, key=itemgetter(4, 3, 8, 0))
                        if "speed" in PrimacyTask:
                                ProbablyTranslators=sorted(ProbablyTranslators, key=itemgetter(8, 3, 4, 0))
                        ProbablyTranslators=[ProbablyTranslators[0]]
                        for TRANS in ProbablyTranslators:
                                TRANS[8]=DayPerYear(TRANS[8])
                
                if len(ProbablyTranslators)==1:
                        if "quality" in PrimacyTask:
                                for TRANS in ProbablyTranslators:
                                        if TRANS[constants.INDEXTranslatorQuality]!='3*':
                                                ProbablyTranslators.remove(TRANS)
                        taskList=[]
                        ProbablyTranslators = ProbablyTranslators[0]
                        cost = float(ProbablyTranslators[4])* int(tasks[tasksList][4])
                        time = int(tasks[tasksList][constants.INDEXTaskNumberWords]) / int(ProbablyTranslators[constants.INDEXTranslatorNumberWords])
                        final = dateTime.oneDay(time, ProbablyTranslators[8])
                        taskList.append(final)
                        taskList.append(ProbablyTranslators[0])
                        taskList.append(str(int(math.floor(cost))))
                        taskList.append(tasks[tasksList][0])
                        ListSchedule.append(taskList)
                        if ProbablyTranslators[0] in translators.keys():
                                inf = translators.get(ProbablyTranslators[0])
                                wordsAccumulated = int(ProbablyTranslators[constants.INDEXTranslatorAccumulated])+ int(tasks[tasksList][constants.INDEXTaskNumberWords])
                                inf[6] = wordsAccumulated
                                inf[7] = final
                                                           
                if len(ProbablyTranslators)==0:
                        NOT=[]
                        NOT.append(constants.NOTAssigned +' '+ 'and'+' '+  constants.NOTApplicable)
                        ListSchedule.append(NOT)

        return ListSchedule
        

def DayPerYear(day):
    """
    Swith format the date 
    Requires: A str in the format DD:MM:YYYY or YYYY:MM:DD
    Ensures: A str in the format DD:MM:YYYY or YYYY:MM:DD
    """
    d = day.split(":")
    switch=d[2]
    d[2]=d[0]
    d[0]=switch
    finalDate=str(d[0]+':'+d[1]+':'+d[2])

    return finalDate
