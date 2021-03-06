"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept. 
   The three main design advatages of a object orientation are abstraction,
   encapsulation, and polymorphism. Abstraction permits programmers to take
   advatage of tools such as functions, methods, APIs, and many more without 
   having to understand the inner working of these tools down to each line of 
   code. The advantage of encapsulation is that it allows for bundling of data 
   with methods providing a coherent structure. Polymorphism affords programmers
   flexibility, as it indicats interchangeability of components such as objects. 

2. What is a class?
    A class is a type of structure used for grouping data and methods based on 
    shared similaries. A class definition creates a new class object (instance).  
    For example, if a program is written for a animal day care company, it would 
    make sense to create an Animals class to hold various methods to collect 
    information such a animal's age, gender, diet, etc. Since all animals share 
    these characteristics, we would create additional classes for each animal 
    type (e.g. bunny, cat, etc) that would inherit shared characteristics 
    such as age, gender since all animals have ages (not the
    same age, but all have "an" age).
  

3. What is an instance attribute?
    An instance attribute is an attribute owned by the specific instance 
    of a class. 

4. What is a method?
    A method is a function defined inside a class definition and is invoked 
    on instances of that classs. 

5. What is an instance in object orientation?
     An instance (also known as an object) is a an individual occurrence of a 
    class. To continue with the Animals example from earlier, an example of an
    instance would be "Milo", a dog that was instanciated to the Animals class.

6. How is a class attribute different than an instance attribute?
   Earlier, an instance attribute was defined as an attribute owned by a 
   specific instance of a class. A class attribute is shared by all instances.
   In the Animal class example, an appropriate class attribute would be a 
   neutered class ("neutered is True"), since no animal that attend day care 
   would be allowed in if they were not neutered. An appropriate instance 
   attribute would be an allergies instance attribute. Some animals may have 
   allergies and some animals may not. 
"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

    def __init__ (self, first_name, last_name, address):
        self.first_name =  first_name 
        self.last_name = last_name 
        self.address = address

    def get_first_name(self):
        return self.first_name   

class Question(object):

    def __init__ (self,question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer 


class Exam(object):
    def __init__ (self, questions, name):
        self.questions = []
        self.name = name 


    def adding_question_correct(self, question, correct_answer):
        Question.self = question + correct_answer
        exam.add_questions()


question1 = Exam()
question1 = adding_question_correct('questionisyes', 'answerisyes')



## Testing with my pets :)        

milo = Student('milo', 'quispe', '208 evans')
print milo.first_name  # You get milo 

math = Question("are you tired", "yes!!")
print math.question # You get "are you tired"

# exameee = Exam("you scared?","winter")
# print exameee.questions #You get "you scared?"









