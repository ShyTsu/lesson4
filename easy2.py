# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


a = ['Яблоко', 'Имбу', 'Папайя', 'Капулин', 'Корлан', 'Алыча']
b = ['Папайя', 'Бакупари', 'Алыча', 'Ананас', 'Сантол', 'Лимон', 'Корлан']
z = list(set(a) & set(b))

print(z)
