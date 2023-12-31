from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
        

class Name(Field):
    ...
    

class Phone(Field):
    ...


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"\nPhone number {phone} to contact {self.name} is added successfully!"
        return f"\nThe phone number {phone} for {self.name} is already in adress book!"
    
    # def change_phone(self, old_phone, new_phone):
    #     for idx, p in enumerate(self.phones):
    #         if old_phone.value == p.value:
    #             self.phones[idx] = new_phone
    #             return f"old phone {old_phone} change to {new_phone}"
    #     return f"{old_phone} not present in phones of contact {self.name}"

    def delete_pone(self, phone_to_delete):
        for phone in self.phones:
            if phone.value == phone_to_delete.value:
                self.phones.remove(phone)
                return f'\nPhone number {phone.value} for {self.name} removed successfully!'
        return f"{phone_to_delete} is not in the phones list of the contact {self.name}"
    
        # phones_list = address_book.data[self.name]
        # phones_list.remove(self.phone)
        # address_book.data[self.name] = phones_list 
#     for name, phones in address_book.data.items():
#         if name.name == user_name:
#             for item in phones:
#                 if phone_number == item.phone:
#                     delete_record = Record (name, item)
#                     delete_record.delete_phone()
#                     print (f'\nPhone number {item.phone} for {name.name} removed successfully!')
#                     return main()
#                 else:
#                     print (f'Phone {phone_number} for {user_name} was not found!')
#                     return main

    
    def __str__(self) -> str:
        return f"{self.name} {', '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"\nContact {record} added successfully!"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
    
if __name__ == '__main__':

    # Bill +380(67)333-43-54
    name_1 = Name('Bill')
    print (name_1)
    phone_1 = Phone('+380(67)333-43-54')
    print (phone_1)
    record_1 = Record(name_1, phone_1)
    print (record_1)
    address_book = AddressBook()
    address_book.add_record(record_1)
    print (address_book)
