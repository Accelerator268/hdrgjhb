from random import randint

student_list = ['Denis', 'Dima', '???', 'Dima G.', 'Dima T.', 'Alexey', 'X3', 'NN']
student_points_math = [randint(25, 50) for _ in range(len(student_list))]
student_points_phys = [randint(25, 50) for _ in range(len(student_list))]
student_points_eng = [randint(25, 50) for _ in range(len(student_list))]
student_pass = list(map(lambda x, y, z: x + y + z, student_points_math, student_points_phys, student_points_eng))
print(student_list)
print(student_pass)
print([student_list[i] for i in range(len(student_pass)) if student_pass[i]>=100])