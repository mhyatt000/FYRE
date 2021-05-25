from FYRE import main

def avg_rating_notes(list: Student):
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

def avg_rating_attr(attr):
    '''
        types of attributes
        list
        binary
        string
    '''
