from django.shortcuts import render
from director.models import Director
from zauch.models import Zauch
from Student.models import Student
from curator.models import Curator
from grade.models import Grade
from lesson.models import Lesson





def index(request):
    return render(request, 'main/index.html')


def view_director(request):
    director = Director.objects.all()
    
    context = {
        'director_context': director
    }

    return render(request, 'main/director.html', context)


def view_zauch(request):
    zauch = Zauch.objects.all()

    context = {
        'zauch_context': zauch
    }

    return render(request, 'main/zauch.html', context)


def view_student(request):
    student = Student.objects.all()

    context = {
        'student_context': student
    }
    
    return render (request, 'main/student.html', context)

def view_curator(request):
    curator = Curator.objects.all()

    context = {
        'curator_context': curator
    }
    
    return render(request, 'main/curator.html', context)


def view_grade(request):
    grade = Grade.objects.all()

    context = {
        'grade_context': grade
    }
    
    return render(request, 'main/grade.html', context)

def view_lesson(request):
    lesson = Lesson.objects.all()

    context = {
        'lesson_context': lesson
    }
    return render(request, 'main/lesson.html', context)



















