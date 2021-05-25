import os
import csv
from FYRE.obj import Student

path = '/Users/matthewhyatt/file-storage/loyola/s2/FYRE/input.csv'
students = []

def get():
    with open(path, mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        line_count = 0

        for row in reader:
            if reader.line_num != 1: #the first line is the headers
                students.append(Student(*row))

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

def main():
    get()

    while(True):
        arg = input("arg: ").lower()

        if arg == 'exit':
            break

        if arg == 'all':
            all('all')

        if arg == 'query':
            query(students)

        if arg == 'attr':
            all('attr')


if __name__ == '__main__':
    main()
