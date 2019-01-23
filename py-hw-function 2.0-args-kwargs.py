class Contact:
    def __init__(self, name, surname, telephone, favorite_contact=False, **kwargs):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.kwargs = kwargs
        self.favorite_contact = favorite_contact

    def __str__(self):
        info = []
        for key, value in self.kwargs.items():
            info.append(f"\t {key}: {value}\n")
        info = " ".join(info)
        if self.favorite_contact != False:
            favorite_contact = f"В избранных: {self.favorite_contact}"
        else:
            favorite_contact = "В избранных: отсутствует"
        result = "Имя: " + self.name + "\n" + "Фамилия: " + self.surname + "\n" \
                 + "Телефон: " + self.telephone + "\n" + favorite_contact + \
                 "\n" + "Дополнительная информация: \n" + info
        return result


class PhoneBook:
    def __init__(self, name):
        self.name = name
        contact = list()
        self.contact = contact

    def __str__(self):
        return self.name

    def add_contact(self, user):
        self.contact.append(user)
        return self.contact

    def out_contact(self):
        for i in self.contact:
            print(i)

    def delete_contact(self, tel):
        for i in self.contact:
            if i.telephone == tel:
                self.contact.remove(i)
                print(f"Контакт с номером {tel} удален")

    def all_favorite_tel(self):
        print("Избранные контакты: ")
        for i in self.contact:
            if i.favorite_contact != False:
                print(i.favorite_contact)

    def search_by_name_surname(self, name_contact, surname_contact):
        for i in self.contact:
            if i.name == name_contact and i.surname == surname_contact:
                print(i)


user_1 = Contact("Jhon", "Smith", "+71234567809", telegram="@jhony", email="jhony@smith.com")
user_2 = Contact("Kamil", "Mamedov", "+79109929603", telegram="@kamiweb", email="kami2492@gmail.com")
print(user_1)
print(user_2)
book = PhoneBook("Friends")
book.add_contact(user_1)
book.add_contact(user_2)
book.out_contact()
book.delete_contact("+71234567809")
book.out_contact()
book.all_favorite_tel()
book.search_by_name_surname("Kamil", "Mamedov")
print(book)