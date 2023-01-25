try:
    your_salary = int(input('Твой зарплата в месяц: '))
except (SyntaxError, ValueError):
    your_salary = 10000
try:
    your_working_day = int(input('Твой рабочий день в часах: '))
except (SyntaxError, ValueError):
    your_working_day = 8

def calculate_salary():
    year_salary = your_salary * 12
    day_salary = your_salary / 30
    hours_salary = day_salary / your_working_day
    minutes_salary = hours_salary / 60
    return(f'Твоя зарплата в год: {year_salary}\nТвоя зарплата в день: {round(day_salary, 2)}\nТвоя зарплата в час: {round(hours_salary, 2)}\n'
           f'Твоя зарплата в минуту: {round(minutes_salary, 2)}')