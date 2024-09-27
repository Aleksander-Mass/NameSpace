'''
Домашнее задание по уроку "Пространство имен"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новую функцию test_function
Создайте внутри test_function другую функцию - inner_function,
Эта функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
'''


# Создаем функцию test_function
def test_function():
    # Создаем функцию inner_function внутри test_function
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываем inner_function внутри test_function
    inner_function()


# Вызываем test_function
test_function()

# Пытаемся вызвать inner_function вне функции test_function
try:
    inner_function()  # Попробуем вызвать, но это вызовет ошибку
except NameError as e:
    print(f"Ошибка: {e}")

# 1. Внутри функции test_function создана другая функция inner_function, которая выводит сообщение.

# 2. Вызов функции inner_function происходит внутри функции test_function, и она корректно выводит сообщение.

# 3. Попытка вызвать inner_function вне функции test_function приведет к ошибке NameError,
#    так как эта функция находится в локальной области видимости функции test_function и недоступна снаружи.