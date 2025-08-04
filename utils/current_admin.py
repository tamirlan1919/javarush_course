
def is_admin():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if login == 'admin' and password == '12345':
        print('Cool')
    else:
        print('Not cool')