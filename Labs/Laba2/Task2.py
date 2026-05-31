import random


# 1. Создание функции validate_password(password)
def validate_password(password):
    criteria = {
        'length': len(password) >= 8,
        'has_letter': False,
        'has_digit': False,
        'has_special': False,
        'has_uppercase': False,
        'has_lowercase': False
    }

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?`"

    for char in password:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            criteria['has_letter'] = True
        if '0' <= char <= '9':
            criteria['has_digit'] = True
        if char in special_chars:
            criteria['has_special'] = True
        if 'A' <= char <= 'Z':
            criteria['has_uppercase'] = True
        if 'a' <= char <= 'z':
            criteria['has_lowercase'] = True

    is_valid = all(criteria.values())
    return is_valid, criteria


# 2. Реализация запроса пароля, проверки и повторного ввода при невалидности
def request_and_validate():
    while True:
        user_password = input("Введите пароль: ")
        is_valid, details = validate_password(user_password)

        if is_valid:
            print("Пароль валиден!")
            break
        else:
            print("Пароль невалиден. Детали:")
            for key, passed in details.items():
                print(f" {key}: {passed}")
            print("Попробуйте еще раз.\n")


# 3. Генератор пароля
def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_special=True, exclude_ambiguous=True):
    length = max(8, length)

    if exclude_ambiguous:
        pool_upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
        pool_lower = "abcdefghijkmnopqrstuvwxyz"
        pool_digits = "23456789"
    else:
        pool_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pool_lower = "abcdefghijklmnopqrstuvwxyz"
        pool_digits = "0123456789"

    pool_special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    available_chars = ""
    password = []

    if use_uppercase:
        available_chars += pool_upper
        password.append(random.choice(pool_upper))
    if use_lowercase:
        available_chars += pool_lower
        password.append(random.choice(pool_lower))
    if use_digits:
        available_chars += pool_digits
        password.append(random.choice(pool_digits))
    if use_special:
        available_chars += pool_special
        password.append(random.choice(pool_special))

    while len(password) < length:
        password.append(random.choice(available_chars))

    random.shuffle(password)
    return "".join(password)




if __name__ == "__main__":
    print("--- Генератор паролей ---")
    print("Пароль (10 символов):", generate_password(length=10))
    print("Пароль (15 символов):", generate_password(length=15))
    print("Пароль (без неоднозначных символов):", generate_password(length=12, exclude_ambiguous=True))

    print("\n--- Проверка пароля ---")
    request_and_validate()