campus_name = "NuraDev"
student_count = 35
course_fee = 150000
is_registration_open = True

courses = ["Python", "Web Development", "Flutter", "Computer Basic"]
new_courses = ["AI for Life and Work", "Rust Programming"]

print(campus_name, type(campus_name))
print(student_count, type(student_count))
print(course_fee, type(course_fee))
print(is_registration_open, type(is_registration_open))
print(courses, type(courses))
print(new_courses, type(new_courses))

if student_count >= 30:
    print("Enrollment target achieved")
else:
    print("Need more students")

print(courses[0])
print(courses[1])
print(courses[-1])

courses[2] = "Moblile App Development"

courses.append("UI/UX Design")

courses.insert(1,"Scratch Coding")

courses.extend(new_courses)

courses.remove("Computer Basic")

courses.pop()

del courses[0]

print(courses)