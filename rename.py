import os
import shutil
import datetime
import time

path='../new_puzzles'
nameList = os.listdir(path)
nameList.sort()

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 365

curDate = datetime.datetime.now()
curYear = curDate.year
if curYear % 4 == 0:
    months[1] = 29
    total = 366

lastName = nameList[len(nameList) - 1]
fixName = lastName[7:-4]

year = int(fixName[:2])
month = int(fixName[2:4])
day = int(fixName[4:])

for fileName in nameList[:total]:
    day = day + 1
    if day > months[month - 1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    monthStr = str(month)
    if len(monthStr) == 1:
        monthStr = '0' + monthStr
    dayStr = str(day)
    if len(dayStr) == 1:
        dayStr = '0' + dayStr
    output = str(year) + monthStr + dayStr
    print(output)
    os.rename(path + '/' + fileName, path + '/puzzle_' + output + '.xml')