# ЧАТ_БОТ

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Give me name and phone please'
        except KeyError:
            return 'Enter correct user name. Contact not found'
        except ValueError:
            return 'Wrong name to change. Try again!'
    return wrapper

def good_by(*args):
   return 'Good bye!'

def say_hi(*args):
    return 'How can I help you?'

ADRESSBOOK={}

def showall_contacts(*args):
    if ADRESSBOOK:
        return "\n".join(f"{name}: {phone}" for name, phone in ADRESSBOOK.items())
    else:
        return "No contacts found."

@input_error
def add_contact(data):
    name=data[0].title()
    phone=data[1]
    ADRESSBOOK[name] = phone
    return f"Contact '{name}' with phone '{phone}' has been added.\n {ADRESSBOOK}"

@input_error
def change_contact(data):
    name, new_phone = data[0].title(), data[1]
    if name in ADRESSBOOK:
        ADRESSBOOK[name] = new_phone
        return f"Phone number for contact '{name}' has been updated to '{new_phone}'.\n {ADRESSBOOK}"
    else:
        raise ValueError


@input_error
def get_phone(data):
    name = data[0].title()
    return f"Phone number for contact '{name}': {ADRESSBOOK[name]}"


def handler_parse(rawstr):
    elements = rawstr.split()
    command = elements[0].lower()
    if command in COMANDS:
        return command, elements[1:]
    for key, value in COMANDS.items():
        if any(arg.startswith(command) for arg in value):
            return key, elements[1:]
    return None, None

COMANDS = {add_contact: ['add'],
          change_contact: ['change'],
          get_phone: ['phone'],
          showall_contacts: ['show all'],
          good_by: ['good bye', 'close', 'exit'],
          say_hi: ['hello']}


def main():
    while True:
        user_input = input('Waiting for command...')
        fun = None
        try:
            fun, data = handler_parse(user_input)
            res=fun(data)
            print(res)
        except TypeError:
            print('Wrong comand. Try again!')
        if fun == good_by:
             break



if __name__ == "__main__":
    main()

