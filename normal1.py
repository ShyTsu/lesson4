# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки,
#  имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
#  допускается нижнее подчеркивание
# и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net),
#  te_4_st@test.com - верно указан.


import re


name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
email = input('Введите Ваш e-mail: ')

pattern_name = '[А-Я]{1}[а-я]+'
pattern_surname = '[А-Я]{1}[а-я]+'
pattern_email = '[a-z_0-9]+@[a-z0-9]+\.(ru|org|com)'


if re.match(pattern_email, email) and re.match(pattern_name, name) and re.match(pattern_surname, surname):
    print('Добро пожаловать,', name, surname)
else:
    print('Вы ввели неверные данные!')

