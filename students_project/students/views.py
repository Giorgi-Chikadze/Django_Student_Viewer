from django.shortcuts import render
import random


first_names = [
    "John", "Emma", "Olivia", "Liam", "Sophia", "James", 
    "Mia", "Isabella", "Ethan", "Ava", "Michael", "Charlotte"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", 
    "Garcia", "Miller", "Davis", "Martinez", "Hernandez", "Lopez"
]


def get_random_students():
    students = []
    for i in range(100):
        student = {
            "name": random.choice(first_names),
            "surname":random.choice(last_names),
            "gpa": round(random.uniform(2.0, 4.0), 2),
            "course": random.randint(1, 4),
        }
        students.append(student)
    return students


def main_page_view(request):
    students = get_random_students()
    selected_student = random.choice(students)
    return render(request, "main_page.html", {'student':selected_student})

def students_page_view(request):
    students = get_random_students()
    return render(request, "students_page.html", {'students':students})