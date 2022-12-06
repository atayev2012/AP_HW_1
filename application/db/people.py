people = [
    ["Батыр А.", "Junior Java разработчик"],
    ["Андрей Б.", "Junior+ Java разработчик"],
    ["Леонид У.", "Junior+ Java разработчик"],
    ["Артем В.", "Middle Java разработчик"],
    ["Владимир А.", "Middle Java разработчик"],
    ["Анатолий Г.", "Senior Java разработчик"]
    ]

def get_employees(people):
    print(f"{'#':3s} {'Имя':14s} {'Должность'}")
    print(f"{'-'*3} {'-'*14} {'-'*30}")
    for i,j in enumerate(people):
        print(f"{str(i+1)+'.':3s} {j[0]:14s} {j[1]}")

if __name__ == '__main__':
    get_employees(people)