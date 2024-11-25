# Функция для генерации паролей
def generate_passwords():
    passwords = {}

    # Перебираем числа от 3 до 20
    for n in range(3, 21):
        pairs = []

        # Ищем все пары чисел от 1 до n-1
        for i in range(1, n):
            for j in range(i + 1, n):
                if i + j == n:
                    pairs.append(f"{i}+{j}")

        # Формируем пароль из найденных пар
        password = ''.join(pairs)
        passwords[n] = password

    return passwords


# Генерируем пароли
passwords = generate_passwords()

# Выводим результаты
for number, password in passwords.items():
    print(f"{number} - {password}")

