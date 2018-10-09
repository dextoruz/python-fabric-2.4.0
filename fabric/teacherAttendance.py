
from datetime import datetime

def teacherAtt():
    lst = []
    filename1 = "teacher/monthlyAttendance.csv"
    filename2 = "teacher/todayAttendance.csv"
    with open(filename2,'r') as f2:
        with open(filename1, 'a') as f1:
            for i in f2:
                lst.append(i)
            f1.write(datetime.now().ctime().__str__() + ',' + lst[1])
