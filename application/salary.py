salaries = {
    "Junior Java разработчик":40000,
    "Junior+ Java разработчик":60000,
    "Middle Java разработчик":120000,
    "Senior Java разработчик":250000
    }

def calculate_salary(salaries, people):
    print(f"{'#':3s} {'Имя':14s} Оклад(руб)")
    print(f"{'-'*3} {'-'*14} {'-'*8}")
    for j,i in enumerate(people):
        print(f"{str(j+1)+'.':3s} {i[0]:14s} {salaries[i[1]]:,}".replace(","," "))

if __name__ == '__main__':
    from db.people import people
    calculate_salary(salaries, people)
