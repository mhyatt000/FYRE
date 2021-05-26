def string_to_list(list_as_string):
    container = []

    for course in list_as_string.replace(' ', '').split(","):
        temp = course.upper()
        container.append(temp)

    return container

'------------------------'

class Student:

    '''
        potentially make students a static vatiable
        students = []
        __init__():
            students.append(self)
    '''

    def __init__(self, timestamp, grade, major, credit_hours_2020,
        credit_hours_2021, courses,courses_asynchronous,
        courses_synchronous, courses_in_person, focus, strategies_applied,
        strategies_beneficial, notes_frequency, notes_is_handwritten, like_questions,
        structures, strategies, other, feedback, courses_hybrid, rating):

        self.timestamp = timestamp

        self.grade = grade
        self.major = major
        self.credit_hours_2020 = credit_hours_2020
        self.credit_hours_2021 = credit_hours_2021

        self.courses = string_to_list(courses)

        self.courses_asynchronous = courses_asynchronous
        self.courses_synchronous = courses_synchronous
        self.courses_in_person = courses_in_person

        self.focus = focus
        self.strategies_applied = strategies_applied
        self.strategies_beneficial = strategies_beneficial

        self.notes_frequency = notes_frequency

        if notes_is_handwritten == 'Handwritten':
            self.notes_is_handwritten = True
        else:
            self.notes_is_handwritten = False

        self.like_questions = like_questions
        self.structures = structures
        self.strategies = strategies

        self.other = other
        self.feedback = feedback

        self.courses_hybrid = courses_hybrid
        self.rating = rating

    def contains(self, criterion):
        for a in dir(self):
            if not a.startswith('__') and not callable(getattr(self, a)):
                attr = getattr(self, a)
                if(isinstance(attr, list)):
                    for c in attr:
                        if criterion == c.lower():
                            return True
                else:
                    if getattr(self, a).lower() == criterion:
                        return True
        return False

    def show_attr(self, attr):
        if attr in dir(self):
            print(attr + ": " + getattr(self, attr))

    def show(self):
        for a in dir(self):
            if not a.startswith('__') and not callable(getattr(self, a)):
                print(a + ': ' + str(getattr(self, a)))

    def set(self, a, value):
        'generic mutator method'
        for attr in dir(self):
            if str(attr) == a:
                self.attr = value

    def get_attrs(self) -> list:
        'returns the values of all attributes in a list'
        attr_list = []
        for a in dir(self):
            if not a.startswith('__') and not callable(getattr(self, a)):
                attr_list.append(getattr(self, a))
        return attr_list


class Poll_Question:


    def __init__():
        pass

    def p_value():
        pass

    def mean():
        pass

    def avg():
        pass
