# Задача «Сдача всем».
# Описание: Кроме ягод в магазине продаётся множество других товаров, 
# которые продаются на развес. Давайте автоматизируем расчёт сдачи и для них!
# Формат ввода
# Три натуральных числа:
# цена товара;
# вес товара;
# количество денег у покупателя.
# Формат вывода
# Одно целое число — сдача, которую требуется отдать покупателю
price = int(input("Введите цену товара: "))
weight = int(input("Введите вес товара: "))
money = int(input("Введите количество денег у покупателя: "))
change = money - price * weight
print(f"Сдача составит {change} руб.")