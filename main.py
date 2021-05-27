import os
import csv
from FYRE.obj import Student
from FYRE import stat
import yaml

students = []
path_csv = '/Users/matthewhyatt/file-storage/loyola/s2/FYRE/input.csv'
path_yaml = '/Users/matthewhyatt/file-storage/loyola/s2/FYRE/fyre.yaml'

def get():
    with open(path_csv, mode='r') as file:
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

def set_attrs():
    for student in students:
        print(yaml.dump(student, default_flow_style=False))
        #student.show_all()
        ask = input('set attribute? (y/n/break) ').lower()
        if ask == 'y':
            a = input('attribute: ').lower()
            value = input('value: ')
            setattr(student, a, value)
            student.show_attr(a)
        if ask == 'break':
            break

    yaml_save(path_yaml, students)

def yaml_load(path):
    with open(path, 'r') as file:
        data = yaml.full_load(file)
        student = []
        for item in data:
            students.append(item)

def yaml_save(path, data):
    with open(path, 'w') as file:
        yaml.dump(data, file, indent=4, sort_keys=False)

def clean():
    attr = input('which attribute to clean? ').lower()
    for student in students:
        student.show_attr(attr)
        ask = input('set? (y/n/break) ').lower()
        if ask == 'y':
            val = input('input: ').lower()
            setattr(student, attr, val)
            student.show_attr(attr)
        if ask == 'break':
            break
    yaml_save(path_yaml, students)

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
            set_attrs()

        if arg == 'save':
            yaml_save(path_yaml, students)

        if arg == 'load':
            try:
                students.clear()
                yaml_load(path_yaml)
                print('loaded yaml')
            except:
                pass

        if arg == 'len':
            print(len(students))

        if arg == 'clean':
            clean()
        print()

if __name__ == '__main__':
    main()
