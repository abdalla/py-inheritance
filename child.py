from person import Person;

class Child(Person):
    def __init__(self, first_name, last_name, age, nr_of_toys):
        print("child construct called");
        Person.__init__(self, first_name, last_name, age);
        self.nrOfToys = nr_of_toys;

    # OVERRIDING
    def show_info(self):
        print("First Name: "+ self.firstName);
        print("Last Name: "+ self.lastName);
        print("nr of toys: "+ str(self.nrOfToys));