# The teacher has 20 copies of a document.
# There are 10 tables, and each table is occupied by two students.
# Each document belongs to one of the students.
# On the blackboard, the name of the teacher is written.


class Table:
    def __init__(self):
        self.position = None

    # set a readable number to use beside the non-readable index
    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num


class Blackboard:
    def __init__(self):
        self.content = None

    def set_content(self, teacher):
        self.content = teacher.name

    # Print a "fancy" blackboard
    def get_content(self):
        print("_____________________")
        print("|                   |")
        print("| Welcome to prog 2 |")
        print(f"|   {self.content}   |")
        print("|                   |")
        print("_____________________")


class Student:
    def __init__(self):
        self.name = None
        self.table = None

    def set_name(self, name):
        self.name = name

    # define the table, where the student sits
    def set_table(self, table):
        self.table = table

    def get_name(self):
        return self.name

    def get_table(self):
        return self.table


class Teacher:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Document:
    def __init__(self):
        self.owner = None
        self.num = None

    def set_owner(self, teacher):
        self.owner = teacher

    def set_student(self, student):
        self.student = student

    def get_student(self):
        return self.student

    def get_owner(self):
        return self.owner


def __main__():


    # New Teacher object, with name "Andreas Urben"
    te_andreas = Teacher("Andreas Urben")

    # Create empty documents list
    documents = list()

    # create 20 document objects and append to documents list created above
    for i in range(20):
        document = Document()

        # Set owner of the document, in this case it's the teacher
        document.set_owner(te_andreas)
        documents.append(document)

    # List the 20 documents and show document owner
    # for document in documents:
    #    print(f"{id(document)}: {document.get_owner().get_name()}")

    # define amount of tables
    table_amount = 10

    # Create empty list of tables
    tables = list()

    # Create 10 tables and append to list of tables
    for i in range(table_amount):
        table = Table()
        table.set_num(i)
        tables.append(table)

    #  Student names, which we assign to created student objects
    student_names = ["Emma", "Mia", "Sophia", "Hannah", "Lena", "Lina", "Emilia", "Marie", "Charlotte", "Clara", "Noah", "Liam", "Ben", "Paul", "Leon", "Jonas", "Felix", "Elias", "Maximilian", "David"]

    # Create empty student list
    students = list()

    # Iterate through student_names, create an object for each
    # set object name-attribute and append the objects to student list
    for name in student_names:
        student = Student()
        student.set_name(name)
        students.append(student)

    # Set student for each document by passing the student object as a parameter to the document student attribute
    for i in range(len(documents)):
        documents[i].set_student(students[i])

    # assign tables and students, iterate by using the length of the list (i.e. 20)
    # use integral division 2 to get two students per table
    for i in range(len(students)):
        students[i].set_table(tables[i // 2])

    # print out student name, document ID and table, where the student sits
    for document in documents:
        # {document.get_student().get_table().get_num()}
        print(f"{document.get_student().get_name()} works with document {id(document)} and sits at table {document.get_student().get_table().get_num()}")

    # New Blackboard Object
    blackboard = Blackboard()

    # Define content of blackboard by passing Teacher object
    blackboard.set_content(te_andreas)

    # Print blackboard content
    blackboard.get_content()


__main__()
