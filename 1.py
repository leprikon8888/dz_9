"""Task 1
Необхідно підготувати звіт про витрати членів родини на новорічні свята.
Дані по витратам наведено у файлі hw_10_test.txt у форматі:
Номер за переліком Прізвище та ім'я (або ім'я) Сума Категорія товару
Звіт повинен включати наступне:
1. Яка загальна сума витрат по кожній категорії товарів?
2. Скільки грошей витратив кожен член родини?
3. Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини?"""


def process(line):   #создал функцию, чтобы соотвкетствовать принципу dry
    _, *name, money, category = line.split()
    money = float(money.replace('$', ''))
    name = ' '.join(name)
    return name, money, category


def category_expenses(path_too_file: str):
    categories = {}
    with open(path_too_file, 'r', encoding='utf-8') as z:
        for line in z:
            name, money, category = process(line)
            if category in categories:
                categories[category] += money
            else:
                categories[category] = money
    return categories


def unit_expenses(path_too_file: str):
    unit = {}
    with open(path_too_file, 'r', encoding='utf-8') as z:
        for line in z:
            name, money, category = process(line)
            if name in unit:
                unit[name] += money
            else:
                unit[name] = money
    return unit


def shopping_counter(user: str, path_too_file: str):
    x = 0
    user = user.title()
    with open(path_too_file, 'r', encoding='utf-8') as z:
        for line in z:
            name, money, category = process(line)
            if name == user:
                x += 1
    return x


path_too_file = 'hw_10_test.txt'

x = category_expenses(path_too_file)
for i, y in x.items():
    print(f'категория - {i}, траты по этой категории - {y:.2f}у.е.')

print(70 * '=')

y = unit_expenses(path_too_file)
for i, n in y.items():
    print(f'член семьи по имени {i} потратил(а) {n:.2f}у.е.')

print(70 * '=')

z = list(y.keys())
user = input(f'Введите имя члена семьи, доступные имена: {z} - ')
user_shopping_count = shopping_counter(user, path_too_file)
print(f'{user} совершил {user_shopping_count} покупок(ки).')
