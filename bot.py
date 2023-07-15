import re
from rich import print
from rich.table import Table
from ab_classes import AddressBook, Name, Phone, Record

address_book = AddressBook()

def table_of_commands():

    table = Table(title='\nALL VALID COMMANDS:\n(All entered data must be devided by gap!)')
    table.add_column('COMMAND', justify='left')
    table.add_column('NAME', justify='left')
    table.add_column('PHONE NUMBER', justify='center')
    table.add_column('DESCRIPTION', justify='left')
    table.add_row('hello', '-', '-', 'Greeting')
    table.add_row('add', 'Any name ', 'Phone number in any format', 'Add new contact')
    table.add_row('append', 'Existing name', 'Additional phone number', 'Append phone number') 
    table.add_row('delete', 'Existing name', 'Phone to delete', 'Delete phone number')
    table.add_row('phone', 'Existing name', '-', 'Getting phone number')
    table.add_row('show all', '-', '-', 'Getting all database')
    table.add_row('good bye / close / exit', '-', '-', 'Exit')
    table.add_row('help', '-', '-', 'Printing table of commands')

    return print (table)


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError as e:
            return e
    return wrapper


@input_error
def add_command(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))

    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    return address_book.add_record(rec)


def change_command(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f'No contact {name} in address book'


def exit_command(*args):
    return '\nGood bye! Have a nice day!\n'


def unknown_command(*args):
    pass


def show_all_command(*args):

    table = Table(title='\nALL CONTACTS IN DATABASE')
    table.add_column('Name', justify='left')
    table.add_column("Phone number", justify="left")

    if len(address_book.data) == 0:
        return '\nAddress Book is empty!'
    
    for name, record in address_book.data.items():
        phones_str = ''
        user_name = record.name
        user_phones_list = record.phones
        for item in user_phones_list:
            phones_str += item.value + ', '

        table.add_row(user_name.value, phones_str.strip())
    return table

COMMANDS = {
    add_command: ('add', 'append'),
    change_command: ('change', 'зміни'),
    exit_command: ('good bye', 'close', 'exit'),
    show_all_command: ('show all', )
}


def parser(text:str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                # print(cmd)
                data = text[len(kwd):].strip().split()
                # print(data)
                return cmd, data 
    return unknown_command, []


def main():

    table_of_commands()

    while True:
        user_input = (input(f'\nEnter command, please!\n\n>>>')).strip()
        
        cmd, data = parser(user_input)
        
        result = cmd(*data)
        
        print(result)
        
        if cmd == exit_command:
            break

if __name__ == "__main__":
    main()

# 
# ADD Bill +380(67)333-43-54
# Append Bill +380(67)333-11-11
# phone Bill
# DeLete Bill +380(67)333-43-54
# ADD Bill Jonson +380(67)333-43-5
# Append Bill Jonson +380(67)333-99-88
# PhoNE Bill Jonson
# DeleTe Bill Jonson +380(67)333-43-5
# +380(67)282-8-313
# CHange Mike Jonn +380(67)111-41-77
# delete Mike Jonn +380(67)111-41-77
# PHONE Mike Jonn +380(67)111-41-77
# CHange Bill Jonson +380(67)111-41-77
# PHONE Bill
# phone Bill +380(67)333-43-54
# 12m3m4n
# 12me3m3m 123m3mm2
# ADD Jill Bonson +380(67)333-43-54
# PhOnE Jill Bonson +380(67)333-43-54
# ADD Jill +380(67)333-43-54
# append Jill +380(67)222-44-55
# Иванов Иван Иванович +380(67)222-33-55
# append Иванов Иван Иванович +380(67)999-1-777
# phone Иванов Иван Иванович 
# delete Иванов Иван Иванович +380(67)222-33-55
# dfsadfads asdgfas ref asdf     TypeError
# Jgfdksaflf Sdfjldsf; Asdfk;;lsdff Jldsf;sf';; sdff ; jldsf;sF';;
# add mike 123123-12-3
# delete mike 123123-12-3
# phone mike 123123-12-3