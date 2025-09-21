# Запуск всех тестов с генерацией данных для отчета
pytest --alluredir=allure-results

# Запуск только тестов калькулятора
pytest test_calculator.py --alluredir=allure-results

# Запуск только тестов интернет-магазина
pytest test_shop.py --alluredir=allure-results

# Запуск с подробным выводом
pytest -v --alluredir=allure-results

# После выполнения тестов сгенерируйте HTML-отчет из полученных данных:
allure generate allure-results -o allure-report --clean

# Просмотр отчета через команду allure open (рекомендуется):
allure open allure-report

# Через веб-сервер Allure:
allure serve allure-results

# Прямое открытие файла. Откройте файл allure-report/index.html в любом современном браузере.

# Структура отчета Allure
# После открытия отчета вы увидите:
# Overview - общая статистика выполнения тестов
# Categories - группировка тестов по статусу выполнения
# Suites - тесты, сгруппированные по тестовым наборам
# Graphs - графики и диаграммы с статистикой выполнения
# Timeline - временная шкала выполнения тестов