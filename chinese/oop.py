std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

#def print_score(std):
#    print('%s: %s' % (std['name'], std['score']))



# if there is no suitable object for inheritence, it will be (object)
class Student(object):

    def __init__(self, name, score): # when making instance, set the property
        self.name = name    # property
        self.score = score  # property

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# Class = Student
# Instance = Bart Simpson
