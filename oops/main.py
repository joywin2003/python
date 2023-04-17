# Created a class to form a college application for the admission of new students
class CollegeApplication:
    application_type = "college admission"

    # initialises the attributes
    def __init__(self):
        self.college_name = "SJEC"
        self.college_adress = "Vamanjoor"

    # prints the details of the student
    def create_application(self):
        print(f"Name = {self.name}\n"
              f"Age = {self.age}\n"
              f"DOB = {self.dob}\n"
              f"Course = {self.course}\n"
              f"Address = {self.address}")

    # Asks the details of the student
    def ask_information(self):
        print(self.application_type)
        print(f"Welcome to {self.college_name},{self.college_adress}")
        self.name = input("Enter your full name: ")
        self.age = input("Enter your age: ")
        self.dob = input("Enter your date of birth: ")
        #self.course = input("Enter the course you wanna perceive")
        self.address = input("Enter your address: ")
        self.create_application()


# main program
your_application = CollegeApplication()
her_application = CollegeApplication()
your_application.course = "CSE"
CollegeApplication.application_type = "jobless"

# your_application.ask_information()
# her_application.course = "ECE"
her_application.ask_information()


