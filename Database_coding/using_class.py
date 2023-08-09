import shelve


class Student:
    def __init__(self, fname, lname, stream_name):
        self.first_name = fname
        self.last_name = lname
        self.stream = stream_name

    def __str__(self):
        return f'Name :{self.first_name}\nStream:{self.stream}\n\n'


def store_data(student_in):
    # db = shelve.open('../Database/class_student_shelve')
    db = shelve.open('Database/class_student_shelve')
    db[student_in.first_name] = student_in
    db.close()


def display_data():
    # db = shelve.open('../Database/class_student_shelve')
    db = shelve.open('Database/class_student_shelve')
    for key in db:
        print(db[key])


if __name__ == '__main__':
    harry = Student(fname='Harry', lname='Potter', stream_name='ECE')
    ron = Student(fname='Ron', lname='Weasley', stream_name='CSE')
    harmoine = Student(fname='Harmoine', lname='Grenger', stream_name='ISE')
    lst_students = [harry, ron, harmoine]
    for student in lst_students:
        store_data(student)
    display_data()
