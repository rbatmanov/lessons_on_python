def print_digit(num):
    print(num, end='')  # Печатает цифру без переноса строки


# Номер, который мы хотим вывести
phone_number = "88005553535"


# Вызов функции 11 раз для каждой цифры номера
for digit in phone_number:
    print_digit(digit)
