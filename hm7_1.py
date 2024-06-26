from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
   pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit string.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            date_format = "%d.%m.%Y"
            datetime.strptime(value, date_format)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthdays(self, birthday):
        self.birthday = Birthday(birthday)

    def get_birthday(self):
        return self.birthday

    def add_phone(self,  phone):
        #self.phones.append(Name(name))
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(phone)
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self,  old_phone, new_phone):
        print(old_phone, new_phone)
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                print(p.value)
                

        

    def find_phone(self, phone):
        for p in self.phones:
            if  str(p) == phone:
               
                print(p)

                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"
    
    def birthdays(args, book):
        return book.get_upcoming_birthdays()



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found.")

    def find_record(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("Contact not found.")
        
    def get_upcoming_birthdays(self):
            today = datetime.now().date()
            next_week = today + timedelta(days=7)
            upcoming_birthdays = []
            for record in self.data.values():
                if record.birthday:
                    birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                    if today <= birthday_date < next_week:
                        upcoming_birthdays.append(record.name.value)
            return upcoming_birthdays
    
    def add_birthday(self, args, book):
        self.name, self.birthday = args
        self.record = book.find_record(self.name)
        record.add_birthdays(self.birthday)
        return f"Birthday added for {self.name}."
    
    def show_birthday(args, book):
        name, *_ = args
        record = book.find_record(name)
        if record.birthday:
            return f"{name}'s birthday: {record.birthday.value}"
        else:
            return f"No birthday found for {name}."
        
if __name__ == "__main__":
    book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        
        user_input = input("Enter a command: ")
        command, *args = user_input.strip().split(" ")

        

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            name, phone = args
            record=Record(name)
            record.add_phone(phone)
            book.add_record(record)
            print("User added!")
            

        elif command == "change":
            name, old_nomber, new_nomber = args
            record=book.find_record(name)
            record.edit_phone(old_nomber, new_nomber)
            print(record)

        elif command == "phone":
            name, = args
            record=book.find_record(name)
            print(record.phones)


        elif command == "add-birthday":
            name,birthday=args
            record=book.find_record(name)
            record.add_birthdays(birthday)
            print(record)

        elif command == "show-birthday":
            name,=args
            record=book.find_record(name)
            #a=record.show_birthday(args, book)
            print(record.birthday)

        elif command == "birthdays":
            print(book.get_upcoming_birthdays)

        else:
            print("Invalid command.")

        for key, value in book.items():
            print("{0}:{1}".format(key,value))