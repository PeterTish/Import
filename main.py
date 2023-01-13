from salary import calculate_salary
from people import get_employees
from datetime import datetime








if __name__ == '__main__':
    print(f'На {datetime.now()} в твоей команде: {get_employees()}')
    print(calculate_salary())


