class Person:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.shopping_list = []

    def add_to_list(self, item):
        self.shopping_list.append(item)

    def remove_from_list(self, item):
        self.shopping_list.remove(item)

person = Person("Bob", 30)
person.add_to_list("Apples")