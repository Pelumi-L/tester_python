#print an person object with name, gender, qualification, occupation. then a child object with firstname and surname(coming from person name), class, describe the child in reference to the parent
class Person():
     def __init__(self, surname, firstname, gender, qualification, occupation):
          self.surname = surname
          self.firstname = firstname
          self.gender = gender
          self.qualification = qualification
          self.occupation = occupation
     def lname(self):
          print(f"Surname: {self.surname}")
     def fname(self):
          print(f"Firstname: {self.firstname}")
     def sex(self):
          print(f"Gender: {self.gender}")
     def qual(self):
          print(f"Qualification: {self.qualification}")
     def job(self):
          print(f"Occupation: {self.occupation}")
profile = Person("Dragneel", "Natsu", "Male", "B.Sc", "Engineer")
profile.lname()
profile.fname()
profile.sex()
profile.qual()
profile.job()

class Child(Person):
     def __init__(self, surname, firstname, gender, qualification, occupation, childfname, childgender, child_description):
          super().__init__(surname, firstname, gender, qualification, occupation)
          self.childfname = childfname
          self.childgender = childgender
          self.child_description = child_description
     def chdfname(self):
          print(f"Name: {self.childfname}")
     def chdsex(self):
          print(f"Dender: {self.childgender}")
     def chd_desc(self):
          print(f"Description: {self.child_description} {self.surname} {self.childfname}")
childprofile = Child("Dragneel", "", "", "", "", "Nashi", "Female", "Her full name is" )
childprofile.chdfname()
childprofile.chdsex()
childprofile.chd_desc()