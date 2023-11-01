"""Task 1
Необхідно підготувати звіт про витрати членів родини на новорічні свята.
Дані по витратам наведено у файлі hw_10_test.txt у форматі:
Номер за переліком Прізвище та ім'я (або ім'я) Сума Категорія товару
Звіт повинен включати наступне:
1. Яка загальна сума витрат по кожній категорії товарів?
2. Скільки грошей витратив кожен член родини?
3. Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини?"""

path_too_file = 'hw_10_test.txt'


def pars(path_too_file: str):
    """
    Функция принимает адрес текстового файла и на выходе даст список списков строк в файле в заданном формате ,а именно:
    имя, сумма трат, категория трат
    """
    with open(path_too_file, 'r', encoding='utf-8') as z:
        res = []
        a = []
        for line in z:
            _, *name, money, category = line.split()
            name = ' '.join(name)
            money = float(money.replace('$', ''))
            a.append(name)
            a.append(money)
            a.append(category)
            res.append(a)
            a = []
    return res


# траты по каждой категории
def category_expenses(path_too_file: str):
    """
    функция для подсчета трат по каждой категории товаров
    """
    a = pars(path_too_file)
    categories = {}
    for i in a:
        name, money, category = i
        if category in categories:
            categories[category] += money
        else:
            categories[category] = money
    return categories


# траты каждого человека
def unit_expenses(path_too_file: str):
    unit = {}
    a = pars(path_too_file)
    for el in a:
        name, money, category = el
        if name in unit:
            unit[name] += money
        else:
            unit[name] = money

    return unit


def shopping_counter(user: str):
    x = 0
    a = pars(path_too_file)
    user = user.title()
    for el in a:
        name, money, category = el
        if name == user:
            x += 1

    return f'член семьи по имени {user} совершила {x} покупки(ок) на сумму {unit_expenses(path_too_file)[user]:.2f}у.е.'


x = category_expenses(path_too_file)
for i, y in x.items():
    print(f'категория - {i}, траты по этой категории - {y:.2f}у.е.')

print(70 * '=')

y = unit_expenses(path_too_file)
for i, n in y.items():
    print(f'член семьи по имени {i} потратил {n:.2f}у.е.')

print(70 * '=')

z = list(y.keys())
user = input(f'введи имя члена семьи, доступные имена: {z} - ')

print(shopping_counter(user))
