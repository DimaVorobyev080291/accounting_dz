import datetime
from application.salary import calculate_salary
from application.people import get_employees

def new_datatime():
    current_time = datetime.datetime.now()
    print(current_time)
    print (current_time.strftime("%d-%m-%Y %H:%M:%S"))


if __name__ == '__main__':
    calculate_salary(5)
    get_employees(7)

    current_time = datetime.datetime.now()
    print(current_time)
    print (current_time.strftime("%d-%m-%Y %H:%M:%S"))
