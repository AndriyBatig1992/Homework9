# ЧАТ_БОТ

def input_error(function):
    def wraper(*args, **kwargs):
       try:
           return function(*args, **kwargs)
       except KeyError as k:
           print(f"При вводі сталася помилка: {k}")
       except ValueError as e:
           print(f"При вводі сталася помилка: {e}")
       except IndexError as i:
           print(f"При вводі сталася помилка: {i}")
    return wraper


def say_hi():
    """Функція привітання"""
    print('How can I help you?')

def good_by():
    """Функція до побачення"""
    print('Good bye!')

def show_all_contact(contacts: dict)-> None:
    """Функція показує всі контакти"""
    message = 'Список контактів порожній. Для додавання контакту використайте функцію "add"'
    print('\n'.join([f"{name.capitalize()}: {phone}" for name, phone in contacts.items()]) if len(contacts)>0 else message)


@input_error
def add_contact(contacts: dict, data: str)-> None:
    """Функція додає новий контакт до наявних"""
    arg=data.split()
    if len(arg) != 2:
        raise ValueError("Введіть будь-ласка тільки одне ім'я і телефон після  команди 'add'")
    name, phone = arg
    if name not in contacts:
        contacts[name] = [phone]
        print(f'Додано контакт {name.capitalize()}, телефон якого {phone}')
    else:
        print(f'Контакт з іменем {name.capitalize()}, телефон якого {contacts[name][0]}, вже є')



@input_error
def change_contact(contacts: dict, data: str)-> None:
    """Функція змінює телефон наявного контакту"""
    arg = data.split()
    if len(arg) != 2:
        raise ValueError("Введіть будь-ласка тільки одне ім'я і його новий телефон після команди 'change'")
    name, new_phone = arg
    if  name not in contacts:
        raise IndexError(f"Немає що змінювати. Ви не додали користувача {name.capitalize()} до списку!!!'")
    else:
        contacts[name] = [new_phone]
        print(f'У {name.capitalize()} телефон змінився на {new_phone}')


@input_error
def show_phone(contacts: dict, name: str)-> None:
    """Функція показує телефон наявного контакту"""
    if len(name.split())!= 1:
        raise ValueError("Введіть тільки ім'я")
    if name in contacts:
        print(contacts[name])
    else:
        a = f"Введіть ім'я користувача, який є у списку контактів." \
        f" Бо користувача {name.capitalize()} немає у контактах"
        raise KeyError(a)

def main():
    """Головна функція"""
    contacts = {}
    while True:
         input_user = input('Waiting for command...').lower()

         if input_user == 'hello':
            say_hi()
         elif input_user.startswith('add'):
            _, data = input_user.split(' ', 1)
            add_contact(contacts, data)
         elif input_user.startswith('change'):
            _, data = input_user.split(' ', 1)
            change_contact(contacts, data)
         elif input_user.startswith('phone'):
            _, name = input_user.split(' ', 1)
            show_phone(contacts, name)
         elif input_user.startswith('show all'):
            show_all_contact(contacts)
         elif input_user in ['good bye', 'close', 'exit']:
            good_by()
            break
         else:
             print('Unknown command, please try again.')

if __name__=="__main__":
    main()
