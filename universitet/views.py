from django.shortcuts import render
from .models import Faculty, Student, Kafedra, Subject, Teacher, Group

def home_page(request):
    students = Student.objects.all()
    ctx = {'students': students}

    return render(request, 'home_page.html', ctx)

def faculties(request):
    faculties = Faculty.objects.all()
    ctx = {'faculties': faculties}

    return render(request, 'faculties.html', ctx)


def groups(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}

    return render(request, 'groups.html', ctx)


def kafedras(request):
    kafedras = Kafedra.objects.all()
    ctx = {'kafedras': kafedras}

    return render(request, 'kafedras.html', ctx)


def students(request):
    students = Student.objects.all()
    ctx = {'students': students}

    return render(request, 'students.html', ctx)

def subjects(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}

    return render(request, 'subjects.html', ctx)

def teachers(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}

    return render(request, 'teachers.html', ctx)