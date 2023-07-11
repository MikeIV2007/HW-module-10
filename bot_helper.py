import re
from rich import print
from rich.table import Table

from collections import UserDict


#Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів.
class Field:
    pass

#Клас Name, обов'язкове поле з ім'ям.
class Name(Field):
    def __init__(self, name) -> None:
        self.name = name


#Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


#Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
#Записи Record в AddressBook зберігаються як значення у словнику. Як ключі використовується значення Record.name.value.
class Record(Field):
    def __init__(self, name, phone):

        #Record зберігає об'єкт Name в окремому атрибуті
        self.name = name
        #Record зберігає список об'єктів Phone в окремому атрибуті.
        #self.phones = []
        self.phone = phone
        #self.phones.append(self.phone)

#AddressBook реалізує метод add_record, який додає Record у self.data.
class AddressBook(UserDict):
    def add_record(self, rec):
    #def add(self, name, phone_number):
        self.data[rec.name] = rec.phone

    def display_contacts(self):
        table = Table(title="\nALL CONTACTS IN DATABASE")
        table.add_column("Name", justify="left")
        table.add_column("Phone number", justify="center")

        if len(self.data) == 0:
            print ('\nAddress Book is empty!')
            return main()
        for name, phone_number in self.data.items():
            #print(f"{name.name}: {phone_number.phone}")
            table.add_row(name.name, phone_number.phone)
        print (table)
        return main()

address_book = AddressBook()
    

    # def add(self,record):

    #     record_name = record.name
    #     record_phone = record.phone
        
    #     print (f'\nNew contat {record_name.name} {record_phone.phone} added successfully!')
    #     #print (f'AB {record.name}, {record.phone}')
    #     self.data[record_name.name] = record_phone.phone

# USER_DATA_DICTIONARY = {}
# I = 1

def table_of_commands():

    table = Table(title="\nALL VALID COMMANDS:\n(All entered data must be devided by gap!)")
    table.add_column("COMMAND", justify="left")
    table.add_column("NAME", justify="left")
    table.add_column("PHONE NUMBER", justify="center")
    table.add_column("DESCRIPTION", justify="left")
    table.add_row('hello', '-', '-', 'Greeting')
    table.add_row('add', 'Any name ', 'Phone number in any format', 'Add new contact')
    table.add_row('change', 'Any name', 'Phone number in any format', 'Change phone number')
    table.add_row('phone', 'Any name', '-', 'Getting phone number')
    table.add_row('show all', '-', '-', 'Getting all database')
    table.add_row('good bye / close / exit', '-', '-', 'Exit')
    table.add_row('help', '-', '-', 'Printing table of commands') 

    return print (table)


def user_name_exists(func):
    def wrapper(user_name: str, phone_number: str):
        if user_name not in USER_DATA_DICTIONARY:
            print (f'\nContact {user_name} is not exist! Try other options!')
            main()
        else:
            func(user_name, phone_number)
    return wrapper


def hello():
    print('\nHow can I help you?')
    return main()


def exit_programm():

    print ('\nGood bye! Have a nice day!\n')
    exit()


def add(user_name, phone_number):
    # if user_name in address_book:
    #     print (f'\nContat {user_name} is already exist! Try other options!')
    #     main()
    # if phone_number == '':
    #     print ('There is no phone number')
    #     return main()
    name = Name(user_name)
    phone = Phone(phone_number)
    rec = Record(name, phone)

    for name, phone in address_book.data.items():
        if name.name == user_name:
            print (f'\nContat {name.name} is already exist! Try other options!')
            return main()
    if phone_number == '':
        print ('There is no phone number')
        return main()
    address_book.add_record(rec)
    print (f'\nNew contat {user_name} {phone_number} added successfully!')
    return main()
    # if user_name in USER_DATA_DICTIONARY:
    #     print (f'\nContat {user_name} is already exist! Try other options!')
    #     main()
    # if phone == '':
    #     print ('There is no phone number')
    #     return main
    # USER_DATA_DICTIONARY[user_name] = phone_number
    # print (f'\nNew contat {user_name} {phone_number} added successfully!')
    # save_data()
    # return main()


# @user_name_exists
# def change(user_name: str, phone_number:str):
#     USER_DATA_DICTIONARY[user_name] = phone_number
#     save_data()
#     print (f'\nPhone number {phone_number} for {user_name} changed successfully!')
#     return main()


# @user_name_exists
# def phone(user_name:str, phone_number: str):
#     phone_number = USER_DATA_DICTIONARY[user_name]
#     print (f'\nPhone number of {user_name} is: {phone_number}')
#     return main()


def show_all():
    address_book.display_contacts()
#     try:
#         with open('contacts_log.txt', 'r') as file:
#             list = file.readlines()

#         if list == []:
#             print ('\nDatabase is empty!')
#             return main()
        
#         else:
#             table = Table(title="\nALL CONTACTS IN DATABASE")
#             table.add_column("Name", justify="left")
#             table.add_column("Phone number", justify="center")

#             for item in list:
#                 item_split =item.split(':')
#                 table.add_row(item_split[0], item_split[1].replace('\n', ''))
#         print (table)
#         return main()
    
    # except FileNotFoundError:
    #     print ('\nDatabase is empty!')
    #     return main()
    

COMMAND_INPUT = {'hello': hello, 
                'add': add,
                'show all': show_all,
                'exit': exit_programm,
                'good bye': exit_programm, 
                'close': exit_programm,
                'help': table_of_commands} 
                #  'change': change, 
                #  'phone': phone,


def execute_command(command, user_name, phone_number):
    COMMAND_INPUT[command](user_name, phone_number)
    # if command == 'add':
       
    #     record.add()


def input_error(func):
    def wrapper(data:str):
        try:
            regex_command = r'^[a-zA-Z]+'
            match = re.search(regex_command, data)
            
            if match:
                command = (match.group()).lower()

            if command in COMMAND_INPUT:
                span = match.span()
                user_info = data[span[1]:].strip()
                return command, user_info
            
            else:
                print ('\nUnknown command! Try agayn!')
                return main()
                
        except(KeyError, ValueError, IndexError, TypeError, UnboundLocalError):
            print ('\nWrong input! Try again')
            return main()
    return wrapper


def check_phone_number(command, phone):
    if command == 'phone':
        return phone
    if 18>= len(phone) >= 10:
        for i in phone:
            if i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '(', ')', ' '):
                continue
            else:
                print (f'Phone number {phone} is not correct')
                return main()
            
        return phone
    else:
        print (f'Phone number {phone} is not valid! It must be in range from 10 to 18 characters! Try againe!')
        return main()


def get_user_name(command: str, user_info: str )-> tuple:

    regex_name = r'[a-zA-ZА-Яа-я]+'
    user_input_split = user_info.strip().split()
    name_list =[]
    for i in user_input_split:
        match_name = re.match(regex_name, i)
        if match_name:
            if len(match_name.group()) == len(i): # checking if there are no other symbols than letters
                name_list.append(i.capitalize())
                user_info = user_info[match_name.span()[1]:].strip()
                phone = user_info
            else:
                print ('\nName is not correct! Try again!')
                return main()

    if len(name_list)>=1:
        name = ' '.join(name_list)
        
    else:
        print ('\nName is not correct! Try again!')
        return main()
    
    return name, phone


@input_error
def identify_command_get_info(input: str):

    regex_command = r'^[a-zA-Z]+'
    match = re.search(regex_command, input)
    
    if match:
        command = (match.group()).lower()

        if command in COMMAND_INPUT:
            span = match.span()
            user_info = input[span[1]:].strip()
            return command, user_info
        
    else:
        print ('\nUnknown command! Try agayn!')
        return main()
          
        
def get_user_input():

    global I
    
    # if I == 1:
    #     table_of_commands()
    #     I += 1

    while True:
        user_input = (input(f'\nEnter command, please!\n\n>>>')).strip()

        if user_input.lower() == "hello":
            return COMMAND_INPUT[user_input]()
          
        if user_input.lower() == 'show all':
            return COMMAND_INPUT[user_input]()                  

        if user_input.lower() in  ('exit', 'close', 'good bye'):
            return COMMAND_INPUT[user_input]()
        
        if user_input.lower() == 'help':
            return COMMAND_INPUT[user_input](), main() 

        return user_input
    

# user_name = Name()
# user_phone = Phone()
# record = Record (user_name, user_phone)

def main():
    #load_data()
    user_input = get_user_input()
    command, user_info = identify_command_get_info(user_input )
    name, phone = get_user_name(command, user_info)
    phone = check_phone_number(command, phone)
    execute_command(command, name, phone)

    
if __name__ == "__main__":
    main()

#
# 
# ADD Bill +380(67)333-43-54
# ADD Bill Jonson +380(67)333-43-5
# +380(67)282-8-313
# CHange Mike Jonn +380(67)111-41-77
# PHONE Mike Jonn +380(67)111-41-77
# CHange Bill Jonson +380(67)111-41-77
# CHANGE Bill +380(67)454-12-12
# PHONE Bill
# phone Bill +380(67)333-43-54
# 12m3m4n
# 12me3m3m 123m3mm2
# ADD Jill Bonson +380(67)333-43-54
# PhOnE Jill Bonson +380(67)333-43-54
# ADD Jill +380(67)333-43-54
# change Jill +380(67)222-33-55
# Иванов Иван Иванович +380(67)222-33-55
# change Иванов Иван Иванович +380(67)999-1-777
# phone Иванов Иван Иванович 
# dfsadfads asdgfas ref asdf     TypeError
# Jgfdksaflf Sdfjldsf; Asdfk;;lsdff Jldsf;sf';; sdff ; jldsf;sF';;
# add mike 123123-12-3