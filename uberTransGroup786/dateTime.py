#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 032
# 50011 Rodrigo Alcarva
# 50030 Joao Miguel Pinto


###################################TIME#########################################

def hourToInt(time):
    """Hour of a given time
    Requires: A String of the time with two dots dividing the hours
    from the minutes
    Ensures: Returns a int with the hour 
    """
    h = time.split(":")
    return int(h[0])



def minutesToInt(time):
    """ This function tells the minutes that we give
    Requires: int time and time > 0
    Ensures: Returns in int the minutes of the given time
    """
    m = time.split(":")
    return int(m[1])



def intToTime(hour, minutes):
    """ This Function tells the hour and minutes with ":"
    Requires: h and m str and h and m > 0 and m < 24
    Ensures: Returns in int the hours plus ":" plus minutes
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h
        
    if minutes < 10:
        m = "0" + m

    return h + ":" + m


###################################DATE#########################################


def dayToInt(date):
    """ This function tells the day that we give
    Requires: int day and day > 0
    Ensures: Returns in int the day of the given date
    """
    
    d = date.split(":")
    return int(d[0])


def monthToInt(date):
    """ This function tells the month that we give
    Requires: int month and month >0
    Ensures: Returns in int the month of the given date
    """
    m = date.split(":")
    return int(m[1])

def yearToInt(date):
    """ This function tells the year that we give
    Requires: int year and year > 0
    Ensures: Returns in int the year of the given date
    """
    y = date.split(":")
    return int (y[2])

def intToDate(day, month, year):
    """ This Function tells the day, month and year with ":"
    Requires: day, month and year str and day, month and year >0
    Ensures: Returns in int the day plus ":" plus month plus ":" plus year
    """
    d= str(day)
    m= str(month)
    y= str(year)
    
    if day < 10:
        d = "0" + d
        
    if month < 10:
        m = "0" + m

    return d + ":" + m + ":" + y

################################10MINUTES######################################

def ten_minutes(time,date):
    """ This function add ten minutes at the variables minutes.
    Requires: add string
    Ensures: Add 10 minutes and convert for hours
    """
    h = hourToInt(time)
    m = minutesToInt(time)
    d = dayToInt(date)
    M = monthToInt(date)
    y = yearToInt(date)
    add = m + 10
    if add >= 60:
        add = add - 60
        h += 1
        if h >= 24:
            h = 00
            d += 1
            if d > 31 and (M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12):
                M += 1
                d = d - 31
            if d > 30 and (M==4 or M==6 or M==9 or M==11):
                M += 1
                d = d - 30
            if d > 28 and M==2:
                M += 1
                d = d - 28
            if M> 12:
                y += 1
                M=1
    return intToTime(h, add), intToDate(d, M, y)

def oneDay(days,date):
    """ This function add days to date
    Requires: a int day and a str date
    Ensures: A str in the format DD:MM:YYYY after the add
    """
    d = dayToInt(date)
    M = monthToInt(date)
    y = yearToInt(date)
    finalDate = d + days
    for f in range(finalDate):
        if finalDate > 31 and (M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12):
            M += 1
            finalDate = finalDate - 31
        if finalDate > 30 and (M==4 or M==6 or M==9 or M==11):
            M += 1
            finalDate = finalDate - 30
        if finalDate > 28 and M==2:
            M += 1
            finalDate = finalDate - 28
        if M> 12:
            y += 1
            M=1

    return intToDate(finalDate,M,y)

def DayPerYear(day):
    """
    Swith format the date 
    Requires: A str in the format DD:MM:YYYY or YYYY:MM:DD
    Ensures: A str in the format DD:MM:YYYY or YYYY:MM:DD
    """
    d = day.split(":")
    change = d[2]
    d[2]=d[0]
    d[0]=change
    finalDate=str(d[0]+':'+d[1]+':'+d[2])

    return finalDate

