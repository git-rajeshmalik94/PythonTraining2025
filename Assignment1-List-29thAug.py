#Write a Python program that manages a list of student scores. Perform the following operations step-by-step:
#Create an empty list to store scores.
student_scores = []

#Append the scores: 85, 90, 78, 92, 88
student_scores.extend([85, 90, 78, 92, 88])

#Insert the score 80 at index 2
student_scores.insert(2, 80)

#Remove the score 92 from the list
student_scores.remove(92)

#Sort the scores in ascending order
student_scores.sort()

#Reverse the list
student_scores.reverse()

#Find and print the maximum and minimum score
print('maximum score is :', max(student_scores))
print('minimum score is :', min(student_scores))

#Check if 90 is in the list
print('if 90 is in the list', 90 in student_scores)

#Print the total number of scores
print('total number of scores', sum(student_scores))

#Slice and print the first three scores
print('the first three scores', student_scores[:3])

#find the last element from the list
print('last element from the list is', student_scores[-1] )

#replace the score with new score on the index 2
student_scores[2] = "12"

#create a new copied list also
copied_score = student_scores.copy()

print('copied_score', copied_score)
