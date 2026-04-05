class Garden:
    students_default = ['Alice',
               'Bob',
               'Charlie',
               'David',
               'Eve',
               'Fred',
               'Ginny',
               'Harriet',
               'Ileana',
               'Joseph',
               'Kincaid',
               'Larry']
    
    plants_names = {'G':'Grass',
            'C':'Clover',
            'R': 'Radishes',
            'V': 'Violets'}
    
    def __init__(self, diagram, students = None):

        if students is None:

            students = self.students_default

        diagram = diagram.splitlines()
        self.students = sorted(students)
        self.diagram = diagram

    def plants(self, name):


        start = (self.students.index(name) * 2)

        letters = self.diagram[0][start: start + 2] + self.diagram[1][start: start + 2]

        full_names = [self.plants_names[x] for x in letters]

        return full_names


        