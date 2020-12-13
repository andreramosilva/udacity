names = input("Enter studant names separated by commas ex: Andre, juca , joao:   \n") # get and process input for a list of names
assignments =  input("Enter assignments counts for the studants separated by commas ex: 1, 7, 10:   \n")# get and process input for a list of the number of assignments
grades = input("Enter Grades for the studants separated by commas ex: 7, 10,0:  \n") # get and process input for a list of grades


# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
print(names,assignments,grades)
list_names = list(names.split(","))
list_assigments = list(assignments.split(","))
list_grades = list(grades.split(","))
pot_grade=[]
#print(list_names,list_assigments,list_grades)
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for index in  range(len(list_names)):
    #print(index)
    pot_grade.append(int(list_grades[index])+int(list_assigments[index])*2)
    print(message.format(list_names[index],list_assigments[index],list_grades[index],pot_grade[index]))
