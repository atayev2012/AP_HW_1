from datetime import datetime
from application.db.people import people, get_employees
from application.salary import salaries, calculate_salary
import pandas as pd

def date_now():
    dt = datetime.now()
    print(dt.strftime("%X - %A, %d %B %Y"))

def data_gen_for_padnas(people, salaries):
    data_dict = {"Имя":[],"Должность":[],"Оклад":[]}
    for i in people:
        data_dict["Имя"].append(i[0]) 
        data_dict["Должность"].append(i[1]) 
        data_dict["Оклад"].append(salaries[i[1]])
    return data_dict


if __name__ == '__main__':
    date_now()
    get_employees(people)
    print()
    date_now()
    calculate_salary(salaries, people)
    print()
    print("через Pandas")
    date_now()
    print(pd.DataFrame(data_gen_for_padnas(people, salaries)))
