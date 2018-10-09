class Student(object):

    def __init__(self, name, score):
        self.__name = name #__ private, 1 underscore = not private but don't visit, 2 underscores = private
        self.__score = score

    # encapsulation
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

     def set_score(self, score): # if change name with .__name, cannot, therefore need this function
        self.__score = score

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print bart.get_grade()

bart.__name # Student' object has no attribute '__name'
