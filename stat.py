from FYRE import obj

def avg_rating_notes(list: list):
    sum1 = 0
    count1 = 0

    sum2 = 0
    count2 = 0

    for student in list:
        if student.note_style == "Typed":
           sum1 += int(student.rating)
           count1 +=1
        else:
            sum2 += int(student.rating)
            count2 += 1
    print(count1 + count2)
    dictionary = {"Typed": float(sum1) / count1, "Handwritten": float(sum2) / count2}
    print(dictionary)

'this data could be converted to Handwritten: true, Handwritten: false'
'''
    types of attributes
        list
        binary
        string
'''

def avg_rating_val(students: list, a, val):
    sum = 0
    count = 0

    for student in students:
        if getattr(student, a) == val:
            'the ratings are stored as strings rn'
            sum += int(student.rating)
            count += 1
    print(f'average rating for {a} == {val}: {float(sum) / count}')

def avg_rating_attr(students: list, a):

    'boolean'
    if isinstance(getattr(students[0], a), bool):
        avg_rating_val(students, a, True)
        avg_rating_val(students, a, False)

    'string'
    if isinstance(getattr(students[0], a), str):
        uniquevals = set({})
        for student in students:
            uniquevals.add(getattr(student, a))

        for s_val in uniquevals:
            avg_rating_val(students, a, s_val)

    'list'
    if isinstance(getattr(students[0], a), str):
        pass
        
    'another data type'
    print(f'{a} is {type(getattr(students[0], a))}')
    print('more types will be handled in future revisions')

def main():
    print('stat')

if __name__ == '__main__':
    main()
