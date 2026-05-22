# Agar key na mile to error nahi aata.

student = {
    "name": "Ravi",
    "age": 21
}

print(student.get("name q"))
student["city"] = "Ahmedabad"  # add
student["age"] = 25  # update
student.pop("age") # remove
del student["age"] # remove
student.clear()


print(student)



