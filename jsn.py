# # # # import json
# # # # student = {
# # # #     "name":"parshw",
# # # #     "age":20,
# # # #     "skills":["python","AI"]
# # # # }

# # # # json_data=json.dumps(student,indent=4)
# # # # print(json_data)
# # # import json

# # # data = '{"name":"Parshw","age":20}'

# # # python_data = json.loads(data)

# # # print(python_data["name"])

# # try:
# #     a = 10
# #     b = 0

# #     print(a / b)

# # except ZeroDivisionError:
# #     print("Cannot divide by zero")

# # finally:
# #     print("Execution Completed")


# # a= 2
# # if a % 2 == 0:
# #     print("Even")
# # else:

# #     print("odd")

# import math

# def is_prime(n):
#     # Primes must be greater than 1
#     if n <= 1:
#         return False
#     # 2 is the only even prime
#     if n == 2:
#         return True
#     # Eliminate all other even numbers
#     if n % 2 == 0:
#         return False
    
#     # Check odd factors from 3 up to sqrt(n)
#     limit = int(math.sqrt(n)) + 1
#     for i in range(3, limit, 2):
#         if n % i == 0:
#             return False
            
#     return True

# # Testing the function
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number!")
# else:
#     print(f"{num} is not a prime number.")

import json

class Student:

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def to_dict(self):
        return {
            "name": self.name,
            "skill": self.skill
        }

students = []

while True:

    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter name: ")
        skill = input("Enter skill: ")

        student = Student(name, skill)

        students.append(student.to_dict())

        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Student Added")

    elif choice == "2":

        try:
            with open("students.json", "r") as file:
                data = json.load(file)

                for student in data:
                    print(student)

        except FileNotFoundError:
            print("No data found")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")