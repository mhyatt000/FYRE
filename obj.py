def string_to_list(list_as_string):
    container = []

    for course in list_as_string.replace(' ', '').split(","):
        temp = course.upper()
        container.append(temp)

    return container

'------------------------'

class Student:

    def __init__(self, timestamp, grade, major, credit_hours_2020,
        credit_hours_2021, courses,courses_asynchronous,
        courses_synchronous, courses_in_person, focus, strategies_applied,
        strategies_beneficial, notes_frequency, notes_type, like_questions,
        structures, strategies, other, feedback, courses_hybrid, online_rating):

        self.timestamp = timestamp

        self.grade = grade
        self.major = major
        self.credit_hours_2020 = credit_hours_2020
        self.credit_hours_2021 = credit_hours_2021

        'courses'
        self.courses = string_to_list(courses)

        self.courses_asynchronous = courses_asynchronous
        self.courses_synchronous = courses_synchronous
        self.courses_in_person = courses_in_person

        self.focus = focus
        self.strategies_applied = strategies_applied
        self.strategies_beneficial = strategies_beneficial

        self.notes_frequency = notes_frequency
        self.notes_type = notes_type

        self.like_questions = like_questions
        self.structures = structures
        self.strategies = strategies

        self.other = other
        self.feedback = feedback

        self.courses_hybrid = courses_hybrid
        self.online_rating = online_rating

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

        print(f'{self.grade}, {self.major}')
        print(f'credit hours: {self.credit_hours_2020} {self.credit_hours_2021}')
        print(self.courses)
        print()

        '''
        for a in dir(self):
            if not a.startswith('__') and not callable(getattr(self, a)):
                print(getattr(self, a))
                print(a)
        '''

class Poll_Question:


    def __init__():
        pass

    def p_value():
        pass

    def mean():
        pass

    def avg():
        pass
