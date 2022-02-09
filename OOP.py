#!/usr/bin/env python
# coding: utf-8

# In[192]:


def avrg(dct):
    smm = 0    
    count = 0
    for grades in dct.values():
        for grade in grades:
            smm += grade
            count += 1
    return smm/count

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade): #Оценивать можно только завершенные курсы
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 
        
    def calc_avrg(self):
        self.avrg = avrg(self.grades)  
    
    def __str__(self):
        self.calc_avrg()
        res = ""
        res += f"Имя: {self.name}\n"
        res += f"Фамилия: {self.surname}\n"
        res += f"Средняя оценка за домашние задания: {self.avrg}\n"
        res += "Курсы в процессе обучения: "
        for i, course in enumerate (self.courses_in_progress):
            if i : res += ","
            res += " " + course
        res += "\nЗавершенные курсы: "
        for i, course in enumerate (self.finished_courses):
            if i : res += ","
            res += " " + course        
        return res
            
        
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    


class Reviewer(Mentor):
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
       
    def __str__(self):
        res = ""
        res += f"Имя: {self.name}\n"
        res += f"Фамилия: {self.surname}\n"
        return res 



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def calc_avrg(self):
        self.avrg = avrg(self.grades)  
    
    def __str__(self):
        self.calc_avrg()
        res = ""
        res += f"Имя: {self.name}\n"
        res += f"Фамилия: {self.surname}\n"
        res += f"Средняя оценка за лекции: {self.avrg}\n"
        return res
    
    def __lt__(self, other_lecturer):
        self.calc_avrg()
        other_lecturer.calc_avrg()
        return self.avrg < other_lecturer.avrg


# In[193]:


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

other_student = Student("William", "Gosset", "male")

 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)


cool_reviewer.rate_hw(best_student, 'Git', 9)
 
#print(best_student.grades)


# In[195]:


gann = Lecturer("Gannibal", "Lecter")
gann.courses_attached.append("Math")

jac = Lecturer("Jacque", "Fresco")
jac.courses_attached.append("Math")


#print(Gann.courses_attached)
best_student.finished_courses.append("Math")
best_student.finished_courses.append("Введение в программирование")



other_student.finished_courses.append("Math")


# In[196]:


best_student.rate_lecturer(gann, "Math", 5)
other_student.rate_lecturer(gann, "Math", 10)
other_student.rate_lecturer(jac, "Math", 9)


# In[197]:


print(gann.grades)


# In[198]:


print(cool_reviewer)


# In[200]:


print(best_student)


# In[199]:


print(gann)


# In[201]:


print(jac)


# In[202]:


jac > gann


# In[ ]:




