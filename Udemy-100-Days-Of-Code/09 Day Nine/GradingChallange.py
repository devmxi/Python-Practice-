student_scores = {
    'Moksh': 88,
    'Alex': 87,
    'Amelia': 95,
    'Mat': 81,
    'Timon': 60,
}

#* dictionary of students and their corresponding test scores

student_grades = {} #* empty dictionary 

for name in student_scores: #* looping for every name in the dictionary 
    
    if student_scores[name] >= 91 and student_scores[name] <= 100: #* checking the range 
        grade = "Outstanding"
    elif student_scores[name] >= 81 and student_scores[name] <= 91:#* checking the range 
        grade = "Exceeds Expectations"
    elif student_scores[name] >= 71 and student_scores[name] <= 80:#* checking the range 
        grade = "Acceptable"
    elif student_scores[name] <= 70: #* checking the range 
        grade = "Fail"
    
    student_grades[name] = grade #* assigning key of name with the value of the grade they got

print(student_grades) #output