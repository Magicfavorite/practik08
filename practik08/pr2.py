"""Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
количества на экран."""

user_str = input("Введите строку у которой нам будет необходимо почитать кол-во букв  кол-во цифр")
digital_count = 0
letter_count = 0
for i in user_str:

    if i.isdigit():
        digital_count += 1
    elif i.isalpha():
        letter_count += 1
    
print(f"количество цифр в вашем предложении : {digital_count}")
print(f"количество букв в вашем предложении : {letter_count}")


