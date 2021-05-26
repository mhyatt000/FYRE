import os
import csv
from FYRE.obj import Student
from FYRE import stat
import yaml

students = []

def get():
    path = input('input .csv path or "n"')
    if path == 'n':
        path = '/Users/matthewhyatt/file-storage/loyola/s2/FYRE/input.csv'
    with open(path, mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        students.clear()
        for line in reader:
            students.append(Student(*line))

def all(mode):
    'all students'
    if mode == 'all':
        for student in students:
            student.show()
    if mode == 'attr':
        attr = input('which attribute? ')
        for student in students:
            student.show_attr(attr)

def query(students_in):
    students_q = []

    ask = input('add criteria? (y/n): ').lower()

    if ask == 'y':
        criterion = input('contains what? ').lower()
        for student in students_in:
            if student.contains(criterion):
                students_q.append(student)
        query(students_q)
    else:
        students_q = students_in
        print()
        for student in students_q:
            student.show()

def set_attrs(path):
    for student in students:
        print(yaml.dump(student, default_flow_style=False))
        #student.show_all()
        ask = input('set attribute? (y/n/break) ').lower()
        if ask == 'y':
            a = input('attribute: ').lower()
            value = input('value: ')
            student.a = value
            student.show_attr(a)
        if ask == 'break':
            break

    yaml_save(path, students)

def yaml_load(path):
    with open(path, 'r') as file:
        data = yaml.full_load(file)
        student = []
        for item in data:
            students.append(item)

def yaml_save(path, data):
    with open(path, 'w') as file:
        yaml.dump(data, file, indent=4, sort_keys=False)

def main():
    path = '/Users/matthewhyatt/fyre.yaml'

    while(True):
        arg = input("arg: ").lower()
        print()

        if arg == 'exit':
            break

        if arg == 'get':
            get()

        if arg == 'all':
            all('all')

        if arg == 'query':
            query(students)

        if arg == 'attr':
            all('attr')

        if arg == 'avg':
            a = input('attribute: ').lower()
            stat.avg_rating_attr(students, a)

        if arg == 'set':
            print('cannot currently set data')
            #set_attrs(path)

        if arg == 'save':
            yaml_save(path, students)

        if arg == 'load':
            try:
                students.clear()
                yaml_load(path)
                print('loaded yaml')
            except:
                pass

        if arg == 'len':
            print(len(students))



if __name__ == '__main__':
    main()
