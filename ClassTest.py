class Person(object):
    def __init__(self, name, description):
        self.person_name = name
        self.desc = description

    def __str__(self):
        return "This person is called {} and says {}".format(self.person_name, self.desc)

person1 = Person("Simon", "Hey")
person2 = Person("Steffen", "hey")

print(person1)
print(person2)

this = "this is a string"

print(this[1:-1])