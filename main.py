from utils import *
from dbmanager import *
from settings import *

# список интересующих работодателей
target_employers = ['Тинькофф', 'Компания Лимарк', 'Carbon Soft', 'Тензор', 'ЭР-Телеком',
                    'KVINT', 'InfiNet Wireless', 'URALNIX', 'OmniLine', 'УрГУПС']

employers_info = parse_employers_info(target_employers)

# подключение к БД
db_manager = DBManager(
    host=host,
    database=database,
    user=user,
    password=password
)

# создание таблиц и заполнение их информацией
db_manager.create_tables()
db_manager.insert_data(employers_info)

# применение описанных в классе методов
companies_and_vacancies = db_manager.get_companies_and_vacancies_count()
all_vacancies = db_manager.get_all_vacancies()
avg_salary = db_manager.get_avg_salary()
vacancies_higher_salary = db_manager.get_vacancies_with_higher_salary()
keyword_vacancies = db_manager.get_vacancies_with_keyword('Инженер-электрик')

print(companies_and_vacancies)

# закрытие подключения к БД
db_manager.close_connection()