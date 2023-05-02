#!/bin/Python3

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]]
print(gradebook)
[['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[4][1] += 5
poetry_grade = grades[2]
gradebook.remove(["poetry", poetry_grade])
gradebook[2].append("Pass")
last_semester_gradebook = [["Biology", 90], ["History", 80], ["French", 85]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
[['Biology', 90], ['History', 80], ['French', 85], ['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98]]
done

