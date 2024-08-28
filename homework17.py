# Глобальная переменная для отслеживания количества вызовов функций
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    # Приводим все элементы списка и искомую строку к нижнему регистру для сравнения
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches

# Выводим количество вызовов
print(calls)
