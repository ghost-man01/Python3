courses = {"Python Programming", "RDBMS", "Web Technology", "Soft Engg"}
elective = {"Bussiness Intelligence", "Big Data Analytics"}

num = len(courses)
print("Number of couses opted by John", num)

list1 = list(courses)
print(list1)

update_courses = str(courses)+str(elective)
print("Courses with electives:",update_courses)