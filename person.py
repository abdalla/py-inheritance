class Person():
    def __init__(self, first_name, last_name, age):
        print("person construct called");
        self.firstName = first_name;
        self.lastName = last_name;
        self.age = age;

    def show_info(self):
        print("First Name: "+ self.firstName);
        print("Last Name: "+ self.lastName);