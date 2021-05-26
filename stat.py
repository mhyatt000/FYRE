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
def avg_rating_attr(students: list, a):
    'if attribute is binary (True/False) then provide both average ratings'
    'else do nothing'
    try:
        if isinstance(getattr(students[0], a), bool):
            sum_true = 0
            count_true = 0

            sum_false = 0
            count_false = 0

            for student in students:
                if getattr(student, a):
                    sum_true += int(student.rating)
                    count_true +=1
                else:
                    sum_false += int(student.rating)
                    count_false += 1


            print(count1 + count2)
            dictionary = {f'{a} true: ': float(sum1) / count1, f'{a} false: ': float(sum2) / count2}
            print(dictionary)
        else:
            print(f'{a} is not boolean')
            print('will be handled in future revisions')
    except AttributeError:
        print(f'Student object has no attribute {a}')

def main():
    print('stat')

if __name__ == '__main__':
    main()
