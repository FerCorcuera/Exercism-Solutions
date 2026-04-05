class School:
    def __init__(self):

        self.grades = {}
        self.added_studends = []
        

    def add_student(self, name, grade):
        
        if grade not in self.grades.keys():

            self.grades[grade] = []

        final_roaster = self.roster()
        if name not in final_roaster:

            self.grades[grade].append(name)
            self.added_studends.append(True)

        else:

            self.added_studends.append(False)
        
    def roster(self):

        final_roaster  = []
        
        for x in sorted(self.grades):
            
            final_roaster.extend(sorted(self.grades[x]))

        return final_roaster

    def grade(self, grade_number):

        if grade_number in self.grades:
            return sorted(self.grades[grade_number])
        else:
            return []

    def added(self):

        return self.added_studends
