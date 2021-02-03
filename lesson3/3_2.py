def info(name, surname, year_of_birth, city_of_residence, email, phone_number):
    return f'имя:{name}, фамилия:{surname}, год_рождения:{year_of_birth}, ' \
           f'город_проживания:{city_of_residence}, email:{email}, телефон:{phone_number}'


a = input('введите имя: ')
b = input('введите фамилию: ')
c = input('введите год рождения: ')
d = input('введите город проживания: ')
f = input('введите email: ')
e = input('введите номер телефона: ')

print(info(name=a, surname=b, year_of_birth=c, city_of_residence=d,  email=f, phone_number=e))
