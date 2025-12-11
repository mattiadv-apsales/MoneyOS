class Person:
    _persons = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

        new_person = {
            "name": name,
            "surname": surname,
            "age": age
        }

        Person._persons.append(new_person)

    def __str__(self):
        return f"Ciao io sono {self.name} {self.surname} e ho {self.age} anni"
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __add__(self, other):
        return f"{self.name} {other.name}"
    
    @staticmethod
    def search_by_name(name):
        return [p for p in Person._persons if p["name"] == name]

    @staticmethod
    def view_persons():
        for p in Person._persons:
            print(p)

Mattia = Person("Mattia", "De Vincentis", 20)
Federica = Person("Federica", "Giannotti", 20)
Simone = Person("Simone", "Fortunato", 20)
Serena = Person("Serena", "aaaa", 20)

print(Mattia + Federica)
print(Mattia == Federica)

Person.view_persons()
results = Person.search_by_name("Mattia")

for r in results:
    for k, v in r.items():
        print(v)