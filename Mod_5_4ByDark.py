import re

contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return str(e)
        except ValueError as e:
            return str(e)
        except IndexError as e:
            return str(e)
    return inner

def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

@input_error
def add_contact(args):
    if len(args) < 2:
        raise ValueError("Будь ласка, введіть ім'я та телефон.")
    name, phone = args
    if name in contacts:
        raise KeyError("Це ім'я вже існує в телефонній книзі.")
    if not re.match(r"^\+\d{3}\s?\d{2}\s?\d{7}$", phone):
        raise ValueError("Номер телефону в неправильному форматі.")
    contacts[name] = phone
    return "Контакт додано."

@input_error
def change_contact(args):
    if len(args) < 2:
        raise ValueError("Необхідно вказати ім'я та новий номер телефону.")
    name, phone = args
    if name not in contacts:
        raise KeyError("Такого імені немає в телефонній книзі.")
    if not re.match(r"^\+\d{3}\s?\d{2}\s?\d{7}$", phone):
        raise ValueError("Неправильний формат номера телефону.")
    contacts[name] = phone
    return "Номер телефону оновлено."

@input_error
def show_phone(args):
    if len(args) == 0:
        raise IndexError("Не вказано ім'я для пошуку.")
    name = args[0]
    if name not in contacts:
        raise KeyError("Такого контакту не знайдено.")
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args):
    if not contacts:
        return "Ваша телефонна книга порожня."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def handle_command(command, args):
    if command == "add":
        return add_contact(args)
    elif command == "change":
        return change_contact(args)
    elif command == "phone":
        return show_phone(args)
    elif command == "all":
        return show_all(args)
    elif command in ["close", "exit"]:
        print("До побачення!")
        exit()
    else:
        return "Невідома команда."

def main():
    print("Ласкаво просимо до супер АІ Стебл Фьюжин бот-помічник!)")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)
        response = handle_command(command, args)
        print(response)

if __name__ == "__main__":
    main()
