import shelve

def init_data():
    harry = {'name': 'Harry', 'last_name': 'Potter', 'stream': 'ECE'}
    ron = {'name': 'Ron', 'last_name': 'Weasley', 'stream': 'CSE'}
    harmoine = {'name': 'Harmoine', 'last_name': 'Grenger', 'stream': 'ECE'}
    return harry,ron,harmoine

def store_data(harry,ron,harmoine):
    db = shelve.open('../Database/dict_student-shelve')
    db['harry'] = harry
    db['ron'] = ron
    db['harmoine'] = harmoine
    db.close()

def load_data():
    db = shelve.open('../Database/dict_student-shelve')
    print(db['harry'])
    db.close()

if __name__ == '__main__':
    harry,ron,harmoine= init_data()
    store_data(harry,ron,harmoine)
    load_data()