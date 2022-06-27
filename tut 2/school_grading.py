# tutorial for grades
def grade(mark):
    if mark >= 75:
        return "First"
    elif mark < 75 and mark >= 70:
        return "Upper Second"
    elif mark < 70 and mark >= 60:
        return "Second"
    elif mark < 60 and mark >= 50:
        return "Third"
    elif mark < 50 and mark >= 45:
        return "F1 Supp"
    elif mark < 45 and mark >= 40:
        return "F2"   
    else:
        return "F3"
        # tried using it as list to find all grades at once but it had a pb
print(grade(83))             
print(grade(75)) 
print(grade(74.9)) 
print(grade(70)) 
print(grade(69.9)) 
print(grade(65)) 
print(grade(60)) 
print(grade(59.9)) 
print(grade(55)) 
print(grade(50)) 
print(grade(49.9)) 
print(grade(45)) 
print(grade(44.9)) 
print(grade(40)) 
print(grade(39.9)) 
print(grade(2)) 
print(grade(0)) 
